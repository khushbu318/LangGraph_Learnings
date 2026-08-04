# Agentic AI

## What is Agentic AI?

Agentic AI is a type of AI that can take up a task or goal from a user and work toward completing it on its own with minimal human guidance.

It can:
- Plan its actions
- Take action independently
- Adapt to changing conditions
- Seek human assistance only when necessary

---

# Characteristics of Agentic AI

1. Autonomy
2. Goal-Oriented
3. Planning
4. Reasoning
5. Adaptability
6. Context Awareness

---

# 1. Autonomy

**Definition**

Autonomy refers to an AI system's ability to make decisions and take actions on its own to achieve a given goal without requiring step-by-step human instructions.

## Facets of Autonomy

- Execution
- Decision Making
- Tool Usage

## Controlling Autonomy

Since autonomous systems can be risky, they need appropriate controls.

Common control mechanisms include:

- Permission Scope
- Human in the Loop (HITL)
- Override Controls
- Guardrails / Policies

---

# 2. Goal-Oriented

**Definition**

Being goal-oriented means that the AI system operates with a persistent objective in mind and continuously directs its actions toward achieving that objective rather than simply responding to isolated prompts.

## Key Points

- Goals act as a compass for autonomy.
- Goals may come with constraints.
- Goals are stored in the agent's core memory.
- Goals can be modified when required.

---

# 3. Planning

**Definition**

Planning is the agent's ability to break down a high-level goal into a structured sequence of actions or sub-goals and determine the best path to achieve the desired outcome.

## Planning Process

### Step 1: Generate Multiple Candidate Plans

Create several possible approaches for solving the problem.

### Step 2: Evaluate Each Plan

Each plan is evaluated based on factors such as:

- Efficiency
- Tool availability
- Cost
- Risk
- Alignment with the goal

### Step 3: Select the Best Plan

The final plan may be selected using:

- Human in the Loop (HITL)
- A pre-programmed policy

---

# 4. Reasoning

**Definition**

Reasoning is the cognitive process through which an Agentic AI system interprets information, draws conclusions, and makes decisions both while planning ahead and while executing actions in real time.

## Reasoning During Planning

- Goal Decomposition
- Tool Selection
- Resource Estimation

## Reasoning During Execution

- Decision Making
- HITL Handling
- Error Handling

---

# 5. Adaptability

**Definition**

Adaptability is the agent's ability to modify its plans, strategies, or actions in response to unexpected conditions while remaining aligned with the original goal.

## Conditions That Trigger Adaptation

- Failures
- External Feedback
- Changing Goals

---

# 6. Context Awareness

**Definition**

Context awareness is the agent's ability to understand, retain, and utilize relevant information from the ongoing task, past interactions, user preferences, and environmental cues to make better decisions throughout a multi-step process.

## Types of Context

- Original Goal
- Progress So Far & Interaction History
- Environment State
- Tool Responses
- User-Specific Preferences
- Policies or Guardrails

## Memory in Context Awareness

Context awareness is implemented using memory systems.

### Short-Term Memory

Stores information relevant to the current task or conversation.

### Long-Term Memory

Stores persistent knowledge such as user preferences, previous interactions, and learned information that can be reused across future tasks.

---
# Components 

### 1. Brain
- Generally its a LLM 
- Goal Interpretation
- Planning
- Reasoning
- Tool Selection
- Communication 

### 2. Orchestrator (Like a project manager of agentic ai system)
- Task Sequencing
- Conditional Routing
- Retry Logic
- Looping and Iteration
- Delegation

### 3. Tools
- External Actions
- Knowledge Base Access

### 4. Memory
- Short-Term Memory
- Long-Term Memory
- State Tracking

### 5. Supervisor
- Approval Requests (HITL)
- Guardrails Enforcement
- Edge Case Escalation 

---
# LangChain Recap

## What is LangChain?

LangChain is an open-source framework designed to simplify the development of applications powered by Large Language Models (LLMs).

It provides modular building blocks that enable developers to create sophisticated LLM-based workflows with ease.

## Core Components of LangChain

1. **Models**
   - Provides a unified interface to interact with different LLM providers.

2. **Prompts**
   - Helps design, manage, and reuse prompts effectively.

3. **Retrievers**
   - Fetches relevant documents from a vector store for Retrieval-Augmented Generation (RAG).

4. **Chains** ⭐
   - LangChain's biggest offering.
   - Allows multiple components to be connected together into a sequential workflow.

---

# What Can You Build with LangChain?

- Simple conversational applications (Chatbots)
- Text summarizers
- Multi-step workflows
- Retrieval-Augmented Generation (RAG) applications
- Basic-level AI agents

---

# Building Effective Agents

> **Reference:**  
> [Anthropic - Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)

## Workflow vs Agent

### Workflow

A **workflow** is a system where LLMs and tools are orchestrated through **predefined code paths**.

Characteristics:
- Fixed execution flow
- Predictable behavior
- Logic is explicitly defined by the developer

---

### Agent

An **agent** is a system where the LLM dynamically decides:
- What actions to perform
- Which tools to use
- In what order to execute them

The LLM maintains control over how the task is accomplished instead of following a fixed sequence.

---

# Challenges of Building Complex Workflows in LangChain

Consider a workflow such as:

> **Collect user requirements → Screen candidates → Conduct interviews → Hire the selected candidate**

Such workflows are difficult to implement using only LangChain because they involve branching, looping, retries, state management, and human intervention.

## Challenges

### 1. Conditional Branching

LangChain works best with **linear workflows**.

Handling multiple execution paths requires additional custom logic (Glue Code).

---

### 2. Loops

Implementing iterative workflows (retry until success, repeated evaluations, etc.) requires manual coding.

---

### 3. Jumps

Moving execution directly from one step to another (non-linear execution) is not naturally supported.

---

### 4. State Handling

LangChain does not provide a built-in mechanism for maintaining workflow state.

You need to write custom Python code to:

- Store state
- Update state
- Pass state between different chain executions

---

### 5. Glue Code

As workflows become more complex, developers end up writing a large amount of **glue code** to connect different components.

This makes the codebase:
- Harder to understand
- Harder to maintain
- More difficult to debug

---

### 6. Event-Driven Execution

LangChain does not natively support event-driven workflows where execution is triggered by external events.

---

### 7. Fault Tolerance

LangChain provides very limited built-in fault tolerance.

In contrast, **LangGraph** supports:
- Automatic retries for recoverable failures
- Recovery mechanisms for larger workflow failures

---

### 8. Human in the Loop (HITL)

Human approval or intervention is not a built-in feature in LangChain and must be implemented manually.

---

### 9. Nested Workflows

LangChain does not support nested workflows.

**LangGraph** introduces **Subgraphs**, which allow:

- Reusable workflows
- Multi-agent architectures
- Better modularity

---

### 10. Observability

LangChain can be monitored using **LangSmith**, but it only tracks LangChain components.

It **cannot observe** the custom glue code written by developers, resulting in only **partial observability**.

**LangGraph**, on the other hand, provides **full observability** by tracking:

- Every node
- Every edge
- State transitions
- Execution flow

---

# Why **LangGraph**?

**LangGraph** addresses many of **LangChain's** limitations by providing built-in support for:

- **Native State Management**
- **Conditional Branching**
- **Loops**
- **Non-linear Execution**
- **Event-driven Workflows**
- **Fault Tolerance**
- **Human in the Loop (HITL)**
- **Nested Workflows** using **Subgraphs**
- **Full Observability**
- Better support for **Complex** and **Multi-Agent Systems**

---

# What is **LangGraph**?

**LangGraph** is an **orchestration framework** that enables you to build **stateful**, **multi-step**, and **event-driven workflows** using **Large Language Models (LLMs)**.

It is ideal for designing both:

- **Single-Agent** applications
- **Multi-Agent** Agentic AI applications

## Think of LangGraph as a **Flowchart Engine for LLMs**

You define:

- **Nodes** → The individual steps or tasks.
- **Edges** → How those steps are connected.
- **Transition Logic** → Rules that determine which step executes next.

LangGraph takes care of many workflow concerns automatically, including:

- **State Management**
- **Conditional Branching**
- **Looping**
- **Pausing & Resuming Execution**
- **Fault Recovery**

These capabilities make it suitable for building **robust**, **production-grade AI systems**.

---

# When Should You Use **LangChain** vs **LangGraph**?

## Use **LangChain** when:

Your application consists of **simple, linear workflows**, such as:

- Prompt Chains
- Chatbots
- Text Summarizers
- Basic Retrieval Systems (RAG)

These workflows generally follow a fixed sequence of steps without complex control flow.

---

## Use **LangGraph** when:

Your application requires **complex, non-linear workflows** involving one or more of the following:

- **Conditional Paths**
- **Loops**
- **Human in the Loop (HITL)**
- **Multi-Agent Coordination**
- **Asynchronous Execution**
- **Event-driven Execution**
- **State Persistence**
- **Fault Recovery**

LangGraph is designed specifically to orchestrate these advanced workflow patterns.

---

# Should We Still Use **LangChain**?

**Yes.**

**LangGraph is built on top of LangChain—it does not replace it.**

LangChain continues to provide the core building blocks used inside each workflow node, including:

- **ChatOpenAI** (LLMs)
- **PromptTemplate**
- **Retrievers**
- **Document Loaders**
- **Tools**
- And many other integrations

**LangGraph** focuses on **workflow orchestration**, while **LangChain** provides the components required to perform the actual work at each step.

> **In simple terms:**
>
> - **LangChain = Building Blocks**
> - **LangGraph = Workflow Engine**
>
> They are designed to work **together**, not compete with each other.

# LLM Workflows

## What are LLM Workflows?

LLM workflows are step-by-step execution patterns used to build complex LLM-powered applications. Instead of relying on a single prompt, the task is broken into multiple stages, where each stage performs a specific responsibility.

Each step in a workflow can perform one of the following tasks:

- Prompting
- Reasoning
- Tool calling
- Memory access
- Decision making
- Output validation

LLM workflows can be:

- **Linear** – Execute tasks sequentially.
- **Parallel** – Execute multiple independent tasks simultaneously.
- **Branched (Routing)** – Choose different execution paths based on the input.
- **Looped (Iterative)** – Repeat steps until a desired result is achieved.

These workflow patterns enable advanced capabilities such as:

- Retry mechanisms
- Multi-agent communication
- Tool-augmented reasoning
- Self-evaluation and refinement
- Dynamic task planning

---

# Common LLM Workflow Patterns

## 1. Prompt Chaining

Prompt chaining is the simplest workflow pattern where the output of one prompt becomes the input for the next prompt. Each step performs a well-defined task, making complex problems easier to solve.

### Example

Suppose you want to generate a technical blog.

1. Generate an outline.
2. Expand the outline into sections.
3. Proofread the content.
4. Optimize it for SEO.
5. Produce the final blog.

Each prompt depends on the output of the previous prompt.

![Prompt Chaining](images_md/Prompt_Chaining.png)

---

## 2. Routing

Routing is used when different inputs require different processing paths. A router (usually another LLM or a classifier) decides which workflow should handle the request.

### Example

A customer support chatbot receives different types of queries.

- Billing issues → Billing workflow
- Technical problems → Technical support workflow
- Refund requests → Refund workflow
- Product information → Sales workflow

Instead of sending every request through the same process, the router selects the most appropriate workflow.

![Routing](images_md/Routing.png)

---

## 3. Parallelization

Parallelization is used when multiple independent subtasks can be executed simultaneously. Since the subtasks do not depend on one another, they can run in parallel, reducing overall execution time.

### Example: YouTube Content Moderation

When a user uploads a video, several moderation checks can run at the same time:

- Check whether the content follows community guidelines.
- Detect misleading or false information.
- Detect sexual or explicit content.
- Detect hate speech or abusive language.
- Detect violence or graphic content.

Since these checks are independent, they are executed in parallel, and their results are combined to make the final moderation decision.

> **Note:** Parallelization works best when the subtasks are **static** and known in advance.

![Parallelization](images_md/Parallelization.png)

