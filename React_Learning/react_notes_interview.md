# React Interview Prep (1 Year Experience – Backend Developer Transitioning to Full-Stack)

**Target company:** Safran Digit  
**Skills mentioned by HR:** Python, FastAPI, React, Cloud  
**My positioning:** Primarily a backend developer (FastAPI/Python) with **~1 year of React experience** building UI screens and dashboards, often using AI coding assistants.

---

# 1. React Introduction (What I’ll Say in Interview)

## 30-second answer

```text
I am primarily a backend developer working with Python and FastAPI, but for the last year I have also worked on React-based UIs. I have built dashboard screens, forms, tables, and API integrations, and I am comfortable with hooks, routing, state management, and performance optimizations like lazy loading and memoization. I usually collaborate closely with frontend developers and use modern tooling such as Vite, React Router, Tailwind CSS, and Redux Toolkit when needed.
```

---

# 2. Highest Priority Topics (Prepare First)

| Priority | Topic |
|---|---|
| Must | Hooks (useState, useEffect, useRef) |
| Must | Virtual DOM & Reconciliation |
| Must | SSR vs CSR |
| Must | Lazy loading & Suspense |
| Must | React Router & Protected Routes |
| Must | State vs Props |
| Must | Redux Toolkit basics |
| Must | API calls with async/await |
| Must | Performance optimization |
| Good | Custom Hooks |
| Good | useMemo / useCallback |
| Good | Testing basics |
| Optional | Higher Order Components |

---

# 3. React Hooks (Very Important)

## useState

### What is it?
Used to create and update local component state.

```jsx
const [count, setCount] = useState(0);
```

### Common question
**Why is state update asynchronous?**

- React batches updates for performance.
- Multiple updates may be combined into one render.

```jsx
setCount(prev => prev + 1);
```

---

## useEffect

### What is it?
Used for side effects such as API calls, subscriptions, and timers.

### Run once

```jsx
useEffect(() => {
  fetchData();
}, []);
```

### Run when dependency changes

```jsx
useEffect(() => {
  fetchUser(userId);
}, [userId]);
```

### Cleanup

```jsx
useEffect(() => {
  const timer = setInterval(() => console.log('tick'), 1000);

  return () => clearInterval(timer);
}, []);
```

### Most asked question
**What happens if dependency array is missing?**

- Effect runs after every render.
- Can cause infinite loops if state is updated inside it.

---

## useRef

### Use cases

- Access DOM elements
- Store mutable values without re-rendering

```jsx
const inputRef = useRef();

<input ref={inputRef} />

inputRef.current.focus();
```

---

## useMemo

### Why use it?
Memoizes expensive calculations.

```jsx
const total = useMemo(() => {
  return items.reduce((a, b) => a + b.price, 0);
}, [items]);
```

### When NOT to use?
Do not use for simple calculations; memoization itself has a cost.

---

## useCallback

### Why use it?
Prevents function recreation on every render.

```jsx
const handleClick = useCallback(() => {
  console.log('clicked');
}, []);
```

### Difference from useMemo

- `useMemo` → memoizes **value**
- `useCallback` → memoizes **function**

---

## 4. Component Lifecycle (Functional Components)

### What is a lifecycle?

A React component goes through **3 phases** during its existence:

1. **Mount** → Component is created and added to the screen.
2. **Update** → Component re-renders because state or props changed.
3. **Unmount** → Component is removed from the screen.

Think of it like a popup window:

- **Mount** = popup opens
- **Update** = popup content changes
- **Unmount** = popup closes

---

## Mount Phase (Component appears on screen)

### Code

```jsx
useEffect(() => {
  console.log('mounted');
}, []);
```

### Why `[]` ?

- Empty dependency array means **run only once** after the first render.

### Real UI examples

#### Fetch data when page opens

```jsx
useEffect(() => {
  fetchUsers();
}, []);
```

- User opens `/users`
- API is called once
- Data is displayed

