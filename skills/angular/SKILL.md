---
name: angular
description: Angular component architecture, RxJS patterns, change detection, and module organization
---

## Angular Code Review Rules

### Module Organization
- Feature modules should be lazy-loaded where possible
- Shared module for reusable components/pipes/directives
- Core module for singleton services (provided in root)
- Avoid circular module dependencies

### Components
- Use `OnPush` change detection strategy for performance
- Inputs should be immutable (don't mutate input objects)
- Use `trackBy` function with `*ngFor` for lists
- Prefer standalone components for new code (Angular 14+)

### RxJS
- Always unsubscribe (use `takeUntilDestroyed()`, `async` pipe, or `DestroyRef`)
- Avoid nested subscribes (use `switchMap`, `mergeMap`, `concatMap`)
- Use `shareReplay` for HTTP calls that multiple subscribers need
- Handle errors with `catchError` (don't let errors kill the stream)

### Services
- Services should be `providedIn: 'root'` unless scoped to feature
- Use dependency injection, don't instantiate services manually
- HTTP calls belong in services, not components

### Templates
- Avoid complex logic in templates (use getters or pipes)
- Use `ng-container` for structural directives without extra DOM
- Sanitize dynamic HTML with `DomSanitizer` if needed

### Security
- Avoid `bypassSecurityTrust*` unless absolutely necessary
- Validate route parameters and query strings
- Use Angular's built-in CSRF protection with HttpClient

### Testing
- Use `@angular/testing` utilities (TestBed, ComponentFixture)
- Write unit tests for components, services, and pipes
- Mock dependencies in tests (don't use real HTTP calls)
- Test component inputs/outputs and DOM interactions
- Use `async` and `fakeAsync` for testing asynchronous code

### Type Safety
- Enable strict TypeScript mode in tsconfig.json
- Use `strictTemplates: true` in Angular compiler options
- Avoid `any` type - use proper interfaces/types
- Type all function parameters and return values

### Accessibility
- Use semantic HTML elements (e.g., `<button>` not `<div>` with click)
- Include ARIA labels and roles where needed
- Ensure keyboard navigation works for interactive elements
- Test with screen readers and accessibility tools
- Maintain proper heading hierarchy (h1, h2, h3)

### State Management
- Use NgRx or Akita for complex shared state
- Signals (Angular 16+) for reactive local state
- Services with BehaviorSubject for simple shared state
- Avoid component state for data shared across routes

### Internationalization
- Use Angular i18n for localization
- Mark translatable text with `i18n` attribute
- Extract translations with `ng extract-i18n`
- Serve locale-specific builds or use runtime translation

### Linting and Code Style
- Use ESLint with @angular-eslint rules
- Follow Angular style guide conventions
- Use Prettier for consistent code formatting
- Enable editor support for automatic linting/formatting