---

## 4. Orchestrator-Workers

In this workflow, an **Orchestrator** first analyzes the user's request and dynamically decides:

- Which workers should be used.
- What tasks each worker should perform.
- How the final result should be combined.

Unlike parallelization, the subtasks are **not predefined**. They are generated dynamically based on the user's request.

### Example

A user asks:

> "Create a report on Artificial Intelligence in Healthcare."

The orchestrator may decide to:

- Worker 1 → Search for the latest research papers.
- Worker 2 → Collect recent news related to AI in healthcare.
- Worker 3 → Gather market statistics.
- Worker 4 → Generate charts and summarize findings.

If the topic is related to recent events, the orchestrator can instruct one of the workers to retrieve information from news sources. For another topic, it may choose an entirely different set of workers.

This makes the workflow flexible and adaptive.

![Orchestrator Workers](images_md/Orchestrator.png)

---

## 5. Evaluator-Optimizer

The Evaluator-Optimizer workflow is an iterative process where one model generates an output, and another model (or the same model) evaluates it against predefined criteria. If the output is not satisfactory, feedback is provided, and the content is regenerated.

This loop continues until the output meets the required quality.

### Example: Blog Generation

Generating a high-quality blog usually requires multiple iterations.

1. Generate the first draft.
2. Evaluate the draft for grammar, clarity, and structure.
3. Provide feedback.
4. Rewrite the blog based on the feedback.
5. Repeat until the blog satisfies all quality requirements.

This workflow is particularly useful for:

- Blog writing
- Code generation
- Report writing
- Creative writing
- Documentation generation

![Prompt Chaining](images_md/Evaluator_Optimizer.png)

---

# LangGraph Fundamentals

## Graphs, Nodes, and Edges

Let's understand the core concepts of **LangGraph** using a UPSC essay evaluation workflow.

### Example Problem

The system generates an essay topic, collects the student's submission, and evaluates it in parallel on **depth of analysis**, **language quality**, and **clarity of thought**. Based on the combined score, it either provides feedback for improvement or approves the essay.

## Workflow

### 1. Generate Topic
- The system generates a relevant **UPSC-style essay topic**.
- The topic is presented to the student.

### 2. CollectEssay
- The student writes the essay.
- The essay is submitted to the system.

### 3. EvaluateEssay (Parallel Evaluation Block)

The essay is evaluated by **three independent tasks running in parallel**.

#### EvaluateDepth
Analyzes:
- Depth of analysis
- Strength of arguments
- Critical thinking

#### EvaluateLanguage
Evaluates:
- Grammar
- Vocabulary
- Fluency
- Tone

#### EvaluateClarity
Assesses:
- Coherence
- Logical flow
- Clarity of thought

### 4. AggregateResults
- Combines the three evaluation scores.
- Generates a total score (e.g., **out of 15**).

### 5. Conditional Routing

Based on the total score:

- **If the score meets the threshold**
  - → Go to **ShowSuccess**

- **If the score is below the threshold**
  - → Go to **GiveFeedback**

### 6. GiveFeedback
- Provides targeted suggestions for improvement.
- Highlights weak areas based on the evaluation.

### 7. CollectRevision (Optional Loop)
- The student revises the essay.
- The revised essay is submitted again.
- The workflow loops back to **EvaluateEssay** for re-evaluation.

### 8. ShowSuccess
- Congratulates the student.
- Ends the workflow.

---

![UPSC Essay Problem](images_md/upsc_essay_problem.png)

---

# LangGraph Concepts

A **LangGraph** workflow is represented as a **graph** consisting of:

- **Nodes**
- **Edges**
- **State**

---

## Nodes

A **node** is simply a **Python function**.

Each node performs a specific task, such as:

- Generating a topic
- Collecting an essay
- Evaluating language
- Aggregating scores
- Giving feedback

A node:

- Reads data from the shared state.
- Performs some computation.
- Returns updates to the state.

Example nodes from the essay workflow:

- `GenerateTopic`
- `CollectEssay`
- `EvaluateDepth`
- `EvaluateLanguage`
- `EvaluateClarity`
- `AggregateResults`
- `GiveFeedback`
- `ShowSuccess`

---

## Edges

**Edges define how nodes are executed.**

They determine the flow of execution between nodes.

LangGraph supports multiple types of edges.

### Sequential Edge

Runs one node after another.

```text
GenerateTopic
      ↓
CollectEssay
```

### Parallel Edge

Runs multiple nodes simultaneously.

```text
              EvaluateDepth
            /
CollectEssay
            \
              EvaluateLanguage
            \
              EvaluateClarity
```

Parallel execution improves performance because independent tasks do not wait for one another.

### Conditional Edge

Routes execution based on some condition.

```text
Total Score >= Threshold
        ↓
   ShowSuccess

Total Score < Threshold
        ↓
  GiveFeedback
```

### Loop Edge

Allows the workflow to repeat until a condition is satisfied.

```text
GiveFeedback
      ↓
CollectRevision
      ↓
EvaluateEssay
      ↓
AggregateResults
```

This continues until the essay reaches the required score.

---

# State

State is one of the most important concepts in LangGraph.

## What is State?

**State is the shared memory that flows through your workflow.**

It stores all the information required by different nodes as the graph executes.

Instead of passing variables manually between functions, every node reads from and writes to the shared state.

As the workflow progresses, the state gets updated.

---

## Example

In the UPSC essay workflow, the state may store:

- Essay topic
- Essay text
- Individual evaluation scores
- Total score
- Feedback
- Number of evaluation attempts

Every node can access and modify this shared state.

---

## Example State

```python
from typing import Annotated
from operator import add
from typing_extensions import TypedDict

class EssayState(TypedDict):
    topic: str
    essay_text: str

    depth_score: int
    language_score: int
    clarity_score: int

    total_score: int

    feedback: Annotated[list[str], add]

    evaluation_round: int
```

---

## Why State is Useful

Instead of writing:

```python
evaluate(essay, topic, score, feedback, ...)
```

every node simply receives:

```python
state
```

and returns only the fields it wants to update.

This makes workflows:

- Cleaner
- Easier to maintain
- Easier to extend
- Suitable for complex AI pipelines

---

# Reducers

Reducers define **how updates from nodes are applied to the shared state.**

When multiple nodes update the same state key, LangGraph uses a reducer to decide how those updates should be combined.

Reducers are especially important in **parallel workflows**.

---

## Why Reducers are Needed

Suppose three parallel nodes produce feedback.

Without reducers:

```text
Node A → ["Good introduction"]

Node B → ["Grammar mistakes"]

Node C → ["Improve conclusion"]
```

Only one update might survive.

With a reducer:

```text
[
    "Good introduction",
    "Grammar mistakes",
    "Improve conclusion"
]
```

All updates are merged correctly.

---

## Reducer Behavior

Each state key can define its own reducer.

Some common behaviors are:

### Replace (Default)

The new value replaces the existing value.

```python
score: int
```

---

### Append / Add

The new values are appended to the existing collection.

```python
feedback: Annotated[list[str], add]
```

Here, `add` tells LangGraph to append new feedback items instead of replacing the existing list.

---

### Custom Reducer

You can also define your own reducer function if you want custom merge logic.

---

# Supersteps in LangGraph

LangGraph executes workflows using the concept of **Supersteps**, inspired by **Google's Pregel** graph-processing model.

A **Superstep** is a synchronization phase where:

1. All eligible nodes execute simultaneously.
2. Each node reads the current state.
3. Each node produces state updates.
4. LangGraph merges the updates using reducers.
5. The updated state becomes available to the next Superstep.

Example:

```text
Superstep 1
------------
GenerateTopic

Superstep 2
------------
CollectEssay

Superstep 3
------------
EvaluateDepth
EvaluateLanguage
EvaluateClarity
(Parallel)

Superstep 4
------------
AggregateResults

Superstep 5
------------
Conditional Routing
```

Parallel nodes in the same Superstep **cannot see each other's updates** until the Superstep finishes.

This synchronization ensures deterministic execution of the graph.

---

# Summary

- A **Graph** represents the entire workflow.
- **Nodes** are Python functions that perform specific tasks.
- **Edges** define the execution flow:
  - Sequential
  - Parallel
  - Conditional
  - Loop
- **State** is the shared memory passed between all nodes.
- **Reducers** determine how multiple state updates are merged.
- **Supersteps** allow LangGraph to execute parallel nodes efficiently while synchronizing state updates between execution phases.

# Persistence in LangGraph

## What is Persistence?

**Persistence** in LangGraph is the ability to **save the state of a workflow and restore it later**.

This means a graph can:

- pause execution,
- resume from the same point,
- survive application restarts,
- keep conversation or workflow history,
- support long-running and multi-user applications.

In simple words:

> Persistence = "Remember the workflow state so it can continue later."

---

## Where is the state stored?

During development, state can be stored **in memory (RAM)**.

For production, it is usually stored in a **database** such as:

- SQLite
- PostgreSQL
- Redis
- MongoDB (custom implementation)

| Environment | Storage |
|---|---|
| **Development** | RAM / `MemorySaver` |
| **Production** | SQLite / PostgreSQL / Redis / other persistent DBs |
---

## What gets saved?

LangGraph stores the **state after every super-step**.

A **super-step** is a round of execution in which **all active nodes finish running** before the next round begins.

For example, suppose the graph state is:

```python
from typing import TypedDict, Annotated
from operator import add

class State(TypedDict):
    numbers: Annotated[list[int], add]
```

As the graph runs, the state may evolve like this:

| Checkpoint | State |
|---|---|
| **CP1** | `[1]` |
| **CP2** | `[1, 2]` |
| **CP3** | `[1, 2, 3, 4, 5]` |

Here, **CP1, CP2, and CP3 are checkpoints automatically created by the checkpointer** after each super-step.

---

# Checkpointers in Persistence

## What is a Checkpointer?

A **checkpointer** is the component responsible for **saving and loading graph state**.

It acts like an auto-save system in a video game.

<Highlight value="Without a checkpointer, the graph forgets everything after execution ends."/>

---

## How it works

<CodeBlock language="text" content="Node execution
      ↓
State updated
      ↓
Checkpointer saves snapshot
      ↓
Next node runs"/>

After every **super-step**, LangGraph asks the checkpointer to store a snapshot of the current state.

---

## Simple Example (Memory Persistence)

```python
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph

# Create a checkpointer
checkpointer = MemorySaver()

# Compile graph with persistence enabled
graph = builder.compile(checkpointer=checkpointer)
```

`MemorySaver` stores checkpoints in **RAM**, so the state is available while the application is running.

---

## Resume Example

```python
config = {"configurable": {"thread_id": "user-1"}}

# First run
graph.invoke(
    {"numbers": [1]},
    config=config
)

# Resume later with the same thread_id
graph.invoke(
    {"numbers": [2]},
    config=config
)
```

### What happens?

- First run saves: `[1]`
- Second run loads the previous checkpoint and updates it to: `[1, 2]`

Because the **same `thread_id` (`user-1`)** is used, LangGraph restores the previous state automatically and continues the workflow instead of starting from scratch.

---

## Easy Analogy

Think of writing a document:

- You type a paragraph → **state changes**
- Auto-save runs → **checkpoint created**
- Laptop shuts down → **application stops**
- You reopen the document → **state restored from checkpoint**

LangGraph persistence works in the same way.


---

# Threads in Persistence

## Definition (Simple English)

A **thread** is a **unique ID that represents one conversation or one workflow session**.

All checkpoints belonging to the same thread are grouped together.

<Highlight value="Thread = the identity of a running workflow."/>

For example:

- `thread_id = "user-1"` → Alice's workflow
- `thread_id = "user-2"` → Bob's workflow

Their states are stored separately.

---

## Why are threads needed?

Without threads, all users would share the same saved state.

Threads provide **isolation** between workflow sessions.

