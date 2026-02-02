---
name: fastapi
description: FastAPI endpoint design, Pydantic validation, dependency injection, and async patterns
---

## FastAPI Code Review Rules

### Security (Critical)
- Validate and sanitize all inputs to prevent injection attacks
- Use `OAuth2PasswordBearer` or similar for auth
- Rate limit sensitive endpoints
- Never log sensitive data (passwords, tokens)
- Implement CORS properly with `CORSMiddleware`
- Use CSRF protection for cookie-based auth
- Validate content types and sanitize HTML to prevent XSS
- Use security headers (HSTS, CSP, X-Frame-Options)
- Always validate user input in path operations and request bodies
- Never use HTML comments (`<!-- -->`) in production code

### Endpoint Design
- Use appropriate HTTP methods (GET for reads, POST for creates, etc.)
- Return appropriate status codes (201 for create, 204 for delete, etc.)
- Use path parameters for resource identifiers, query params for filtering
- Group related endpoints with `APIRouter` and tags
- Document endpoints with clear docstrings
- Use OpenAPI metadata (summary, description, response descriptions)
- Provide detailed response model documentation
- Implement API versioning (URL prefix recommended)
- Mark deprecated endpoints with `deprecated=True`

### Pydantic Models
- Use Pydantic models for request body validation (not raw dicts)
- Define explicit response models with `response_model` parameter
- Use `Field()` for validation constraints (min/max, regex, etc.)
- Separate input models from output models (Create vs Response)
- Use type annotations for all endpoint arguments and return types
- Return only JSON-serializable results
- Use `model_config` for Pydantic v2 configuration

### Dependency Injection
- Use `Depends()` for shared logic (auth, db sessions, etc.)
- Database sessions should be dependencies, not global
- Close resources properly (use context managers or finally)

### Async
- Use `async def` for I/O-bound endpoints
- Don't mix sync and async database calls
- Use `asyncio.gather()` for parallel async operations
- Avoid blocking calls in async functions (use `run_in_executor`)

### Advanced Async Patterns
- Use async context managers (`async with`) for managing async resources (DB sessions, HTTP clients)
- Use `BackgroundTasks` for work that should outlive the response
- Use startup/shutdown events (`@app.on_event("startup"/"shutdown")`) to initialize/cleanup shared async resources
- Apply concurrency limits with `asyncio.Semaphore` when calling external services
- For streaming responses or WebSockets, implement backpressure-aware designs
- For more patterns, see [FastAPI Async Documentation](https://fastapi.tiangolo.com/async/)

### Error Handling
- Use `HTTPException` for expected errors with proper status codes
- Create custom exception handlers for domain exceptions
- Don't expose internal error details to clients
- Log errors with context (request ID, user, etc.)

### Project Structure
- Organize by feature or layer (routers, models, services, dependencies)
- Keep routers thin - business logic in services
- Separate Pydantic models from database models
- Use a `dependencies` module for reusable dependencies
- Create `config.py` for settings management
