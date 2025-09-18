# V1

## Context

Types:

```python
from alchemyst_ai.types.v1 import ContextSearchResponse
```

Methods:

- <code title="post /api/v1/context/delete">client.v1.context.<a href="./src/alchemyst_ai/resources/v1/context/context.py">delete</a>(\*\*<a href="src/alchemyst_ai/types/v1/context_delete_params.py">params</a>) -> object</code>
- <code title="post /api/v1/context/add">client.v1.context.<a href="./src/alchemyst_ai/resources/v1/context/context.py">add</a>(\*\*<a href="src/alchemyst_ai/types/v1/context_add_params.py">params</a>) -> object</code>
- <code title="post /api/v1/context/search">client.v1.context.<a href="./src/alchemyst_ai/resources/v1/context/context.py">search</a>(\*\*<a href="src/alchemyst_ai/types/v1/context_search_params.py">params</a>) -> <a href="./src/alchemyst_ai/types/v1/context_search_response.py">ContextSearchResponse</a></code>

### Traces

Types:

```python
from alchemyst_ai.types.v1.context import TraceListResponse, TraceDeleteResponse
```

Methods:

- <code title="get /api/v1/context/traces">client.v1.context.traces.<a href="./src/alchemyst_ai/resources/v1/context/traces.py">list</a>() -> <a href="./src/alchemyst_ai/types/v1/context/trace_list_response.py">TraceListResponse</a></code>
- <code title="delete /api/v1/context/traces/{traceId}/delete">client.v1.context.traces.<a href="./src/alchemyst_ai/resources/v1/context/traces.py">delete</a>(trace_id) -> <a href="./src/alchemyst_ai/types/v1/context/trace_delete_response.py">TraceDeleteResponse</a></code>

### View

Types:

```python
from alchemyst_ai.types.v1.context import ViewRetrieveResponse
```

Methods:

- <code title="get /api/v1/context/view">client.v1.context.view.<a href="./src/alchemyst_ai/resources/v1/context/view.py">retrieve</a>() -> <a href="./src/alchemyst_ai/types/v1/context/view_retrieve_response.py">ViewRetrieveResponse</a></code>
- <code title="get /api/v1/context/view/docs">client.v1.context.view.<a href="./src/alchemyst_ai/resources/v1/context/view.py">docs</a>() -> object</code>

## Org

### Context

Types:

```python
from alchemyst_ai.types.v1.org import ContextViewResponse
```

Methods:

- <code title="post /api/v1/org/context/view">client.v1.org.context.<a href="./src/alchemyst_ai/resources/v1/org/context.py">view</a>(\*\*<a href="src/alchemyst_ai/types/v1/org/context_view_params.py">params</a>) -> <a href="./src/alchemyst_ai/types/v1/org/context_view_response.py">ContextViewResponse</a></code>