<Box background="surface" border={{"size":1,"color":"default"}} radius="3xl" padding={4}><Row align="center" columnGap={3} wrap="wrap"><Badge label="Thread user-1" color="info"/><Text weight="semibold">numbers = [1, 2]</Text><Spacer/><Badge label="Stored separately" variant="outline"/></Row><Divider spacing={3}/><Row align="center" columnGap={3} wrap="wrap"><Badge label="Thread user-2" color="success"/><Text weight="semibold">numbers = [10, 20]</Text><Spacer/><Badge label="Stored separately" variant="outline"/></Row></Box>

---

# Example with Two Graph Sessions

## Graph setup

```python
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)
```

---

## Session 1 (User A)

```python
config_a = {"configurable": {"thread_id": "user-A"}}

graph.invoke(
    {"numbers": [1, 2]},
    config=config_a
)
```

Saved state for **user-A**:

```python
{"numbers": [1, 2]}
```

---

## Session 2 (User B)

```python
config_b = {"configurable": {"thread_id": "user-B"}}

graph.invoke(
    {"numbers": [10, 20]},
    config=config_b
)
```

Saved state for **user-B**:

```python
{"numbers": [10, 20]}
```

---

## Resume User A

```python
graph.invoke(
    {"numbers": [3]},
    config=config_a
)
```

Result:

```python
{"numbers": [1, 2, 3]}
```

LangGraph automatically loaded the previous checkpoint for **user-A** and appended `3`.

---

# Visual Flow

```text
Thread: user-A

Start
  │
  ├── CP1 → [1]
  ├── CP2 → [1, 2]
  └── CP3 → [1, 2, 3]


Thread: user-B

Start
  │
  ├── CP1 → [10]
  └── CP2 → [10, 20]
```

Each thread has **its own independent checkpoint history**.

---

# Key Points to Remember

- **Persistence** saves and restores workflow state.
- **Checkpointer** performs the actual save/load operations.
- State is saved after every **super-step**.
- **MemorySaver** stores state in RAM (temporary).
- Production systems should use a **persistent database**.
- **Threads** separate workflow sessions using a unique `thread_id`.
- Using the same `thread_id` allows the graph to **resume from the last checkpoint**.

---

# One-Line Revision

> **Persistence remembers the graph state, the checkpointer stores it, and the `thread_id` tells LangGraph which saved workflow to continue.**

---

Yesterday 11:10 PM
Format the structure  and also compel the incomple info about the persistence in langgraph and add the exaple to make the undersant simple and give me the md code only

---
What is persistence

- Persistence is LangGraph refers to the ability to save and restore the state of a workflow over time.

- can be save in Ram and in database in production

- store value at each iteration

- Example: 

-- Checkpointers in Persistence

- with help of checkpointers we get persistence in langGraph

- we save the checkpointeres at each super step

- Ex:
at first the state is 
numbers: [list[int], add]

- at cp1 the numbers is 1
- at cp2 the numbers is [1,2]
- at cp3 the numbers is [1,2,3,4,5] (if the flow is paralled node working)

---- 
Threads in Persistence

- defination (simplest and in english)

- Example with 2 graphs example 


# Persistence in LangGraph

## What is Persistence?

**Persistence** in LangGraph is the ability to **save the state of a workflow and restore it later**.

This means a graph can:

- pause execution,
- resume from the same point,
- survive application restarts,
- keep conversation or workflow history,
- support long-running and multi-user applications.

In simple words:

> Persistence = "Remember the workflow state so it can continue later."

---

## Where is the state stored?

During development, state can be stored **in memory (RAM)**.

For production, it is usually stored in a **database** such as:

- SQLite
- PostgreSQL
- Redis
- MongoDB (custom implementation)

| **Environment** | **Storage** |
|-----------------|-------------|
| **Development** | RAM / MemorySaver |
| **Production** | SQLite / PostgreSQL / Redis / other persistent DBs |
---

## What gets saved?

LangGraph stores the **state after every super-step** (a step where all active nodes for that round finish execution).

For example, if the state is:

<CodeBlock language="python" content="from typing import Annotated
from operator import add

class State(TypedDict):
    numbers: Annotated[list[int], add]"/>

As the graph runs, the state may evolve like this:

<Table columnSizing="equal" rowDivider={{"size":1,"color":"default"}}><Table.Row header><Table.Cell>Checkpoint</Table.Cell><Table.Cell>State</Table.Cell></Table.Row><Table.Row><Table.Cell><Text inline weight="semibold">CP1</Text></Table.Cell><Table.Cell><Code value="[1]"/></Table.Cell></Table.Row><Table.Row><Table.Cell><Text inline weight="semibold">CP2</Text></Table.Cell><Table.Cell><Code value="[1, 2]"/></Table.Cell></Table.Row><Table.Row><Table.Cell><Text inline weight="semibold">CP3</Text></Table.Cell><Table.Cell><Code value="[1, 2, 3, 4, 5]"/></Table.Cell></Table.Row></Table>

Here, **CP1, CP2, and CP3 are checkpoints** automatically created by the checkpointer.

---

# Checkpointers in Persistence

## What is a Checkpointer?

A **checkpointer** is the component responsible for **saving and loading graph state**.

It acts like an auto-save system in a video game.

<Highlight value="Without a checkpointer, the graph forgets everything after execution ends."/>

---

## How it works

<CodeBlock language="text" content="Node execution
      ↓
State updated
      ↓
Checkpointer saves snapshot
      ↓
Next node runs"/>

After every **super-step**, LangGraph asks the checkpointer to store a snapshot of the current state.

---

## Simple Example (Memory Persistence)

<CodeBlock language="python" content="from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph

# Create a checkpointer
checkpointer = MemorySaver()

# Compile graph with persistence
graph = builder.compile(checkpointer=checkpointer)"/>

Now the graph can resume from previously saved checkpoints.

---

## Resume Example

<CodeBlock language="python" content="config = {"configurable": {"thread_id": "user-1"}}

# First run
graph.invoke({"numbers": [1]}, config=config)

# Later...
graph.invoke({"numbers": [2]}, config=config)"/>

Because the same **thread_id** is used, the graph loads the previous state and continues execution.

---

# Easy Analogy

Think of writing a document:

- You type a paragraph → **state changes**
- Auto-save runs → **checkpoint created**
- Laptop shuts down → application stops
- You reopen the document → **state restored from checkpoint**

LangGraph persistence works in the same way.

---

# Threads in Persistence

## Definition (Simple English)

A **thread** is a **unique ID that represents one conversation or one workflow session**.

All checkpoints belonging to the same thread are grouped together.

<Highlight value="Thread = the identity of a running workflow."/>

For example:

- `thread_id = "user-1"` → Alice's workflow
- `thread_id = "user-2"` → Bob's workflow

Their states are stored separately.

---

## Why are threads needed?

Without threads, all users would share the same saved state.

Threads provide **isolation** between workflow sessions.

> **Thread:** `user-1`  
> **State:** `numbers = [1, 2]`  
> *Stored separately*

---

> **Thread:** `user-2`  
> **State:** `numbers = [10, 20]`  
> *Stored separately*
---

# Example with Two Graph Sessions

## Graph setup

```python
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)
```

---
## Session 1 (User A)

```python
config_a = {"configurable": {"thread_id": "user-A"}}

graph.invoke(
    {"numbers": [1, 2]},
    config=config_a
)
```

Saved state for **user-A**:

```python
{"numbers": [1, 2]}
```

---

## Session 2 (User B)

```python
config_b = {"configurable": {"thread_id": "user-B"}}

graph.invoke(
    {"numbers": [10, 20]},
    config=config_b
)
```

Saved state for **user-B**:

```python
{"numbers": [10, 20]}
```

---

## Resume User A

```python
graph.invoke(
    {"numbers": [3]},
    config=config_a
)
```

Result:

```python
{"numbers": [1, 2, 3]}
```

LangGraph automatically loaded the previous checkpoint for **user-A** and appended `3`.

---

## Visual Flow

```text
Thread: user-A

Start
│
├── CP1 → [1]
├── CP2 → [1, 2]
└── CP3 → [1, 2, 3]
```
```text
Thread: user-B

Start
│
├── CP1 → [10]
└── CP2 → [10, 20]
```

Each thread has **its own independent checkpoint history**.

---

## Key Points to Remember

- Persistence saves and restores workflow state.
- A checkpointer performs the actual save/load operations.
- State is saved after every super-step.
- `MemorySaver` stores state in RAM (temporary).
- Production systems should use a persistent database.
- Threads separate workflow sessions using a unique `thread_id`.
- Using the same `thread_id` allows the graph to resume from the last checkpoint.

---

## One-Line Revision

**Persistence lets LangGraph save workflow state after every super-step and later resume execution from the last checkpoint using the same `thread_id`.**

## Where is the state stored?

During development, state can be stored **in memory (RAM)**.

For production, it is usually stored in a **database** such as:

- SQLite
- PostgreSQL
- Redis
- MongoDB (custom implementation)

| Environment | Storage |
|---|---|
| **Development** | RAM / `MemorySaver` |
| **Production** | SQLite / PostgreSQL / Redis / other persistent DBs |

---

## Easy Analogy

Think of writing a document:

- You type a paragraph → **state changes**
- Auto-save runs → **checkpoint created**
- Laptop shuts down → **application stops**
- You reopen the document → **state restored from checkpoint**

LangGraph persistence works in the same way.

---

## Why are threads needed?

Without threads, all users would share the same saved state.

Threads provide **isolation** between workflow sessions.

### Thread `user-1`

- `numbers = [1, 2]`

### Thread `user-2`

- `numbers = [10, 20]`

Both states are stored **separately**.

---

# Example with Two Graph Sessions

## Graph setup

```python
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)
```

---

## Session 1 (User A)

```python
config_a = {"configurable": {"thread_id": "user-A"}}

graph.invoke(
    {"numbers": [1, 2]},
    config=config_a
)
```

Saved state for **user-A**:

```python
{"numbers": [1, 2]}
```

---

## Session 2 (User B)

```python
config_b = {"configurable": {"thread_id": "user-B"}}

graph.invoke(
    {"numbers": [10, 20]},
    config=config_b
)
```

Saved state for **user-B**:

```python
{"numbers": [10, 20]}
```

---

## Resume User A

```python
graph.invoke(
    {"numbers": [3]},
    config=config_a
)
```

Result:

```python
{"numbers": [1, 2, 3]}
```

LangGraph automatically loaded the previous checkpoint for **user-A** and appended `3`.

---

# Visual Flow

```text
Thread: user-A

Start
  │
  ├── CP1 → [1]
  ├── CP2 → [1, 2]
  └── CP3 → [1, 2, 3]


Thread: user-B

Start
  │
  ├── CP1 → [10]
  └── CP2 → [10, 20]
```

Each thread has **its own independent checkpoint history**.

---

# Key Points to Remember

- **Persistence** saves and restores workflow state.
- **Checkpointer** performs the actual save/load operations.
- State is saved after every **super-step**.
- **MemorySaver** stores state in RAM (temporary).
- Production systems should use a **persistent database**.
- **Threads** separate workflow sessions using a unique `thread_id`.
- Using the same `thread_id` allows the graph to **resume from the last checkpoint**.

---

# One-Line Revision

> **Persistence remembers the graph state, the checkpointer stores it, and the `thread_id` tells LangGraph which saved workflow to continue.**
What gets saved?
LangGraph stores the state after every super-step (a step where all active nodes for that round finish execution).

For example, if the state is:

<CodeBlock language="python" content="from typing import Annotated from operator import add

class State(TypedDict): numbers: Annotated[list[int], add]"/>

Resume Example
<CodeBlock language="python" content="config = {"configurable": {"thread_id": "user-1"}}

 

As the graph runs, the state may evolve like this:

CheckpointStateCP1CP2CP3
Here, CP1, CP2, and CP3 are checkpoints automatically created by the checkpointer.
imple Example (Memory Persistence)
<CodeBlock language="python" content="from langgraph.checkpoint.memory import MemorySaver from langgraph.graph import StateGraph


## What gets saved?

LangGraph stores the **state after every super-step**.

A **super-step** is a round of execution in which **all active nodes finish running** before the next round begins.