#### Start a timer

```jsx
useEffect(() => {
  const timer = setInterval(() => {
    console.log('tick');
  }, 1000);
}, []);
```

#### Add event listener

```jsx
useEffect(() => {
  window.addEventListener('resize', handleResize);
}, []);
```

### Interview explanation

> Mount phase is useful for initialization tasks such as API calls, loading user data, starting timers, opening WebSocket connections, or registering event listeners.

---

## Update Phase (Component data changes)

### Code

```jsx
useEffect(() => {
  console.log('updated');
}, [value]);
```

### What triggers update?

- `setState()`
- Parent passes new props
- Context value changes

### Example

```jsx
const [search, setSearch] = useState('');

useEffect(() => {
  searchProducts(search);
}, [search]);
```

### What happens?

- User types in search box
- `search` state changes
- Effect runs again
- New API request is made

### Real UI examples

#### Search suggestions

```jsx
useEffect(() => {
  fetchSuggestions(query);
}, [query]);
```

#### Filter table data

```jsx
useEffect(() => {
  applyFilters(filters);
}, [filters]);
```

#### Update chart

```jsx
useEffect(() => {
  drawChart(data);
}, [data]);
```

### Why is this useful?

Without update lifecycle:

- UI would not react to user input
- API calls would not refresh
- Charts/tables would show old data

### Interview explanation

> Update phase is used to synchronize the UI with changing data, such as search input, filters, selected items, or server responses.

---

## Unmount Phase (Component removed from screen)

### Code

```jsx
useEffect(() => {
  return () => console.log('cleanup');
}, []);
```

### What is the returned function?

The function returned from `useEffect` is called a **cleanup function**.

React runs it when:

- component is removed
- effect re-runs before next execution

### Real UI examples

#### Clear timer

```jsx
useEffect(() => {
  const timer = setInterval(() => console.log('tick'), 1000);

  return () => clearInterval(timer);
}, []);
```

#### Remove event listener

```jsx
useEffect(() => {
  window.addEventListener('resize', handleResize);

  return () => {
    window.removeEventListener('resize', handleResize);
  };
}, []);
```

#### Close WebSocket

```jsx
useEffect(() => {
  const socket = new WebSocket('ws://localhost:8000');

  return () => socket.close();
}, []);
```

### Why cleanup is important?

If you forget cleanup:

- memory leaks
- multiple timers running
- duplicate event listeners
- unnecessary API/socket activity

---

## Visual Flow

```text
User opens page
      |
      v
[ MOUNT ]
  fetch data
  start timer
  add listener
      |
      v
User interacts
      |
      v
[ UPDATE ]
  search API
  filter table
  update chart
      |
      v
User leaves page
      |
      v
[ UNMOUNT ]
  clear timer
  remove listener
  close socket
```

---

## How this helps in real React UI building

### Example: Dashboard Page

```jsx
function Dashboard() {
  const [users, setUsers] = useState([]);

  // MOUNT
  useEffect(() => {
    fetch('/api/users')
      .then(res => res.json())
      .then(setUsers);
  }, []);

  // UNMOUNT
  useEffect(() => {
    const interval = setInterval(() => {
      console.log('refresh heartbeat');
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      {users.map(u => (
        <p key={u.id}>{u.name}</p>
      ))}
    </div>
  );
}
```

### What happens?

#### When page opens (Mount)

- API request sent
- Users loaded
- Timer started

#### When state changes (Update)

- Component re-renders
- UI shows latest users

#### When user navigates away (Unmount)

- Timer is cleared
- No background work remains

---

## Mapping to old class component lifecycle

| Class Component | Functional Component |
|---|---|
| `componentDidMount()` | `useEffect(..., [])` |
| `componentDidUpdate()` | `useEffect(..., [deps])` |
| `componentWillUnmount()` | `return cleanup` inside `useEffect` |

### Old class version

```jsx
componentDidMount() {
  fetchData();
}

componentWillUnmount() {
  clearInterval(this.timer);
}
```

