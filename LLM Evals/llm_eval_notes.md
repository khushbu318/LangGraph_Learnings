- Why llm evaluation is imp

1. Vibe Testing
vibe testing means causally trying an llm app with a few prompts and judging it by feel.

Basically: i asked it 5 - 10 questions, the answers looked good so i think it work.

it is informal, subjectino and usually not repeatable

and it only works at a personal project level !

-- The evaluation is important
but why don't people test their LLM applications? 
Because it's not straight forward !

- Software testing vs LLm Evals

deterministic | non deterministic
correctness | rag answer  eval dimensions : factuality, completeness, cruality, grounded ness, latency, cost and this dimension vary as per the use case and company

---
llm eval vs llm application eval

rag evals 

agent evals

safety evals

operation evals

--- 
what are llm Eval ?
LLm evals are systematic repeatable tests use to judge an llm or llm - powered system against a clear criteria

systematic
- instead of askign 5 question casually  and 'looks good', we create planned test cases.

for example: 
- 100 real studednt dougs for a any course assistant

--
repeatable 

The same eval should be runnable again

if we change the prompt, model, retriever, chunking strategy or system instructin, we shuold be able to run the same test again and compare results.

this is how we know whether the system improved or became worse.

--
clear criteria

we must define what good means.

for example: 

---
An eval is not just a metric. An eval is the complete testing setup. it includes

1. What are we evaluating ?
2. what does good means ?
3. what test cases are we using ?
4. How are we judging the output ?
5. When are we running it ?
6. which tool are we using ?

we are talking about the complete process fo testing an LLM-powered system in a structure way. 

the goal is not just to get a score. The goal is to answer practical questions like:

- can the model be user for a particular tast/application ?
- is this system good enough to ship ?
- did prompt v2 improve over prompt v1 
- is the RAG answer grounded in the retrieval context ?
- is the agent completing the task correctly ?
- is the chatbot safe for real users ?
- is the latency under control ?

-- LLM Eval
 
1. Model Evals

model evals evaluate the model itself. The main idat is to test and evaluate the capabilities of model

some imp cababilities include : 
1. Reasoning ? can it reason
2. Knowledge ? can it answer knowledge based question
3. Maths ? can it solve maths problems
4. coding ? can it write code
5. instruction following
6. Long Context ? can it follow long document
7. Multimodal understanding ? can it understand images 
8. Tool - use ? can it use tools

-- llm leader boards / bench mark

-- note: create the table of famous capability area, bench mark name, what it checks

--- Ai eng don't do llm evals as it is done by frontier labs 
- as we know the model evals , bench mark of the llm we can take better dicitions 

----------
Application evals 

includesl: 
user interface
input handler
output parcred
tools/ api
prompt layer
orchestrator/ workflow
guardrails / safety
output parser
llm / model
context/ memory
embedding model
retrieval system
vector database
monitoring/ logging
feedback loop
chunking stragy

![llm_app_eval](/images_md/llm_app_eval.png)

analogy is Smartphones

- Appliction evals asses the behavioru and performand of an llm-powered application, whether at the level of the entire system or a specific componenet within it. 

---

llm aplication eval workflow

- One llm based application have several llm evals

![llm_app_eval_flow](/images_md/llm_app_eval_flow.png)