For example, suppose the graph state is:

```python
from typing import TypedDict, Annotated
from operator import add

class State(TypedDict):
    numbers: Annotated[list[int], add]
```

As the graph runs, the state may evolve like this:

| Checkpoint | State |
|---|---|
| **CP1** | `[1]` |
| **CP2** | `[1, 2]` |
| **CP3** | `[1, 2, 3, 4, 5]` |

Here, **CP1, CP2, and CP3 are checkpoints automatically created by the checkpointer** after each super-step.

---

## Simple Example (Memory Persistence)

```python
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph

# Create a checkpointer
checkpointer = MemorySaver()

# Compile graph with persistence enabled
graph = builder.compile(checkpointer=checkpointer)
```

`MemorySaver` stores checkpoints in **RAM**, so the state is available while the application is running.

---

## Resume Example

```python
config = {"configurable": {"thread_id": "user-1"}}

# First run
graph.invoke(
    {"numbers": [1]},
    config=config
)

# Resume later with the same thread_id
graph.invoke(
    {"numbers": [2]},
    config=config
)
```

### What happens?

- First run saves: `[1]`
- Second run loads the previous checkpoint and updates it to: `[1, 2]`

Because the **same `thread_id` (`user-1`)** is used, LangGraph restores the previous state automatically and continues the workflow instead of starting from scratch.
# Benefits of Persistence
- Short Term Memory
- Fault Tolerance
- HITL
- Time Travel

upate this with the simple examples too in langgraph how it works
# Benefits of Persistence in LangGraph

Persistence is not just for saving state — it enables several powerful features that are used in real-world AI applications.

---

# 1. Short-Term Memory

## What is it?

The graph can **remember information from previous interactions** in the same thread.

This is useful for:

- chatbots,
- assistants,
- form-filling workflows,
- multi-step reasoning.

---

## Example

```python
from typing import TypedDict
from langgraph.checkpoint.memory import MemorySaver

class State(TypedDict):
    name: str

checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "user-1"}}

# First interaction
graph.invoke({"name": "Rahul"}, config=config)

# Second interaction
result = graph.invoke({}, config=config)

print(result["name"])
```

Output:

```python
Rahul
```

### How it works

- First call saves `name = "Rahul"`.
- Second call uses the same `thread_id`.
- LangGraph loads the previous checkpoint automatically.
- The graph remembers the user’s name.

### Real-world use

A chatbot can remember:

- user name,
- preferred language,
- recent questions,
- temporary session data.

---

# 2. Fault Tolerance

## What is it?

If the application **crashes or stops**, the graph can **resume from the last saved checkpoint** instead of starting again.

---

## Example

```python
config = {"configurable": {"thread_id": "job-1"}}

# Step 1 completed and saved
graph.invoke({"step": 1}, config=config)

# 💥 Application crashes here

# Restart application and resume
graph.invoke({"step": 2}, config=config)
```

### What happens?

- Checkpoint after step 1 is already stored.
- After restart, LangGraph loads the saved state.
- Execution continues from the last checkpoint.

---

## Visual

```text
Start
  │
  ├── Step 1 ✅ (checkpoint saved)
  │
  ├── 💥 Crash
  │
Restart
  │
  └── Resume from Step 1 → Step 2
```

### Real-world use

Useful for:

- long-running data pipelines,
- document processing,
- API workflows,
- background jobs.

---

# 3. HITL (Human-in-the-Loop)

## What is it?

The graph can **pause and wait for human input**, then continue execution later.

This is one of the most important features enabled by persistence.

---

## Example

```python
from langgraph.types import interrupt

def ask_human(state):
    answer = interrupt("Approve the request?")
    return {"approved": answer}
```

When the graph reaches `interrupt(...)`:

- execution pauses,
- state is checkpointed,
- control returns to the application.

Later, a human provides input and the graph resumes.

---

## Resume with human answer

```python
graph.invoke(
    Command(resume=True),
    config=config
)
```

---

## Visual Flow

```text
Node A
  │
  ▼
Ask Human
  │
  ├── Pause & save checkpoint
  │
  └── Waiting for approval...
          │
          ▼
     Human approves
          │
          ▼
       Node B
```

### Real-world use

- manager approval,
- compliance review,
- content moderation,
- customer-support escalation.

---

# 4. Time Travel (Helps Debugging)

## What is it?

Because every checkpoint is stored, you can **go back to an earlier state and replay the workflow from that point**.

This is called **time travel**.

---

## Example

Suppose the checkpoints are:

| Checkpoint | State |
|---|---|
| CP1 | `[1]` |
| CP2 | `[1, 2]` |
| CP3 | `[1, 2, 3]` |

You can load **CP2** and continue from there.

```python
snapshot = graph.get_state(config)

print(snapshot.values)
```

Output:

```python
{"numbers": [1, 2]}
```

Now replay from that point:

```python
graph.invoke(
    {"numbers": [99]},
    config=config
)
```

New state:

```python
[1, 2, 99]
```

---

## Visual

```text
CP1 → [1]
  │
CP2 → [1, 2]
  │
CP3 → [1, 2, 3]

⬅️ Go back to CP2

CP2 → [1, 2]
  │
  └── Replay with new input
          ↓
      [1, 2, 99]
```

### Real-world use

- debugging workflows,
- reproducing bugs,
- testing different prompts,
- auditing AI decisions.

---

# Summary Table

| Benefit | What it does | Simple Example |
|---|---|---|
| **Short-Term Memory** | Remembers previous state | Remember user name |
| **Fault Tolerance** | Resume after crash | Continue a job from last checkpoint |
| **HITL** | Pause for human input | Approval workflow |
| **Time Travel** | Go back to an old checkpoint | Replay from CP2 |

---

# One Simple Workflow Showing All 4

```text
User: “Process my loan request”
        │
        ▼
Remember user info (Short-Term Memory)
        │
        ▼
Save checkpoint
        │
        ▼
Ask manager approval (HITL)
        │
   Pause & persist
        │
Manager approves
        ▼
Resume execution
        │
        ▼
System crashes? (Fault Tolerance)
        │
Restart
        ▼
Continue from saved checkpoint
        │
        ▼
Need to audit later? (Time Travel)
        │
Load old checkpoint and replay
```

---

# One-Line Revision

> **Persistence gives LangGraph memory, crash recovery, human approval pauses, and the ability to rewind and replay workflows from any saved checkpoint.**
---

## What is Streaming

- In LLms, streaming means the model starts sending tokens (words) as soon as they're generated, instead of waiting for the entire response to be ready before returning it. 

### Why Streaming

1. Faster response time - low drop-off rates
2. Mimics human like conversation (Builds trust, feels alive and keeps the user engaged)
3. Important for Multi-modal Us
4. Better UX for long output such as code
5. You can cancel midway saving tokens
6. You can interleave Ui updates.

---
# LangSmith Notes (Observability for LLM Applications)

## Why I need this topic

In real AI applications, the model may:

- become **slow (latency issue)**
- become **expensive (token/cost issue)**
- start giving **hallucinated answers**
- fail with **errors**
- behave differently after prompt/model changes

To debug these problems, we need **observability**.

---

# LangSmith Notes – Observability & Debugging for AI Applications

---

# 1. Why Observability Is Needed in AI Systems

In traditional backend systems, we monitor:

- API latency
- Error rates
- CPU / memory
- Database performance

But AI applications introduce new problems:

- LLM responses become slow
- Token usage increases
- Costs suddenly rise
- RAG systems hallucinate
- Agents take unexpected actions
- Prompt changes break workflows

Without observability, debugging becomes **guesswork**.

---

# 2. Real Examples

---

## Example 1: Resume & Cover Letter Generator

### Workflow

```text
User uploads resume
      |
      v
Provide Job Description (JD)
      |
      v
LLM analyzes JD
      |
      v
LLM rewrites resume
      |
      v
LLM generates cover letter
      |
      v
Return final documents
```

### Problem: High Latency

Earlier response time:

```text
8 seconds
```

Now:

```text
25+ seconds
```

### What needs debugging?

- Which LLM call is slow?
- Is the JD too large?
- Is prompt chaining causing delay?
- Is there a retry loop?

### Without observability

```text
Only know: "API is slow"
```

### With observability

```text
JD analysis call      -> 15s
Resume rewrite call   -> 4s
Cover letter call     -> 3s
Total                 -> 22s
```

Now we know the **JD analysis step is the bottleneck**.

---

## Example 2: Research Report Agent

### Workflow

```text
User provides research topic
      |
      v
Agent searches online
      |
      v
Collects articles
      |
      v
Summarizes findings
      |
      v
Generates final report
```

### Problem: Cost Increased

Earlier:

```text
1 report = ₹1
```

Now:

```text
1 report = ₹2
```

### Possible reasons

- More web search results fetched
- Larger context passed to LLM
- Additional hidden LLM calls
- Agent stuck in a reasoning loop
- Model changed from cheaper to expensive one

### What observability reveals

```text
Search tool called        3 times
Summarization LLM         1 time
Report generation LLM     1 time
Unexpected retry loop     2 extra calls
Total tokens doubled
```

Root cause:

```text
Retry loop triggered because one tool returned malformed JSON.
```

---

## Example 3: RAG Chatbot for Company Policies

### Use case

Chatbot answers questions about:

- Leave policy
- Insurance
- Promotions
- Benching
- Project allocation
- Working hours
- Reimbursement rules

### RAG Architecture

```text
Company documents
      |
      v
Chunking
      |
      v
Embeddings
      |
      v
Vector Database
      |
      v
Retriever
      |
      v
LLM
      |
      v
Final answer
```

### Problem: Hallucinations

User asks:

```text
How many casual leaves do I get?
```

Actual policy:

```text
12 casual leaves
```

LLM answers:

```text
15 casual leaves
```

### Why did this happen?

Possible reasons:

- Wrong chunks retrieved
- No relevant chunk found
- LLM answered from general knowledge
- Chunk size too large
- Embedding mismatch

### With observability

We can inspect:

```text
Retrieved chunks:
- Promotion policy
- Insurance policy
- Travel reimbursement policy

No leave-policy chunk retrieved.
```

Root cause becomes clear.

---

# 3. What Is Observability?

## Simple Definition

> Observability is the ability to understand what is happening inside a system by examining its inputs, outputs, intermediate steps, performance, cost, and errors.

---

## In AI Systems

Observability helps us answer:

### What did the user ask?

```text
Input prompt
```

### What did the model return?

```text
Final response
```

### What happened in between?

```text
Prompt templates
Retriever results
Tool calls
Agent reasoning steps
```

### How long did it take?

```text
Latency per step
```

### How much did it cost?

```text
Token usage + API cost
```

### Did something fail?

```text
Errors / exceptions
```

---

# 4. Enter LangSmith

## Definition

> LangSmith is a unified observability and evaluation platform where teams can debug, test, and monitor AI application performance.

### Official website

```text
https://smith.langchain.com
```

---

# 5. What LangSmith Traces

A **trace** is a complete record of one AI application execution.

---

## 1. Input and Output

### Input

```text
"Generate a resume for a Python developer role"
```

### Output

```text
Final resume content
```

This helps reproduce issues.

---

## 2. Intermediate Steps

LangSmith records every internal operation.

### Example

```text
Step 1: Analyze JD
Step 2: Extract required skills
Step 3: Rewrite resume
Step 4: Generate cover letter
```

For RAG:

```text
Step 1: Embed query
Step 2: Retrieve chunks
Step 3: Build context
Step 4: Generate answer
```

This is the **most valuable feature for debugging**.

---

## 3. Latency

Shows time taken by each step.

### Example

```text
Retriever              120ms
Prompt formatting       10ms
LLM call              4200ms
Output parser           15ms
Total                 4345ms
```

Use it to identify bottlenecks.

---

## 4. Token Usage

Tracks:

- Prompt tokens
- Completion tokens
- Total tokens

### Example

```text
Prompt tokens      1200
Completion tokens   350
Total              1550
```

Useful for optimization.