### Modern hook version

```jsx
useEffect(() => {
  fetchData();

  return () => clearInterval(timer);
}, []);
```

---

## Most Asked Interview Questions

### Q1. Why use `useEffect` instead of calling API directly in component body?

**Wrong**

```jsx
function App() {
  fetch('/api'); // runs on every render ❌
}
```

**Correct**

```jsx
useEffect(() => {
  fetch('/api'); // runs once or when deps change ✅
}, []);
```

### Q2. What happens if dependency array is omitted?

```jsx
useEffect(() => {
  console.log('runs every render');
});
```

- Runs after **every render**
- Can cause infinite loops if state is updated inside

---

### Q3. What happens if dependency array is empty?

```jsx
useEffect(() => {
  console.log('runs once');
}, []);
```

- Runs only after first render
- Similar to `componentDidMount`

---

### Q4. Why do we return a cleanup function?

To prevent **memory leaks** and remove subscriptions, timers, or listeners when the component is destroyed.

---

## One-line memory trick

```text
[]        -> Mount (once)
[dep]     -> Update (when dep changes)
return () -> Unmount (cleanup)
```

Remember:

- **Mount = start something**
- **Update = react to changes**
- **Unmount = stop/clean something**

### Interview tip
In React functional components, **useEffect replaces lifecycle methods** like `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount`.

---

# 5. State Management

## Props vs State

| Props | State |
|---|---|
| Read-only | Mutable |
| Passed from parent | Managed inside component |
| External data | Local data |

---

## Prop Drilling

Passing props through many intermediate components.

### Solution

- React Context
- Redux Toolkit
- Zustand

---

## React Context

### When to use?

- Theme
- Auth user
- Language
- Small global state

```jsx
const AuthContext = createContext();
```

### Limitation
Frequent updates can cause unnecessary re-renders.

---

# 6. Redux Toolkit (RTK) – Must Know

## Why Redux?

- Predictable global state
- Debugging with DevTools
- Shared data across unrelated components

---

## Why RTK?

- Less boilerplate
- Built-in Immer
- Recommended by Redux team

---

## Create slice

```jsx
import { createSlice } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: state => {
      state.value += 1;
    }
  }
});

export const { increment } = counterSlice.actions;
export default counterSlice.reducer;
```

---

## useSelector & useDispatch

```jsx
const count = useSelector(state => state.counter.value);
const dispatch = useDispatch();

dispatch(increment());
```

### Expected question
**When would you choose Context over Redux?**

- Context → small/simple state
- Redux → complex shared state with async flows

---

# 7. Custom Hooks

## Why?

Extract reusable logic.

---

## Example

```jsx
function useFetch(url) {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(url)
      .then(res => res.json())
      .then(setData);
  }, [url]);

  return data;
}
```

Usage:

```jsx
const users = useFetch('/api/users');
```

### Interview answer
Use custom hooks when **the same stateful logic is used in multiple components**.

---

# 8. Lazy Loading & Suspense (HOT)

## Why?

Reduce initial bundle size.

---

## Example

```jsx
const Dashboard = React.lazy(() => import('./Dashboard'));

<Suspense fallback={<div>Loading...</div>}>
  <Dashboard />
</Suspense>
```

---

## Code Splitting

- Route-based splitting
- Component-based splitting

### Benefits

- Faster first load
- Better Lighthouse score
- Improved user experience

### Very common question
**Difference between lazy loading and code splitting?**

- **Code splitting** = creating separate JS chunks
- **Lazy loading** = loading those chunks only when needed

---

# 9. Virtual DOM & Reconciliation (HOT)

## What is Virtual DOM?

A lightweight JavaScript representation of the real DOM.

---

## How React updates UI

1. State changes
2. New Virtual DOM is created
3. React compares old vs new (diffing)
4. Only changed nodes are updated in the real DOM

---

## Reconciliation

