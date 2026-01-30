---
name: nextjs
description: Next.js 14+ App Router patterns, Server Components, API routes, and performance optimization
---

## Next.js Code Review Rules

### App Router Structure
- Verify `app/` directory structure follows conventions (`page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`)
- Check `use client` directive is only used when necessary (event handlers, hooks, browser APIs)
- Server Components should not import client-only libraries (useState, useEffect, etc.)
- Implement error boundaries with `error.tsx` for error handling
- Use error boundaries to catch and handle errors in Server Components
- Provide fallback UIs for errors with proper error messages

### Data Fetching
- Prefer Server Components for data fetching over client-side fetching
- Check for proper use of `cache()` for request deduplication
- Validate `revalidate` options for ISR (Incremental Static Regeneration)
- Ensure `generateStaticParams()` is used for static generation of dynamic routes

### Performance
- Images must use `next/image` with explicit `width`/`height` or `fill`
- Fonts should use `next/font` for automatic optimization
- Check for proper `Suspense` boundaries around async components
- Verify no blocking data fetches in layouts (affects all child routes)

### Security
- Server Actions must validate input
- No secrets exposed in client components
- Check `headers()` and `cookies()` usage is server-side only

### API Routes
- Validate HTTP methods (check `req.method` or use route handlers)
- Implement authentication and authorization
- Return appropriate HTTP status codes
- Handle errors gracefully with try-catch
- Sanitize and validate all inputs
- Use proper CORS headers when needed

### Accessibility
- Use semantic HTML elements
- Include `alt` text on all images
- Ensure keyboard navigation works
- Test with screen readers
- Maintain proper heading hierarchy
- Add ARIA labels where needed

### Testing
- Write unit tests for critical components
- Test Server Components and Server Actions
- Use integration tests for data fetching flows
- Test error boundaries and error states
- Include e2e tests for critical user flows
- Validate test coverage for mission-critical features

### Dependencies
- Keep Next.js and React versions compatible
- Check for breaking changes when updating
- Audit third-party packages for security and compatibility
- Use official Next.js plugins when available
- Avoid excessive dependencies for simple functionality

### Edge Runtime
- Review usage of Edge runtime for API routes
- Ensure Edge-compatible code (no Node.js-specific APIs)
- Use Edge runtime for latency-sensitive operations
- Be aware of Edge runtime limitations (memory, execution time)
- Test Edge functions thoroughly

### Common Anti-patterns
- Avoid `use client` at layout level (makes all children client components)
- Avoid fetching same data in multiple components (use cache or pass as props)
- Avoid `dynamic = 'force-dynamic'` without justification