---

## 5. Cost

### Example

```text
GPT-4o call -> $0.012
Embedding   -> $0.001
Total       -> $0.013
```

You can compare executions and detect sudden cost spikes.

---

## 6. Errors

Captures exceptions automatically.

### Example

```text
OutputParserException:
Expected JSON but received plain text
```

No need to search logs manually.

---

## 7. Tags

Used to categorize traces.

### Examples

```python
tags=["resume", "production", "gpt4o"]
```

Filter traces by:

- feature
- environment
- model
- customer
- experiment

---

## 8. Metadata

Attach business information.

### Example

```python
metadata={
    "user_id": "u123",
    "plan": "premium",
    "feature": "research_agent"
}
```

Helps correlate cost and performance with users or plans.

---

## 9. Feedback

Store human evaluation.

### Example

```text
Thumbs up/down
Rating (1-5)
Reviewer comments
```

Used for continuous improvement and evaluation datasets.

---

# 6. Visual Trace Example

```text
User Question
   |
   v
Retriever -------------------- 80ms
   |
   v
Retrieved 4 chunks
   |
   v
Prompt Builder ---------------- 5ms
   |
   v
LLM Call ------------------- 3500ms
   |
   v
Output Parser --------------- 10ms
   |
   v
Final Response

Total latency: 3595ms
Tokens: 1420
Cost: $0.009
```

This gives a **complete execution timeline**.

---

# 7. How LangSmith Solves the Earlier Problems

---

## Resume Generator (Latency)

### Before

```text
Total API time = 25s
No idea which step is slow
```

### After

```text
JD analysis = 18s
Resume rewrite = 4s
Cover letter = 2s
```

### Fix

- Reduce JD size
- Summarize JD first
- Use a faster model for extraction

---

## Research Agent (Cost)

### Before

```text
Cost doubled unexpectedly
```

### After

```text
Tool retry loop detected
Extra 3 LLM calls observed
Token usage increased from 4k -> 9k
```

### Fix

- Add retry limit
- Validate tool outputs
- Cache search results

---

## RAG Hallucination

### Before

```text
Wrong leave-policy answer
```

### After

```text
No relevant leave-policy chunk retrieved
LLM answered from prior knowledge
```

### Fix

- Improve chunking
- Increase top-k retrieval
- Add similarity threshold
- Add "If context is missing, say I don’t know"

---

# 8. Key Interview Question

## Q: What is the difference between logging and observability?

### Logging

```text
Print statements
Error logs
Basic request logs
```

### Observability

```text
Inputs/outputs
Intermediate steps
Latency
Token usage
Cost
Errors
Metadata
Feedback
```

### Interview Answer

> Logging tells us that something happened, while observability helps us understand **why it happened and how the entire AI workflow behaved**.

---

# 9. How to Enable LangSmith (Basic)

```python
from langsmith import traceable

@traceable
def generate_resume(jd, resume):
    ...
```

Set environment variables:

```bash
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=your_key
export LANGCHAIN_PROJECT=resume-generator
```

After this, traces automatically appear in the LangSmith dashboard.

---

# 10. Best Practices

## Use tags

```python
tags=["production", "rag", "policy-bot"]
```

---

## Add metadata

```python
metadata={"user_id": user_id}
```

---

## Trace every external dependency

- LLM calls
- Vector DB retrieval
- Web search
- Database queries
- Tool executions

---

## Create evaluation datasets

Store good and bad examples and run automated evaluations after prompt changes.

---

# 11. One-Line Revision Points

## Observability

```text
Understand the internal behavior of an AI system.
```

## Trace

```text
A complete record of one execution.
```

## Latency

```text
Time taken by each step.
```

## Token Usage

```text
Number of prompt and completion tokens consumed.
```

## Cost

```text
API cost for a single execution.
```

## Hallucination

```text
Model generates information not grounded in retrieved context.
```

## LangSmith

```text
A platform to debug, monitor, evaluate, and improve LLM applications.
```

---
# 2. Monitoring & Alerting

Once an AI application goes into production, we need continuous monitoring.

LangSmith provides dashboards for monitoring production traffic.

---

## What can be monitored?

### Latency

Example

```text
Average Response Time

Yesterday
2.4 seconds

Today
7.9 seconds
```

Immediately indicates performance degradation.

---

### Error Rate

Example

```text
Yesterday
1%

Today
12%
```

Shows something is failing after deployment.

---

### Token Usage

Monitor

- Prompt tokens
- Completion tokens
- Total tokens

Useful for controlling LLM costs.

---

### Cost Monitoring

Example

```text
Yesterday

₹1 per report

Today

₹2.5 per report
```

LangSmith helps identify:

- Which prompt became expensive
- Which agent is consuming more tokens
- Whether retries are increasing cost

---

## Alerting

LangSmith can notify teams when predefined thresholds are crossed.

Examples:

- Latency > 10 seconds
- Cost per request increases by 30%
- Error rate exceeds 5%
- Hallucination score increases
- Tool failure rate increases

This helps teams react before users report issues.

---

# 3. Evaluation (Very Important)

Evaluation answers the question:

> Is my AI application actually producing good responses?

Instead of manually checking every output, LangSmith automates evaluations.

---

## Why evaluation?

Imagine changing:

- Prompt
- Model
- Temperature
- Retrieval strategy

How do you know whether responses became better?

Evaluation measures quality automatically.

---

## Types of Evaluation

### Correctness

Did the model answer correctly?

---

### Relevance

Is the answer related to the user's question?

---

### Faithfulness

Is the answer grounded in retrieved documents?

Especially important in RAG systems.

---

### Helpfulness

Would a user find this response useful?

---

### Toxicity / Safety

Does the response contain unsafe or offensive content?

---

## Example

Question

```text
How many casual leaves do employees receive?
```

Ground Truth

```text
12 Casual Leaves
```

LLM Output

```text
12 Casual Leaves
```

Evaluation

```text
Correctness
100%

Faithfulness
100%

Relevance
100%
```

---

## Benefits

- Compare different prompts
- Compare different models
- Prevent regressions
- Improve quality over time

---

# 4. Prompt Experimentation

One of LangSmith's strongest features.

Instead of guessing which prompt is better, we compare them scientifically.

---

## Example

Prompt A

```text
Summarize the document.
```

Prompt B

```text
Summarize the document in bullet points with action items.
```

Run both prompts on the same dataset.

Compare:

- Accuracy
- Cost
- Latency
- User ratings

Choose the better prompt.

---

## Compare Models

Example

```text
GPT-4o

vs

Claude

vs

Gemini
```

Compare:

- Speed
- Cost
- Accuracy
- Hallucination rate

---

## Benefits

No guessing.

Use data to decide which prompt performs best.

---

# 5. Dataset Creation & Annotation

Evaluation requires datasets.

LangSmith helps create and manage datasets.

---

## Dataset Example

| Input | Expected Output |
|--------|-----------------|
| Leave Policy | 12 casual leaves |
| Insurance | Medical insurance available |
| Promotion | Promotion after annual review |

---

These datasets can be reused for testing every time prompts change.

---

## Annotation

Humans can label responses.

Example

```text
Correct

Incorrect

Partially Correct
```

Or

```text
Rating

1

2

3

4

5
```

Annotations improve evaluation quality.

---

# 6. User Feedback Collection

Real users provide the best evaluation.

LangSmith allows collecting feedback directly.

Examples

👍 Helpful

👎 Not Helpful

⭐ Rating

Comment

---

Example

```text
Question

How many leaves do I get?

Response

12 Casual Leaves

User Feedback

⭐⭐⭐⭐⭐
```

Another

```text
Question

Insurance Policy

Response

Incorrect Answer

User Feedback

👎
```

This feedback can later become training or evaluation data.

---

# 7. Collaboration

LangSmith is designed for teams.

Different people can work together.

Examples

- AI Engineers
- Backend Developers
- ML Engineers
- Product Managers
- QA Engineers

---

Everyone can view:

- Traces
- Evaluations
- Prompt versions
- User feedback
- Performance dashboards

Instead of sending screenshots, the entire execution trace can be shared.

---

# Real Project Example

## Resume Generator

Problem

```text
Resume generation suddenly takes 30 seconds.
```

LangSmith shows

```text
JD analysis

22 seconds

Resume generation

5 seconds

Cover letter

3 seconds
```

Root Cause

```text
Large Job Description.
```

---

## Research Agent

Problem

```text
Cost increased from ₹1 to ₹2.5.
```

LangSmith shows

```text
Extra retry loop.

Additional LLM calls.

Token usage doubled.
```

---

## RAG Chatbot

Problem

```text
Wrong leave policy answer.
```

LangSmith trace shows

```text
Retriever fetched insurance documents.

Leave policy document never retrieved.
```

Root Cause

```text
Retriever failure.

Not an LLM issue.
```
---

## Difference between Logging and LangSmith

### Logging

- API Logs
- Error Logs
- Print Statements

Limited visibility.

---

### LangSmith

- Complete execution trace
- Prompt inspection
- Tool execution
- Agent reasoning
- Cost analysis
- Token tracking
- Evaluation
- User feedback

Provides complete observability.

--- 
# LangGraph ToolNode, tools_condition & MCP Notes

---

# 1. What is a Tool in an LLM?

An LLM by itself **cannot**:

- Access databases
- Search the internet
- Read local files
- Call APIs
- Send emails
- Query GitHub
- Execute Python code

Instead, we expose these capabilities as **Tools**.

A tool is simply a Python function (or API) that performs a task on behalf of the LLM.

---

## Example Tool

```python
from langchain.tools import tool

@tool
def get_weather(city: str):
    """Returns weather for a city."""
    return f"The weather in {city} is 28°C."
```

Now the LLM can call:

```text
get_weather("Mumbai")
```

instead of trying to guess the answer.

---

# 2. What is ToolNode?

## Definition

> A **ToolNode** is a prebuilt LangGraph node that automatically executes tools requested by the LLM.

Normally in LangGraph, you write every node yourself.

Example:

```python
def my_node(state):
    ...
    return state
```

A ToolNode saves you from writing all the tool execution logic.

It already knows how to:

- Detect tool calls
- Find the correct tool
- Execute it
- Capture the result
- Return the result back to the graph

---

# Without ToolNode

Suppose the LLM wants weather information.

You would need to manually:

```text
LLM says:
"I need get_weather()"

        |

Detect tool call

        |

Find correct Python function

        |

Execute function

        |

Capture result

        |

Append result into state

        |

Return to LLM
```

You write all this yourself.

---

# With ToolNode

You simply provide your tools.

```python
ToolNode(tools)
```

Everything else happens automatically.

---

# Example

```python
from langgraph.prebuilt import ToolNode

tool_node = ToolNode(
    tools=[get_weather, search_docs]
)
```

That's it.

Whenever the LLM requests one of those tools, ToolNode executes it.

---

# Internal Flow

```text
User

   |

   v

LLM

   |

   v

"I want get_weather()"

   |

   v

ToolNode

   |

   v

Runs Python Function

   |

   v

Returns Result

   |

   v

LLM

   |

   v

Final Answer
```

---

# 3. What is tools_condition?

ToolNode executes tools.

But how does the graph know **whether it should go to ToolNode or not?**

That decision is made by **tools_condition**.

---

## Definition

> `tools_condition` is a prebuilt conditional edge in LangGraph that checks whether the LLM requested a tool.

It answers the question:

```text
Should I execute a tool?

OR

Should I continue the conversation?
```

---

# Visual Flow

```text
User

   |

   v

LLM

   |

   v

tools_condition

   |

   +------------------------+

   |                        |

Tool Needed?             No Tool Needed

   |                        |

   v                        v

ToolNode                 END

   |

   v

Back to LLM

   |

   v

Final Response
```

---


# Graph Code

```python
graph.add_conditional_edges(
    "chatbot",
    tools_condition
)
```

LangGraph automatically decides where to go.

---

# Summary

ToolNode

```text
Executes tools.
```

tools_condition

```text
Decides whether a tool should be executed.
```

---