React’s algorithm for comparing trees efficiently.

### Key points

- Different element type → replace node
- Same type → update attributes
- Lists use **key** prop for efficient updates

---

## Why are keys important?

```jsx
{items.map(item => (
  <li key={item.id}>{item.name}</li>
))}
```

### Never use array index if list can reorder.

---

## React Fiber

- New reconciliation engine
- Enables incremental rendering
- Improves responsiveness
- Supports concurrent features

---

# 10. SSR vs CSR (Extremely Important)

| CSR | SSR |
|---|---|
| Rendered in browser | Rendered on server |
| Slower first load | Faster first load |
| Poorer SEO | Better SEO |
| More client work | More server work |

---

## When to use CSR?

- Admin dashboards
- Internal tools
- Authenticated applications

---

## When to use SSR?

- Public websites
- SEO-heavy pages
- E-commerce landing pages

---

## Hydration

Server sends HTML, then React attaches event handlers on the client.

### Common question
**What is hydration mismatch?**

When server-rendered HTML differs from client-rendered HTML.

---

# 11. React Router & Protected Routes

## Basic routing

```jsx
<Routes>
  <Route path='/' element={<Home />} />
  <Route path='/dashboard' element={<Dashboard />} />
</Routes>
```

---

## Protected route (RBAC)

```jsx
function ProtectedRoute({ children }) {
  const token = localStorage.getItem('token');

  return token ? children : <Navigate to='/login' />;
}
```

---

## Role-based access

```jsx
if (user.role !== 'admin') {
  return <Navigate to='/unauthorized' />;
}
```

### Explain RBAC clearly
**Role-Based Access Control** restricts routes and UI actions based on user roles (admin, manager, viewer).

---

# 12. Async API Calls

## Fetch with async/await

```jsx
const fetchUsers = async () => {
  try {
    const res = await fetch('/api/users');
    const data = await res.json();
    setUsers(data);
  } catch (err) {
    console.error(err);
  }
};
```

---

## Loading & Error state

```jsx
const [loading, setLoading] = useState(false);
const [error, setError] = useState(null);
```

### Interview question
**How do you cancel API requests?**

Using `AbortController`.

---

# 13. Performance Optimization

## React.memo

Prevents unnecessary re-render.

```jsx
export default React.memo(UserCard);
```

---

## useMemo

For expensive computations.

---

## useCallback

For stable function references.

---

## List virtualization

Use libraries such as:

- react-window
- react-virtualized

For rendering thousands of rows efficiently.

---

## Bundle optimization

- Lazy loading
- Tree shaking
- Image compression
- Dynamic imports

---

# 14. Reusability & Component Design

## Good reusable component

```jsx
function Button({ variant = 'primary', children, onClick }) {
  return (
    <button className={`btn btn-${variant}`} onClick={onClick}>
      {children}
    </button>
  );
}
```

### Mention

- Props-driven design
- Composition over inheritance
- Keep components small and focused

---

# 15. Testing Basics

## Tools

- Jest
- React Testing Library

---

## Simple test

```jsx
test('renders button text', () => {
  render(<Button>Save</Button>);
  expect(screen.getByText('Save')).toBeInTheDocument();
});
```

---

## What should you test?

- Rendering
- User interactions
- API success/error states
- Conditional rendering

### Interview answer
I focus on **user behavior testing** rather than testing internal implementation details.

---

# 16. Styling

## Tailwind CSS (Most useful)

### Pros

- Fast development
- Consistent design
- Small final CSS bundle

```jsx
<button className='bg-blue-500 text-white px-4 py-2 rounded'>
  Save
</button>
```

---

## CSS Modules

```jsx
import styles from './Button.module.css';

<button className={styles.btn}>Save</button>
```

---

## StyleX (Meta)

Know it is a **compile-time optimized styling solution**, but Tailwind is more commonly used in industry.

---

# 17. Higher Order Components (HOC)

## What is HOC?

