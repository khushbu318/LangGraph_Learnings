# RAG Testing Questions - The 4-Hour Workweek

## Level 1 - Basic Retrieval

- What is the main idea of The 4-Hour Workweek?What is the main idea of The 4-Hour Workweek?
- Who is the author of the book?
- What problem is the book trying to solve?
- What does the author say about the traditional 9-to-5 job?
- What are the key principles discussed in the book?
- Summarize Chapter 1.
- Summarize the conclusion of the book.

---

## Level 2 - Chapter Specific

- What is explained in Chapter 3?
- What does the author teach in Chapter 5?
- What are the important lessons from Chapter 8?
- Give a summary of Chapter 10.
- Which chapter discusses outsourcing?
- Which chapter explains automation?
- Which chapter talks about retirement?

---

## Level 3 - Concept Retrieval

- What is the DEAL framework?
- Explain the D in DEAL.
- Explain the E in DEAL.
- Explain the A in DEAL.
- Explain the L in DEAL.
- What does lifestyle design mean?
- What is the New Rich (NR)?
- What is selective ignorance?
- What is Parkinson's Law?
- What is the 80/20 Principle according to the author?
- What is the Low Information Diet?
- What is fear-setting?
- What does the author say about perfectionism?
- What is the author's opinion on productivity?
- How does the author define effectiveness?

---

## Level 4 - Exact Information

- What are the steps of fear-setting?
- List the rules of the Low Information Diet.
- What are the questions used in dreamlining?
- What are the examples of outsourcing mentioned in the book?
- According to the book, what tasks should be outsourced?
- What tools does the author recommend?
- What websites are mentioned for hiring virtual assistants?
- Which email automation examples are given?
- What companies or services are recommended in the book?

---

## Level 5 - Multi-hop Retrieval

- Explain the relationship between the 80/20 Principle and outsourcing.
- How does the author combine automation with delegation?
- How does dreamlining relate to lifestyle design?
- Explain the complete DEAL framework with examples.
- What are the author's recommendations for escaping the 9-to-5 lifestyle?
- How can someone use automation together with virtual assistants?

---

## Level 6 - Quote Retrieval

- Find a quote about productivity.
- Find a quote about fear.
- Find a quote about time management.
- Find a quote about retirement.
- Find a quote related to taking action.
- Quote the author's advice about being busy versus being productive.

---

## Level 7 - Fact Verification

- Does the author recommend quitting your job immediately?
- Does the author support multitasking?
- Does the author recommend checking email constantly?
- Does the author encourage outsourcing personal work?
- Does the author believe retirement should happen at age 65?

---

## Level 8 - Retrieval with Reasoning

- I work 10 hours a day. Which chapters should I read first?
- I want to start a side business. Which concepts from the book are most relevant?
- I procrastinate a lot. What advice does the book give?
- I spend too much time checking emails. What does the author recommend?
- I want more free time. Which techniques from the book should I apply?
- How would the author advise a software engineer who is overworked?

---

## Level 9 - Edge Cases (Hallucination Tests)

- What is the author's opinion on cryptocurrency?
- What does the book say about ChatGPT?
- Which chapter explains LangGraph?
- What does the author think about AI agents?
- What is the author's advice for using Kubernetes?
- What does the book say about Docker containers?

Expected behavior:
The bot should answer that this information is not present in the book instead of making up an answer.

---

## Level 10 - Citation Tests

- From which chapter is the DEAL framework explained?
- Which page explains Parkinson's Law?
- Which chapter discusses outsourcing?
- Where is the Low Information Diet explained?
- Show the source for your answer.
- Quote the paragraph where the author introduces Dreamlining.

---

## Stress Tests

- Explain the DEAL framework in less than 100 words.
- Summarize the entire book in one paragraph.
- Explain the book as if I am a 10-year-old.
- Give five actionable lessons from the book.
- Compare the beginning and ending chapters.
- Which chapter would you recommend reading first and why?
- What are the top 10 takeaways from the book?

---

## RAG Quality Checklist

For every answer, verify:

- ✅ Retrieved the correct document chunks
- ✅ Answer matches the retrieved context
- ✅ No hallucinations
- ✅ Correct citations (if implemented)
- ✅ Good semantic retrieval
- ✅ Handles "information not found" correctly
- ✅ Doesn't answer from LLM knowledge when context is missing
- ✅ Uses multiple chunks when necessary
- ✅ Produces concise yet complete answers