# Interview Question

## Difference between ToolNode and tools_condition?

### ToolNode

- Executes tool
- Runs Python functions
- Returns tool output

### tools_condition

- Makes routing decision
- Checks if LLM requested a tool
- Sends graph to ToolNode if required

---

# 4. MCP (Model Context Protocol)

## What is MCP?

> MCP (Model Context Protocol) is an open standard that allows AI models to communicate with external applications through standardized servers instead of custom tool implementations.

Think of MCP as **USB-C for AI applications**.

Instead of writing custom integrations for every application, AI connects using a common protocol.

---

# Why was MCP introduced?

Suppose your chatbot needs access to:

- GitHub
- Slack
- Google Drive
- PostgreSQL
- Jira
- Notion

Without MCP, you write a custom tool for every service.

---

# Without MCP

Example

You want the LLM to list GitHub Pull Requests.

You write:

```python
def get_pull_requests(repo):
    ...
```

Inside this function you manually:

- Authenticate
- Handle tokens
- Call GitHub API
- Parse JSON
- Handle pagination
- Handle retries
- Update code when GitHub changes APIs

Every project repeats this work.

---

# Problems

- Duplicate code
- API version changes
- Authentication management
- Difficult maintenance
- Tight coupling

---

# With MCP

Instead of writing API logic yourself:

```text
LLM

↓

GitHub MCP Server

↓

GitHub API
```

The MCP server handles everything.

Your application only communicates using the MCP protocol.

---

# Why is this Better?

If GitHub changes:

```text
GitHub API v2

↓

Only GitHub MCP Server updates

↓

Your application continues working
```

No changes needed in your AI application.

---

# Benefits of MCP

- Standardized integrations
- Less custom code
- Easier maintenance
- Reusable connectors
- Better security
- Version compatibility
- Plug-and-play architecture

---

# Real MCP Servers

There are MCP servers for:

- GitHub
- Slack
- Google Drive
- Gmail
- PostgreSQL
- SQLite
- Jira
- Notion
- Filesystem
- Web Browser

Instead of writing tools for each one, simply connect to the MCP server.

---

# Tool vs MCP

| Tool | MCP |
|-------|-----|
| Python function | External standardized server |
| Project-specific | Reusable across projects |
| You maintain it | MCP server maintains integration |
| Manual API integration | Standard protocol |
| Tight coupling | Loose coupling |
| Breaks when APIs change | MCP server absorbs API changes |

---

# Example Comparison

## Tool

```python
@tool
def github_prs(repo):
    ...
```

Every project implements similar logic.

---

## MCP

```text
LLM

↓

GitHub MCP Server

↓

GitHub API
```

No GitHub-specific code inside your application.

---

# When Should You Use Tools?

- Simple calculations
- Local Python functions
- Internal business logic
- Small utilities
- Quick prototypes

Examples

- Calculator
- Date formatting
- Currency conversion
- Internal database lookup

---

# When Should You Use MCP?

- GitHub
- Slack
- Gmail
- Notion
- Google Drive
- Jira
- Enterprise systems
- External services used by multiple projects

---

# Interview Questions

## What is ToolNode?

```text
A prebuilt LangGraph node that automatically executes tools requested by the LLM.
```

---

## What is tools_condition?

```text
A prebuilt conditional edge that decides whether the graph should execute a tool or continue the conversation.
```

---

## What is MCP?

```text
Model Context Protocol (MCP) is an open standard that enables AI models to communicate with external applications through standardized servers instead of custom tool implementations.
```

---

## Why is MCP better than writing tools?

```text
MCP reduces maintenance by standardizing integrations. When an external API changes (like GitHub), only the MCP server needs updating instead of every AI application.
```

---

## Transport Types

### 1. stdio

Used when the MCP Server is running locally.

Example:

```python
{
    "transport": "stdio",
    "command": sys.executable,
    "args": ["calculator_server.py"]
}
```

Flow

```
LangGraph
    │
    ▼
Local Python Process
    │
    ▼
Tool
```

---

### 2. http

Used when the MCP Server is hosted remotely.

Example

```python
{
    "transport": "http",
    "url": "https://search.parallel.ai/mcp"
}
```

Flow

```
LangGraph
    │
    ▼
HTTP Request
    │
    ▼
Remote MCP Server
    │
    ▼
Remote Tool
```

---

# Parallel Search MCP

Website

https://search.parallel.ai/mcp

Authentication

✅ No Authentication Required

Transport

HTTP

---

# Free MCP Servers (No Authentication Required)

These MCP servers are great for learning LangGraph + MCP because they require **no authentication** and let you focus on understanding the MCP protocol instead of OAuth or API keys.

| MCP Server | Auth | Transport | Best For | Difficulty |
|------------|------|-----------|----------|------------|
| Parallel Search | ✅ No Auth | HTTP | AI Search Agent | ⭐⭐⭐⭐⭐ |
| MCPub | ✅ No Auth | HTTP | Discovering MCP Servers | ⭐⭐⭐⭐⭐ |
| Official Fetch | ✅ No Auth | stdio / HTTP (self-host) | Reading Websites | ⭐⭐⭐⭐ |
| Everything Server | ✅ No Auth | stdio / HTTP (self-host) | Learning every MCP feature | ⭐⭐⭐⭐⭐ |
| CatAPI MCP | ✅ No Auth | HTTP | Simple API integration | ⭐⭐⭐ |

---

# 1. Parallel Search MCP ⭐⭐⭐⭐⭐

## What is it?

A hosted Remote MCP Server that provides real-time internet search capabilities.

It exposes web search as MCP tools so your LLM can search the internet whenever required.

No need to write your own search API.

---

## Transport

HTTP

---

## Authentication

✅ No Authentication Required (Basic Usage)

---

## Python Configuration

```python
from typing import cast
import sys
from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    cast(dict, {
        "parallel_search": {
            "transport": "http",
            "url": "https://search.parallel.ai/mcp"
        }
    })
)
```

---

## Available Tools

```
web_search

web_fetch
```

---

## Example Questions

```
What is LangGraph?
```

```
Latest FastAPI release
```

```
Latest AI News
```

```
Research RAG Architecture
```

```
Compare FastAPI vs Flask
```

```
Summarize latest OpenAI announcements
```

---

## Agent Flow

```
User

↓

LLM

↓

web_search()

↓

Parallel MCP

↓

Search Results

↓

LLM

↓

Answer
```

---

# 2. MCPub ⭐⭐⭐⭐⭐

## What is it?

Think of MCPub as a **Google Search for MCP Servers**.

It lets your AI discover publicly available MCP servers.

---

## Transport

HTTP

---

## Authentication

✅ No Authentication Required

---

## Python Configuration

```python
client = MultiServerMCPClient({
    "mcpub": {
        "transport": "http",
        "url": "https://mcpub.dev/mcp"
    }
})
```

---

## Available Tools

```
search()

search_live()

list_all()

list_all_live()

get()

submit()
```

---

## Example Questions

```
Find GitHub MCP Servers
```

```
Find Weather MCP Servers
```

```
Find Database MCP Servers
```

```
List all live MCP Servers
```

---

## Agent Flow

```
User

↓

LLM

↓

search_live()

↓

MCPub

↓

Matching MCP Servers

↓

LLM
```

---

# 3. Official Fetch MCP ⭐⭐⭐⭐

## What is it?

Official MCP Server that fetches webpage content and converts HTML into Markdown.

Useful for:

- Documentation
- Blogs
- RAG
- Research

---

## Authentication

✅ No Authentication Required

---

## Installation

```bash
pip install mcp-server-fetch
```

---

## Python Configuration

```python
client = MultiServerMCPClient({
    "fetch": {
        "transport": "stdio",
        "command": sys.executable,
        "args": [
            "-m",
            "mcp_server_fetch"
        ]
    }
})
```

---

## Available Tool

```
fetch()
```

---

## Example Questions

```
Read FastAPI Documentation
```

```
Summarize this webpage

https://fastapi.tiangolo.com/
```

```
Extract key points from this blog
```

---

## Agent Flow

```
User

↓

LLM

↓

fetch(url)

↓

Website

↓

Markdown

↓

LLM
```

---

# 4. Everything Server ⭐⭐⭐⭐⭐

## What is it?

The Official Reference MCP Server.

It demonstrates every major feature supported by MCP.

This server is designed specifically for developers learning MCP.

---

## Authentication

✅ No Authentication Required

---

## Installation

```bash
npx -y @modelcontextprotocol/server-everything
```

---

## Python Configuration

```python
client = MultiServerMCPClient({
    "everything": {
        "transport": "stdio",
        "command": "npx",
        "args": [
            "-y",
            "@modelcontextprotocol/server-everything"
        ]
    }
})
```

Windows

```python
client = MultiServerMCPClient({
    "everything": {
        "transport": "stdio",
        "command": "cmd",
        "args": [
            "/c",
            "npx",
            "-y",
            "@modelcontextprotocol/server-everything"
        ]
    }
})
```

---

## What can you learn?

✅ Tools

✅ Resources

✅ Prompts

✅ Sampling

✅ MCP Protocol

---

## Best Use Case

Learning how MCP works internally.

---

# 5. CatAPI MCP ⭐⭐⭐

## What is it?

A simple MCP Server wrapping the public Cat API.

Good for learning HTTP-based MCP servers without authentication.

---

## Authentication

✅ No Authentication Required

---

## Example Questions

```
Show me 5 cat images.
```

```
Random cat fact.
```

```
Random cat picture.
```

---

# Using Multiple MCP Servers

LangGraph can connect to multiple MCP Servers simultaneously.

Example

```python
from typing import cast
import sys

client = MultiServerMCPClient(
    cast(dict, {

        "calculator": {
            "transport": "stdio",
            "command": sys.executable,
            "args": ["09_langgraph_mcp_server.py"]
        },

        "parallel_search": {
            "transport": "http",
            "url": "https://search.parallel.ai/mcp"
        },

        "mcpub": {
            "transport": "http",
            "url": "https://mcpub.dev/mcp"
        }
    })
)

tools = await client.get_tools()
```

---

# Example Multi-MCP Flow

Prompt

```
Find the latest FastAPI release.

Calculate the cost of 35 servers if each costs $42.

Then summarize everything.
```

Execution

```
Human

↓

LLM

↓

web_search()

↓

Parallel Search MCP

↓

Search Results

↓

multiply()

↓

Calculator MCP

↓

Result

↓

LLM

↓

Final Response
```

---

# Interview Notes

✅ MCP Servers can be Local or Remote.

✅ Local MCP uses stdio.

✅ Remote MCP typically uses HTTP.

✅ One LangGraph application can connect to multiple MCP Servers.

✅ The LLM decides which tool should be called.

✅ ToolNode executes the selected tool.

✅ MCP Server executes the tool.

✅ Tool output is returned to the LLM.

✅ The LLM generates the final answer using the tool result.

---

# RAG (Retrieval-Augmented Generation)

## Why RAG?

- **Outdated Knowledge**
  - LLMs have a training cutoff and cannot access newly published information.
- **Privacy**
  - Allows LLMs to use private or proprietary data without retraining.
- **Reduce Hallucinations**
  - Grounds responses in retrieved documents, improving factual accuracy.

---

## What is RAG?

**RAG = Retrieval + Generation**

It is a technique where an LLM retrieves relevant information from an external knowledge base before generating a response.

---

## How RAG Works

1. User submits a query.
2. Convert the query into an embedding.
3. Search the vector database for similar document chunks.
4. Retrieve the most relevant chunks.
5. Pass the retrieved context along with the query to the LLM.
6. LLM generates the final response.

---

## RAG Architecture

![RAG Architecture](images_md/rag_explanation.png)

---

# Human-in-the-Loop (HITL)

## What is HITL?
**Human-in-the-Loop (HITL)** is a design approach where a human participates at critical points in an AI workflow to **supervise, approve, correct, or guide** the AI's output before it proceeds.

---

## Why HITL?

- Improve reliability of agentic systems
- Add human accountability for important actions

---