A function that takes a component and returns an enhanced component.

```jsx
function withLoader(Component) {
  return function Wrapped(props) {
    if (props.loading) return <p>Loading...</p>;
    return <Component {...props} />;
  };
}
```

---

## When to use?

- Authentication
- Logging
- Permission checks
- Analytics

### Modern note
Hooks have replaced many HOC use cases.

---

# 18. Most Asked Rapid-Fire Questions

## Q1. Why is React fast?

- Virtual DOM
- Diffing algorithm
- Efficient DOM updates
- Fiber architecture

---

## Q2. Difference between controlled and uncontrolled components?

### Controlled

```jsx
<input value={name} onChange={e => setName(e.target.value)} />
```

### Uncontrolled

```jsx
<input ref={inputRef} />
```

---

## Q3. Why should hooks not be called conditionally?

React relies on **hook call order** being the same on every render.

---

## Q4. What causes unnecessary re-renders?

- Parent re-render
- New object/function references
- Context updates
- State updates

---

## Q5. What is lifting state up?

Move shared state to the nearest common parent.

---

# 19. Questions I Should Ask the Interviewer

- Which state management solution do you use (Context, Redux, Zustand)?
- Do you use SSR frameworks like Next.js?
- How is frontend testing handled?
- What is the deployment setup for frontend applications?
- How closely do frontend and backend teams collaborate?

---

# 20. 1-Day Revision Plan

## Morning (2 hrs)

- useState
- useEffect
- useRef
- Props vs State
- Controlled components

---

## Afternoon (2 hrs)

- Virtual DOM
- Reconciliation
- SSR vs CSR
- React Router
- Protected routes

---

## Evening (2 hrs)

- Redux Toolkit
- Lazy loading + Suspense
- Performance optimization
- Testing basics
- Mock interview questions

---

# 21. Final Focus Areas (Most Likely for My Profile)

## React (High probability)

- useEffect
- useState
- useRef
- Virtual DOM
- SSR vs CSR
- Lazy loading
- React Router
- Redux Toolkit

---

## FastAPI (Very high probability)

- Dependency Injection
- Pydantic models
- Async endpoints
- Background tasks
- JWT authentication
- Middleware
- Error handling
- WebSockets (basic)

---

## Cloud (High probability)

- Docker
- Kubernetes basics
- AWS/GCP services
- CI/CD
- Environment variables
- Logging & monitoring

---

# 22. Honest Experience Boundary

## Say confidently

- Built React forms and dashboards
- Integrated REST APIs
- Used hooks and routing
- Added lazy loading
- Used Tailwind CSS
- Worked with Redux Toolkit in smaller modules

---

## Avoid claiming unless deeply experienced

- Advanced Next.js SSR
- Micro-frontends
- Complex Redux middleware
- React internals beyond high-level Fiber understanding
- Large-scale frontend architecture ownership

---

# 23. 10 Questions I Must Be Able to Answer Without Hesitation

<List><List.Item>What is the difference between state and props?</List.Item><List.Item>How does useEffect work?</List.Item><List.Item>What is the Virtual DOM?</List.Item><List.Item>How does React perform reconciliation?</List.Item><List.Item>Difference between useMemo and useCallback?</List.Item><List.Item>What is lazy loading and why use Suspense?</List.Item><List.Item>Difference between SSR and CSR?</List.Item><List.Item>Why use Redux Toolkit?</List.Item><List.Item>How do you protect routes in React?</List.Item><List.Item>How do you optimize a slow React application?</List.Item></List>

---

# Final Tip

For **Safran Digit**, your strongest combination is:

```text
Backend expertise (Python + FastAPI)
+ Practical React knowledge
+ Understanding of API integration
+ Cloud/Docker/Kubernetes basics
```

Do not try to sound like a senior frontend engineer. Position yourself as a **backend engineer who can independently build and maintain React-based UIs and collaborate effectively across the stack**. That is a very credible and attractive profile for many product teams.