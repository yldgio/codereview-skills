---
name: angular
description: Angular component architecture, RxJS patterns, change detection, and module organization
---

## Angular Code Review Rules

### Security
- Avoid `bypassSecurityTrust*` methods unless absolutely necessary; when used, require code comments justifying the bypass
- Sanitize dynamic HTML with `DomSanitizer` only when needed; always prefer Angular's built-in sanitization
- Validate route parameters and query strings to prevent injection attacks
- Use Angular's built-in CSRF protection with HttpClient
- Template variables (e.g., `*ngFor`, `trackBy`) should explicitly declare variables and avoid dynamic interpolation where possible
- Never interpolate untrusted user input into templates without proper sanitization

### Module Organization
- Feature modules should be lazy-loaded where possible
- Use `SharedModule` for reusable components/pipes/directives; explicitly define exports to avoid accidental global scope exposure
- Use `CoreModule` for singleton services (provided in root); import only once in AppModule
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
- Never use dynamic HTML with `[innerHTML]` without proper sanitization; review all XSS risks

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
- For advanced accessibility patterns, see [Angular Accessibility Guide](https://angular.io/guide/accessibility)

### State Management (Advanced)
- Use NgRx or Akita for complex shared state
- Signals (Angular 16+) for reactive local state
- Services with BehaviorSubject for simple shared state
- Avoid component state for data shared across routes

### Internationalization (Advanced)
- Use Angular i18n for localization
- Mark translatable text with `i18n` attribute
- Extract translations with `ng extract-i18n`
- Serve locale-specific builds or use runtime translation
- For detailed i18n patterns, see [Angular i18n Guide](https://angular.io/guide/i18n-overview)

### Linting and Code Style
- Use ESLint with @angular-eslint rules
- Follow Angular style guide conventions
- Use Prettier for consistent code formatting
- Enable editor support for automatic linting/formatting