## What HITL Ensures

- ✅ Accuracy
- ✅ Safety
- ✅ Ethical alignment
- ✅ Better user experience
- ✅ Human oversight for critical decisions

---

## Common HITL Patterns

### 1. Action Approval Pattern
Human approves or rejects an action **before execution**.

**Example:**
- Send an email
- Execute a database query
- Make a payment

---

### 2. Output Review / Edit Pattern
Human reviews, edits, or provides feedback on AI-generated content before it is finalized.

**Example:**
- Edit a generated email
- Improve a report
- Modify SQL generated by the AI

---

### 3. Ambiguity Clarification Pattern
The AI pauses to ask the human for clarification when the request is ambiguous or missing information.

**Example:**
- "Which customer account should I use?"
- "Do you mean the production or staging environment?"

---

### 4. Escalation Pattern
The AI hands control to a human when it cannot confidently complete a task.

**Example:**
- Fraud detection
- Legal review
- Medical decision support
- Customer support escalation

---

# HITL in LangGraph

LangGraph implements HITL using **interrupts**.

The graph pauses execution at a specific node, waits for human input, and resumes from the same point after receiving a response.

## Flow

```
Start
  ↓
Agent executes
  ↓
interrupt()
  ↓
Human reviews / approves / edits
  ↓
Command(resume=...)
  ↓
Graph continues
```

---

## Human Input in LangGraph

Human input is **not limited to Yes/No**.

It can be:

- Approval (`Yes`)
- Rejection (`No`)
- Free-text feedback
- Suggestions
- Corrections
- Structured JSON/object
- Completely edited content

---
# Example

## Social Media Manager Agent
![langgraph_hitl](images_md/langgraph_hitl.png)
---

## Key Takeaways

- HITL = Human supervision inside an AI workflow.
- LangGraph enables HITL using `interrupt()` and `Command(resume=...)`.
- Human responses can be **approval, rejection, edits, feedback, or structured data**.
- HITL is useful whenever actions are **high-risk, irreversible, expensive, or require human judgment**.

---

# LangGraph Subgraphs

## What are Subgraphs?

A **Subgraph** in LangGraph is a graph that is embedded and executed as a node inside another (parent) graph.

Instead of placing all the workflow logic in a single graph, you can divide complex workflows into smaller, reusable graphs called **subgraphs**.

> Think of a subgraph as a reusable workflow module that can be plugged into multiple parent graphs.

---

# Why are Subgraphs Needed?

Subgraphs help organize and simplify complex AI workflows by providing:

- **Modularity** – Break large workflows into smaller, manageable components.
- **Reusability** – Reuse the same workflow in multiple parent graphs.
- **Separation of Concerns** – Keep different responsibilities isolated.
- **Failure Isolation** – Errors inside a subgraph remain isolated, making debugging easier.
- **Independent State Management** – A subgraph can maintain its own state.
- **Better Maintainability** – Easier to understand, modify, and extend.
- **Scalability** – Build enterprise-scale workflows without creating one huge graph.
- **Team Collaboration** – Different teams can develop different subgraphs independently.

---

# Common Use Cases

Subgraphs are commonly used for implementing reusable workflows such as:

- Tool Calling
- Retrieval-Augmented Generation (RAG)
- Conditional Routing
- Retry Logic
- Memory Management
- Human-in-the-Loop (HITL)
- Evaluation Pipelines
- Guardrails
- Multi-Agent Systems
- Data Validation
- Content Moderation
- Document Processing Pipelines

---

# Benefits of Using Subgraphs

## 1. Failure Isolation

If a subgraph encounters an error, the failure is isolated within that workflow.

This makes:
- debugging easier
- retries more manageable
- workflows more reliable

---

## 2. Independent State

A subgraph can maintain its own state without exposing all internal variables to the parent graph.

Benefits include:

- Cleaner state management
- Less state pollution
- Better encapsulation
- Easier debugging

---

# Ways to Implement Subgraphs in LangGraph

LangGraph supports **two approaches** for implementing subgraphs.

---

## Method 1: Invoke a Graph from Inside a Node

In this approach, the parent graph calls another graph from within a node function.

### Flow

```text
Parent Graph
      │
      ▼
 Parent Node
      │
      ▼
subgraph.invoke(...)
      │
      ▼
 Returns Result
```

### Characteristics

- Parent graph manually invokes the subgraph.
- Parent and subgraph can have completely different state schemas.
- The parent decides what information to pass.
- The parent decides what result to receive.
- Best when the subgraph should remain independent.

### Features

- ✅ Separate state
- ✅ Better encapsulation
- ✅ Reusable
- ✅ Easier testing
- ✅ Strong isolation

### Best For

- RAG Pipelines
- Tool Calling
- Multi-Agent Systems
- Independent workflows

---

## Method 2: Add a Graph as a Node

Instead of manually invoking the graph, the compiled graph itself becomes a node in the parent graph.

### Flow

```text
Parent Graph
      │
      ▼
 Subgraph Node
      │
      ▼
 Executes Automatically
```

### Characteristics

- The compiled graph is added directly as a node.
- Parent and subgraph share state.
- State keys are automatically passed between graphs.
- Less boilerplate code.

### Features

- ✅ Shared state
- ✅ Cleaner implementation
- ✅ Easier integration
- ✅ Automatic state passing

### Best For

- Shared workflows
- Sequential pipelines
- Large workflows with common state

---

# Comparison

| Feature | Invoke Graph from Node | Add Graph as Node |
|----------|-----------------------|-------------------|
| State | Separate | Shared |
| State Schema | Can be different | Should be compatible |
| Isolation | High | Moderate |
| Reusability | High | High |
| Boilerplate | Slightly more | Less |
| Best For | Independent workflows | Shared pipelines |

---

# Persistence with Subgraphs

LangGraph supports persistence (checkpointing) even when using subgraphs.

Persistence allows:

- Resume execution after interruption
- Long-running workflows
- Human approval workflows
- Stateful conversations
- Recovery from failures

### How It Works

The parent graph is typically compiled with a **Checkpointer**.

```python
graph.compile(checkpointer=memory)
```

The same checkpointing mechanism automatically tracks execution across parent graphs and subgraphs.

Benefits:

- Resume from checkpoints
- Persistent state
- Supports Human-in-the-Loop
- Fault tolerance
- Conversation memory

---

# Streaming with Subgraphs

Streaming works seamlessly with subgraphs.

When the parent graph streams events, the events generated inside the subgraph are also streamed.

Example:

```python
graph.stream(input)
```

Streaming can include:

- Node execution events
- State updates
- LLM token streaming
- Intermediate outputs
- Tool execution events

This enables real-time monitoring of both parent and subgraph execution.

---

# When Should You Use Each Method?

### Use "Invoke a Graph from a Node" when:

- Separate state is required
- The workflow should be reusable
- Building independent modules
- Encapsulation is important
- Different state schemas are needed

---

### Use "Add Graph as a Node" when:

- Parent and subgraph naturally share state
- Building sequential pipelines
- You want less boilerplate
- Simpler integration is preferred

---

# Key Takeaways

- A **Subgraph** is a graph executed inside another graph.
- Subgraphs improve modularity, reusability, and maintainability.
- They provide **failure isolation** and cleaner workflow organization.
- LangGraph supports **two approaches**:
  - **Invoke a graph from a node** (separate state)
  - **Add a graph as a node** (shared state)
- Subgraphs fully support:
  - Persistence (Checkpointing)
  - Streaming
  - Human-in-the-Loop
  - Memory
  - Tool Calling
  - RAG
  - Conditional Routing
  - Guardrails
  - Evaluation
  - Multi-Agent workflows
- Choose the implementation method based on whether the subgraph should have **independent state** or **shared state**.

---

# LLM Memory

## LLM at Inference

- At inference time, an LLM is essentially a **parameterized mathematical function**.

![llm_function](images_md/llm_function.png)

Mathematically,

$$
y = f_{\theta}(x)
$$
where:

- **x** = Input (prompt)
- **θ (theta)** = Model parameters (weights learned during training)
- **y** = Output (generated response)

---

## LLMs are Stateless

A parameterized mathematical function is **stateless** during inference.

> **Definition:** A system is **stateless** if its output depends **only on the current input** and **not on anything that happened before**.

### Example

Suppose the model parameters (**θ**) remain fixed.

- If the input is **x₁**:

  $$
  y_1 = f_{\theta}(x_1)
  $$

- If the input is **x₂**:

  $$
  y_2 = f_{\theta}(x_2)
  $$

Since **θ** does not change during inference, each output depends only on its corresponding input.

Since **θ** does not change during inference, each output depends only on its corresponding input.

**Therefore:**

- LLMs at inference are generally **stateless**.
- They **do not have any intrinsic memory** of previous interactions.

---

# Context Window

**Context Window** is the amount of text an LLM can read and remember **at one time** before generating a response.

It includes everything provided in the current prompt, such as:

- System prompts
- User messages
- Previous conversation (if included)
- Retrieved documents
- Examples

Anything outside the context window is **not available** to the model during inference.

---

# In-Context Learning

**In-Context Learning (ICL)** is an **emergent ability** that allows an LLM to use information and patterns present **within the prompt itself**, in addition to its learned **parametric knowledge**, to generate an appropriate response.

![in_context_learning](images_md/in_context_learning.png)

In other words, instead of updating its parameters (**θ**), the model temporarily learns from the examples and instructions provided in the current context.

For example, if a prompt contains:

- Instructions
- Examples
- Demonstrations

the LLM can infer the desired pattern and apply it to new inputs within the same context, without any retraining.

---

---

## Key Takeaways

- During inference, an LLM behaves like a **parameterized mathematical function**.
- The model parameters (**θ**) remain fixed during inference.
- LLMs are generally **stateless** and have **no intrinsic memory**.
- A **context window** provides temporary memory for the current interaction.
- **In-context learning** enables the model to learn from examples and instructions present in the prompt without modifying its parameters.

---

# Implementing Memory in LLM Applications

Although an LLM itself is **stateless**, we can build a **stateful application** around it.

This is achieved by combining:

- **Context Window**
- **In-Context Learning**

The application sends relevant conversation history along with every new user message.

Instead of the model remembering previous interactions internally, the application **reconstructs the memory** by including past information in the prompt.

---

## How Chatbots Remember Conversations

In a chatbot:

1. User sends a message.
2. The conversation history (or a portion of it) is retrieved.
3. The history is appended to the current prompt.
4. The entire prompt is sent to the LLM.
5. The LLM generates a response using the provided context.

This creates the illusion that the model remembers previous conversations.

---

# Short-Term Memory (STM)

In LLM applications, **Short-Term Memory (STM)** refers to the conversation history that exists **within a single thread or session**.

> **Short-Term Memory = Thread Scope**

As long as the conversation continues, previous messages remain available through the context window.

---

## Limitations of Short-Term Memory

### 1. STM is Fragile

If:

- the server crashes,
- the application restarts,
- the conversation is lost,

then the memory disappears because it only existed inside the active session.

To avoid this, applications use **persistent storage**.

---

### 2. Context Window Limitation

The context window has a fixed size.

As conversations become longer:

- older messages cannot all fit,
- important information may be dropped.

Applications usually solve this using techniques such as:

- Trimming old messages
- Conversation Summarization
- Hybrid approaches (summary + recent messages)

> **TODO:** Create a diagram explaining:
>
> - Trimming
> - Summarization
> - Hybrid Memory Strategy

---

### 3. STM is Thread-Scoped

Short-term memory exists only within one conversation thread.

Because of this:

1. User continuity is lost across conversations.
2. Learning never compounds over time.
3. Cross-thread reasoning is impossible.

---

# Long-Term Memory (LTM)

To overcome the limitations of STM, applications introduce **Long-Term Memory (LTM)**.

Long-term memory stores information that should survive:

- beyond a single session,
- beyond a single conversation thread,
- across days, weeks, or even months.

Unlike STM, it is **persistent**.

---

## What Should Long-Term Memory Store?

Long-term memory stores information that defines continuity.

