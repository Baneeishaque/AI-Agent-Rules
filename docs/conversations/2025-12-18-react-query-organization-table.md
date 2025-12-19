# Conversation Log: React Query & OrganizationTable Deep Dive

**Date**: December 18, 2025
**Objective**: Explain and optimize React Query usage in the `OrganizationTable.tsx` component.

## 1. Initial Request
The user requested an explanation of `export default React.memo(App);` (Line 2308) in the `OrganizationTable.tsx` file.

## 2. Key Topics Explained

### 2.1 `React.memo` (Line 2308)
- **Purpose**: Higher-order component that prevents unnecessary re-renders.
- **Mechanism**: Performs shallow comparison of props. If unchanged, React skips rendering the component.
- **Application**: Wrapping the `App` component (which provides `QueryClientProvider`) to avoid re-renders when parent renders for unrelated reasons.

### 2.2 `QueryClientProvider` Pattern (Lines 2282-2306)
The `App` component wraps `OrganizationTable` with `<QueryClientProvider>`:
```tsx
function App({ contractCreated, setCopiedData, ... }) {
  return (
    <QueryClientProvider client={queryClient}>
      <OrganizationTable ... />
    </QueryClientProvider>
  );
}
```

**Key Points Explained**:
1. **Wrapping**: Creates a "scope" enabling React Query hooks (`useQuery`, `useMutation`) in all child components.
2. **`queryClient`**: The "brain" holding cache, configuration, and query state.
3. **Hooks**: `useQuery` reads data, `useMutation` modifies data—both access the shared cache.

### 2.3 Performance Concerns with Large Data (5k+ Rows)
**User Question**: Is React Context a problem with large datasets?

**Answer**: No. Context only carries the `queryClient` instance (a tiny object), not the data itself. The real bottleneck is **DOM rendering**, not Context.

**Current Approach (Already Optimal)**:
- Server-side pagination (`pageSize: 50`) ensures only 50 rows render at a time.
- Virtualization (built into MaterialReactTable) can handle larger client-side datasets.

### 2.4 `queryClient` Creation & Optimization
**Current Code**:
```tsx
const queryClient = new QueryClient(); // Line 2280 (module-level)
```

**Assessment**:
- ✅ **Stable singleton**: Created once, persists for tab lifetime.
- ⚠️ **Caution**: If a global provider already exists at the app root, this creates a cache silo.

**Recommendations for Maximum Performance**:
1. Ensure parent passes stable function references (`useCallback`).
2. Keep `staleTime` (5 mins) to prevent unnecessary refetches.
3. Consider row virtualization if client-side data exceeds 1000 rows.

### 2.5 `useQuery` Hook Deep Dive (Lines 706-724)
```typescript
return useQuery<{ results: User[]; totalCount: number }>({
  queryKey: ["users", { filters, pagination, sorting, tab }],
  queryFn: async () => { ... },
  refetchOnWindowFocus: false,
  placeholderData: (old) => old,
  staleTime: 5 * 60 * 1000,
  gcTime: 10 * 60 * 1000,
});
```

| Option | Purpose |
|--------|---------|
| `queryKey` | Unique identifier; auto-refetches when values change |
| `refetchOnWindowFocus: false` | Prevents refetch on tab focus |
| `placeholderData: (old) => old` | Keep previous data during pagination (no flash) |
| `staleTime: 5 min` | Cache considered fresh for 5 minutes |
| `gcTime: 10 min` | Data kept in memory for 10 minutes after unmount |

### 2.6 State Management Patterns

#### `isFirstRender` (Line 141)
```tsx
const isFirstRender = useRef(true);
```
- **Purpose**: Flag to skip side effects (e.g., saving to SessionStorage) on initial render.
- **Usage**: `if (isFirstRender.current) return;` inside `saveToSessionStorage`.

#### Filter & Visibility State (Lines 142-151)
| State | Purpose |
|-------|---------|
| `filterModes` | Advanced filter data (`{ mode, id, value }`) for API query params |
| `columnFilters` | MRT's internal filter UI state |
| `columnVisibility` | Tracks hidden/visible columns for user customization |

## 3. Summary
The current implementation follows React Query best practices:
- Server-side pagination avoids large DOM overhead.
- `staleTime` and `gcTime` optimize cache behavior.
- `React.memo` prevents unnecessary re-renders.
- Module-level `queryClient` ensures cache persistence.
