---
name: bicep
description: Azure Bicep IaC patterns, parameterization, security, and modular design
---

## Bicep Code Review Rules

### Security (Critical)
- Never hardcode secrets, connection strings, or keys
- Use Key Vault references for secrets
- Apply least privilege to managed identities
- Enable diagnostic settings for auditing
- Use private endpoints where available
- Enforce encryption at rest for all supported resources
- Validate Azure Policy compliance for resources
- Check regulatory standards compliance (HIPAA, PCI-DSS, etc.)
- Always escape or validate user-provided strings before using them in resource names, tags, and outputs to prevent injection risks
- Never use HTML comments (`<!-- -->`) or expose template syntax in outputs

### Parameters
- Use parameters for values that vary between deployments
- Mark sensitive parameters with `@secure()` decorator
- Provide `@description()` for all parameters
- Use `@allowed()` for constrained values
- Set sensible `@minLength()`, `@maxLength()`, `@minValue()`, `@maxValue()`
- Provide default values where appropriate to reduce required inputs
- Validate complex parameter types with parameter constraints, assertions, or custom validation logic
- Document parameter purpose and expected values

### Resource Naming (Essential)
- Use consistent naming convention
- Include environment, region, workload in names
- Use `uniqueString()` for globally unique names
- Follow Azure naming rules and restrictions

### Resource Tagging
- Tag all resources with standard tags (owner, environment, cost center)
- Use consistent tag naming conventions
- Include tags for governance (compliance, data classification)
- Define required tags in policy and enforce them

### Modules
- Break down large templates into modules
- One module per logical resource group
- Use outputs to pass values between modules
- Store shared modules in a registry

### Best Practices
- Use `existing` keyword to reference existing resources
- Use `dependsOn` only when implicit dependencies aren't enough
- Prefer symbolic names over `resourceId()` functions
- Use loops (`for`) instead of copy-paste for similar resources
- Include template metadata block with author, version, and docs
- Use meaningful error messages with `assert()` for validation

### API Version Management
- Avoid deprecated or preview resource API versions unless justified
- Document reasons for using preview features

### Outputs
- Output only values needed by other templates/scripts
- Mark sensitive outputs with `@secure()` (Bicep handles this)
- Include resource IDs for downstream references

### Example Patterns
```bicep
@description('Environment name')
@allowed(['dev', 'staging', 'prod'])
param environment string

@description('SQL admin password')
@secure()
param sqlAdminPassword string

metadata description = 'Azure Storage Account with Key Vault integration'
metadata author = 'Infrastructure Team'
metadata version = '1.0.0'

var baseName = 'myapp-${environment}-${uniqueString(resourceGroup().id)}'
var commonTags = {
  environment: environment
  owner: 'infrastructure-team'
  costCenter: 'IT-001'
}

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: '${baseName}sa'
  location: resourceGroup().location
  tags: commonTags
  sku: { name: 'Standard_LRS' }
  kind: 'StorageV2'
  properties: {
    minimumTlsVersion: 'TLS1_2'
    supportsHttpsTrafficOnly: true
  }
}
```