Examples include:

1. Who the user is.
2. How the system is expected to behave for that user.
3. What tends to work well and what usually fails.
4. Decisions that were already made in previous conversations.

---

## Long-Term Memory Must Be Selective

Not everything should be remembered forever.

Only information that is:

- Stable
- Useful
- Reusable

should survive beyond a single conversation.

Everything else should naturally fade away.

---

# Types of Long-Term Memory

## 1. Episodic Memory

### What it Stores

Specific past experiences or events.

Examples:

- The user booked a vacation.
- The user asked for a study plan.
- The user completed a project.

### Why it Exists

To recall previous experiences and maintain continuity across conversations.

---

## 2. Semantic Memory

### What it Stores

Facts and knowledge about the user or the world.

Examples:

- User prefers Python.
- User is vegetarian.
- User lives in Mumbai.

### Why it Exists

To personalize future interactions without repeatedly asking for the same information.

---

## 3. Procedural Memory

### What it Stores

Instructions about **how the system should behave**.

Examples:

- Always answer briefly.
- Prefer code examples.
- Use bullet points.
- Explain concepts visually whenever possible.

### Why it Exists

To make the assistant consistently behave according to user preferences.

---

# How Does Long-Term Memory Work?

A typical long-term memory pipeline consists of four stages:

1. Creation / Update
2. Storage
3. Retrieval
4. Injection

---

# 1. Creation / Update

The system first asks:

> **"Is anything from what just happened worth remembering beyond this conversation?"**

### What the System Looks At

- User messages
- Model responses
- Tool outputs

### What Happens

The system:

- Extracts memory candidates.
- Filters out noise.
- Determines the memory scope (User / Agent / Application).
- Decides whether to:
  - Create a new memory
  - Update an existing memory
  - Ignore it

Only high-quality memories move to the next stage.

---

# 2. Storage

Once a memory is accepted, it is written to a durable storage system.

### What Storage Means

- Writing memory to persistent storage
- Assigning unique identifiers
- Adding metadata
- Making the memory survive crashes and restarts

Depending on the application, storage may be:

- Relational Database
- Key-Value Store
- Log Storage
- Vector Database (for semantic retrieval)

---

# 3. Retrieval

Whenever a new request arrives, the system asks:

> **"Given the current situation, what should I remember right now?"**

### Retrieval Process

The system:

- Examines the current input.
- Determines whether memory is needed.
- Searches memory stores.
- Selects only the most relevant memories.

> **Key Point:** Retrieval is **selective**, not exhaustive.

The model should only receive memories that are relevant to the current conversation.

---

# 4. Injection

After retrieval, the selected memories are inserted into the prompt.

### What Injection Means

- Retrieved memories are added to the Short-Term Memory.
- They become part of the context window.
- The LLM simply sees them as additional tokens in the prompt.

The LLM has no special mechanism for reading long-term memory directly.

---

## Relationship Between STM and LTM

Long-Term Memory never directly interacts with the LLM.

Instead, the flow looks like this:

```text
Long-Term Memory
        │
        ▼
   Memory Search
        │
        ▼
     Retrieval
        │
        ▼
 Short-Term Memory
        │
        ▼
 Context Window
        │
        ▼
        LLM
```

The retrieved memories temporarily become part of the context window before the model generates a response.

---

# Challenges of Long-Term Memory

Building a reliable long-term memory system involves several challenges.

## 1. Deciding What Is Worth Remembering

Remembering too much leads to noisy memory.

Remembering too little loses personalization.

---

## 2. Retrieving the Right Memory

The system must retrieve:

- the right memory,
- at the right time,
- for the right task.

Poor retrieval can be worse than having no memory at all.

---

## 3. Orchestrating the Entire Pipeline

The application must coordinate:

- Memory extraction
- Storage
- Retrieval
- Prompt injection

while keeping latency low and memory quality high.

---

# Memory Frameworks

Several frameworks help implement long-term memory in LLM applications.

Examples include:

- LangMem
- Mem0
- Supermemory

These frameworks provide utilities for memory extraction, storage, retrieval, and prompt injection.

---

# Research

## Titan + MIRAS

Titan and MIRAS are research efforts focused on helping AI systems develop more effective **long-term memory**, enabling them to retain and retrieve useful information across extended interactions and long time horizons.

---
# LangGraph: Short-Term Memory (STM), Trimming, Summarization & Hybrid Context

## 1. Short-Term Memory (STM) in LangGraph

LangGraph provides **Short-Term Memory (STM)** using:

- **Checkpointer** → Stores the conversation state.
- **thread_id** → Identifies a unique conversation/session.
- **MessagesState** → Default state object used to store conversation messages.

```python
from langgraph.graph import MessagesState
```

### Production Setup

In production, the recommended approach (as per LangGraph documentation) is to use a **PostgreSQL Checkpointer**.

```
User
   │
   ▼
thread_id
   │
   ▼
Postgres Checkpointer
   │
   ▼
MessagesState
```

Every conversation has its own `thread_id`, allowing LangGraph to retrieve the correct conversation history.

---

# 2. The Problem

LLMs have a **limited context window**.

Example:

```
Model Context Window = 8K Tokens

Conversation
----------------------------------

User
Assistant
User
Assistant
...
...
...
100 Messages

Total = 18K Tokens ❌
```

We cannot send the entire conversation to the LLM.

We need strategies to fit the prompt within the model's token limit.

---

# 3. Trimming

## What is Trimming?

Trimming keeps only the messages that fit within a specified token budget.

LangChain already provides utilities for this.

```python
from langchain_core.messages.utils import (
    trim_messages,
    count_tokens_approximately
)
```

---

## Code Example

```python
from langchain_core.messages.utils import (
    trim_messages,
    count_tokens_approximately
)

MAX_TOKENS = 150

def call_node(state: MessagesState):

    # Keep only the latest messages that fit within the token budget
    messages = trim_messages(
        state["messages"],
        strategy="last",
        token_counter=count_tokens_approximately,
        max_tokens=MAX_TOKENS,
    )

    print(
        "Current Token Count:",
        count_tokens_approximately(messages=messages)
    )

    for message in messages:
        print(message.content)

    response = model.invoke(messages)

    return {
        "messages": [response]
    }
```

---

## How Trimming Works

Suppose we have:

```
Conversation

M1
M2
M3
M4
M5
M6
M7
M8
M9
M10
```

Assume:

```
MAX_TOKENS = 150
```

After trimming:

```
Conversation sent to LLM

M8
M9
M10
```

Older messages are **not sent** to the LLM.

---

## Important Point

Trimming **does not delete messages from storage**.

Messages still exist in:

- PostgreSQL
- SQLite
- MemorySaver
- Any Checkpointer

They are only removed from the **prompt sent to the LLM**, not from the database.

```
Database

M1
M2
M3
...
M10

         │

         ▼

trim_messages()

         │

         ▼

Prompt

M8
M9
M10
```

---

## Advantages of Trimming

- Very fast
- No extra LLM call
- Easy to implement
- Guarantees token budget

---

## Challenge with Trimming

Trimming assumes:

> "The latest conversation is the most important."

This assumption often fails in real-world applications.

Example:

```
User:
I'm building an HR chatbot.

...

500 messages later

User:
Now add leave management.
```

After trimming:

```
User:
Now add leave management.
```

The model has forgotten that the project is an **HR chatbot**.

Important context is lost.

---

# 4. Summarization

## Why Summarization?

Instead of completely forgetting older messages, we compress them into a concise summary.

Example:

Original Conversation

```
M1
M2
M3
M4
M5
M6
M7
```

↓

Summary

```
Summary:
- User is building an HR chatbot.
- Uses LangGraph.
- PostgreSQL is used for checkpointing.
- Wants memory support.
```

Instead of sending seven messages, we send one summary.

---

## How It Works

```
Old Messages

↓

LLM generates summary

↓

Store summary

↓

Delete old messages from active state

↓

Keep recent messages
```

---

## Result

Instead of:

```
M1
M2
M3
M4
M5
M6
M7
M8
M9
```

We now have:

```
Summary of M1-M7

+

M8

M9
```

The LLM still knows what happened earlier.

---

## Advantages

- Preserves long-term context.
- Saves tokens.
- Better than forgetting old messages.

---
## Important Note
- Summarized messages get deleted from active state as we have the summarized version of it
- To remove msg from state we use the library 
> from langchain.messages import RemoveMessage

---

## Challenge

A summary is a compressed version of the conversation.

Compression always loses some details.

Example

Original

```
Use GPT-4.1 for coding.
Use Claude for reasoning.
Use Gemini for vision.
Temperature = 0.2
```

Possible Summary

```
User discussed model selection.
```

Specific details are lost.

---

# 5. Hybrid Context (Trimming + Summarization)

Most production AI systems use **both** techniques together.

Many beginners ask:

> If summarization already replaces old messages, why do we still need trimming?

The answer is:

**They solve different problems.**

---

## Trimming solves

```
Current Prompt exceeds
the token limit.
```

---

## Summarization solves

```
Don't lose
important old context.
```

---

## Hybrid Workflow

```
Entire Conversation

M1
M2
M3
...
M1000

        │

        ▼

Summarize old messages

        │

        ▼

Summary

+

Recent Messages

M971
...
M1000

        │

        ▼

trim_messages()

        │

        ▼

Final Prompt

Summary

+

Latest messages that fit the token budget

        │

        ▼

LLM
```

---

## Why Hybrid?

Imagine:

```
1000 Messages
```

Sending everything:

```
❌ Too many tokens
```

Only trimming:

```
Last 20 messages

❌ Older context is forgotten
```

Only summary:

```
Summary

❌ Recent conversation details may be missing
```

Hybrid:

```
Summary

+

Latest messages

✅ Long-term context preserved

✅ Recent details preserved

✅ Token limit maintained
```

This is why hybrid is considered the best production approach.

---

# 6. Difference: Trimming vs Summarization vs Hybrid

| Feature | Trimming | Summarization | Hybrid |
|----------|----------|---------------|---------|
| Removes old messages from prompt | ✅ | ✅ (after summarizing) | ✅ |
| Preserves old context | ❌ | ✅ | ✅ |
| Keeps recent messages | ✅ | Usually | ✅ |
| Requires an additional LLM call | ❌ | ✅ | ✅ |
| Guarantees token budget | ✅ | Not always | ✅ |
| Best for production | Small apps | Medium apps | Large production apps |

---

# 8. Key Takeaways

- **Checkpointer + thread_id** implement **Short-Term Memory (STM)** in LangGraph.
- **MessagesState** is the default state for storing conversation messages.
- Production systems commonly use **PostgreSQL Checkpointer**.
- **Trimming** only removes messages from the prompt, not from the database.
- `trim_messages()` keeps the latest messages that fit within the token budget.
- Developers should choose an appropriate `MAX_TOKENS` based on the application's needs.
- Trimming is fast but may lose important historical context.
- **Summarization** compresses older messages into a concise summary before removing them from the active state.
- Summarization preserves long-term context but may lose fine-grained details.
- **Hybrid Context (Summarization + Trimming)** combines the strengths of both approaches:
  - Summary preserves important historical information.
  - Recent messages retain detailed conversational context.
  - Trimming ensures the final prompt always fits within the model's context window.
- This hybrid approach is the preferred strategy for most production-grade AI agents built with LangGraph.
---
![long_context_solution](images_md/long_context_solution.png)

---
LTM implementation in langGraph

-  As we hvae diffierent threads of conversation 
in one user chat about tech ,in one travel , in one about some pyscology so from different treads we got some imp information about the user
such as : user is tech preson and prefer python, and will locate to mumbai soon, and believer in manifestation 
can be use this info to personalize the conversation later .. this is called the ltm long term memory

- TEchincality in langgraph
- we ahve the BaseStore in langGraph and it is abstract class
- In BaseStore we can perform action of memory such as create, edit, search, delete
- Base store is parent and clid are ImemoryStore, PostgresStore, RedisStore,

![BaseStore_langgraph](images_md/BaseStore_langgraph.png)



