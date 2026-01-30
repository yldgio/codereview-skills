---
name: vercel-composition-patterns
description: React composition patterns that scale. Use when refactoring components with boolean prop proliferation, building flexible component libraries, or designing reusable APIs. Triggers on tasks involving compound components, render props, context providers, or component architecture. Includes React 19 API changes.
license: MIT
metadata:
  author: vercel
  version: "1.0.0"
  source: https://github.com/vercel-labs/agent-skills
---

# React Composition Patterns

Composition patterns for building flexible, maintainable React components. Avoid boolean prop proliferation by using compound components, lifting state, and composing internals. These patterns make codebases easier for both humans and AI agents to work with as they scale.

## When to Apply

Reference these guidelines when:

- Refactoring components with many boolean props
- Building reusable component libraries
- Designing flexible component APIs
- Reviewing component architecture
- Working with compound components or context providers

## Code Review Criteria

When reviewing code, check for:

- **Boolean prop proliferation**: Components with >3 boolean props for variants/modes
- **Render props**: Use of `renderX` props instead of `children` composition
- **Direct state access**: Components accessing context/state outside provider pattern
- **Tightly coupled logic**: UI components with embedded business logic
- **Missing accessibility**: Compound components without proper ARIA attributes

### Migration Guidance

When refactoring legacy patterns:

- **From render props to composition**: Replace `renderHeader={() => <Header />}` with `<Component.Header />`
- **From boolean flags to variants**: Convert `<Button primary large />` to `<Button variant="primary" size="large" />`
- **From prop drilling to composition**: Extract shared state into context provider
- **React 19 migration**: Remove `forwardRef` wrappers, replace `useContext` with `use()`

### Accessibility

Ensure composition patterns maintain accessibility:

- Compound components must preserve semantic HTML relationships
- ARIA attributes should propagate through composition layers
- Keyboard navigation must work across component boundaries
- Screen reader announcements should be logical and complete
- Focus management must be handled correctly in nested components

## Rule Categories by Priority

| Priority | Category                | Impact | Prefix          |
| -------- | ----------------------- | ------ | --------------- |
| 1        | Component Architecture  | HIGH   | `architecture-` |
| 2        | State Management        | MEDIUM | `state-`        |
| 3        | Implementation Patterns | MEDIUM | `patterns-`     |
| 4        | React 19 APIs           | MEDIUM | `react19-`      |

## Quick Reference

### 1. Component Architecture (HIGH)

- `architecture-avoid-boolean-props` - Don't add boolean props to customize behavior; use composition
- `architecture-compound-components` - Structure complex components with shared context

### 2. State Management (MEDIUM)

- `state-decouple-implementation` - Provider is the only place that knows how state is managed
- `state-context-interface` - Define generic interface with state, actions, meta for dependency injection
- `state-lift-state` - Move state into provider components for sibling access

### 3. Implementation Patterns (MEDIUM)

- `patterns-explicit-variants` - Create explicit variant components instead of boolean modes
- `patterns-children-over-render-props` - Use children for composition instead of renderX props

### 4. React 19 APIs (MEDIUM)

> **React 19+ only.** Skip this section if using React 18 or earlier.

- `react19-no-forwardref` - Don't use `forwardRef`; use `use()` instead of `useContext()`
- `react19-use-api` - Use `use()` hook for promises and context (replaces `useContext`)
- `react19-actions` - Use Server Actions and form actions for data mutations
- `react19-suspense-updates` - Leverage improved Suspense for data fetching patterns

### Performance Implications

Consider performance when using composition patterns:

- **Render optimization**: Memoize compound component children to prevent unnecessary re-renders
- **Context splitting**: Split context into multiple contexts to minimize re-renders
- **Provider placement**: Place providers as low in tree as possible
- **State colocation**: Keep state close to where it's used
- **Composition overhead**: Balance flexibility with render performance

## Example: Avoid Boolean Props

### Incorrect

```tsx
// Boolean prop proliferation
<Button primary large disabled loading />
```

### Correct

```tsx
// Explicit variants via composition
<Button variant="primary" size="large">
  <Button.Loader />
  Submit
</Button>
```

## Example: Compound Components

```tsx
// Parent provides context
<Accordion>
  <Accordion.Item>
    <Accordion.Trigger>Section 1</Accordion.Trigger>
    <Accordion.Content>Content 1</Accordion.Content>
  </Accordion.Item>
</Accordion>
```

## Example: State Context Interface

```tsx
interface ContextValue<T> {
  state: T;
  actions: Actions;
  meta: { loading: boolean; error: Error | null };
}
```

## Example: Explicit Variants (Detailed)

### Before: Boolean Props

```tsx
// Harder to maintain as props grow
<Button primary large disabled loading icon="check" />
```

### After: Explicit Variants

```tsx
// Clearer intent, easier to extend
<Button variant="primary" size="large" disabled>
  <Button.Icon name="check" />
  <Button.Loader />
  Submit
</Button>
```

## Example: State/Context Pattern

### Provider Implementation

```tsx
// Provider knows implementation details
function TodoProvider({ children }) {
  const [todos, setTodos] = useState([]);
  
  const value = {
    state: todos,
    actions: {
      add: (todo) => setTodos([...todos, todo]),
      remove: (id) => setTodos(todos.filter(t => t.id !== id))
    },
    meta: { loading: false, error: null }
  };
  
  return <TodoContext.Provider value={value}>{children}</TodoContext.Provider>;
}
```

### Consumer Implementation

```tsx
// Consumer uses generic interface
function TodoList() {
  const { state: todos, actions } = use(TodoContext);
  return todos.map(todo => <TodoItem key={todo.id} {...todo} onRemove={actions.remove} />);
}
```
