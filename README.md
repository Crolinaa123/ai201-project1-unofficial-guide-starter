# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
- It covers teacher evalutaions and course recommendeations. 
     Why is this knowledge valuable, and why is it hard to find through official channels?
     - This knowledge is valuable because it will help students choose the right professor and courses, aiding them to succeed in the long run. This information may be hard to find in the official channels because they might not be as honest in terms of critiques. 
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | Rate my professor | Zumrat's rating | https://www.ratemyprofessors.com/professor/2829445|
| 2 | Rate my professor | Sandeep's rating| - https://www.ratemyprofessors.com/professor/2233896 |
| 3 | Rate my professor | Jacek's rating | https://www.ratemyprofessors.com/professor/2892587|
| 4 | Rate my professor | Bonelli's rating | https://www.ratemyprofessors.com/professor/2113255|
| 5 | Rate my professor| Dimitry's rating| https://www.ratemyprofessors.com/professor/3041210 |
| 6 | Reddit | "How is Shudong Hao for CS 382" |https://www.reddit.com/r/stevens/comments/1rl1aik/how_is_shudong_hao_for_cs_382/ |
| 7 | Reddit | "CS course advice" | https://www.reddit.com/r/stevens/comments/zw25al/cs_course_advice/|
| 8 | Reddit| "Good minor classes for cs" | https://www.reddit.com/r/stevens/comments/1icm4xo/good_minor_classes_for_cs/|
| 9| Reddit | "How are the professor for math and cs"| https://www.reddit.com/r/stevens/comments/1sc2s2h/how_are_the_professors_for_maths_and_cs/ |
| 10| Reddit | "Would you recommed going to stevens for cs" | https://www.reddit.com/r/stevens/comments/unp3nx/would_you_recommend_going_to_stevens_for_a_cs/ |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:150 - 400**

**Overlap:50 characters**

**Why these choices fit your documents:**

**Final chunk count:Because each review is its own complete thought, and it doesn't continue into the next review. So there's no risk of a key idea being split across two chunks.**

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:all-MiniLM-L6-v2**

**Production tradeoff reflection:A general model might not understand certain terms, such as, "curved the exam", or couse code like "CS 392". A model that is aware or is trained on such specificity would be more accurate and efficient, however it would be more difficult to find and costly.**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:Answer the questino using ONLY the information in the provided documents. If the documents don't contain enough information to answer, say "I don't have enough information on that". Always cite which source(s) your answer comes from.**

**How source attribution is surfaced in the response:The source filenames are retrieved form ChromaDB metadata alongside each chunk.After generation, the unique source filenames are collected and displayes in a seperate "Retrieved from" field in the Gradio interface, so users can always see which documents the answer drew from.**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | Is Professor Zumrut a good professor? | Yes, she has a fun personality, and is very engaging with her lectures and dosen't overcomplicate complex topics. | Professor Zumrut is described as "a very nice professor" who "knows a lot about Python" and "encourages her students to ask questions". However, she can be a bit fast-paced. | Relevant | Accurate |
| 2 | Is CS496 a hard course? | It can get quite diffcult, since it consists of complex topics.| CS496 is described as a "difficult class" but manageable with effort and studying, according to rmp_prof4.txt and Reddit sources. |Relevant| Accurate|
| 3 |What do students say about internship opportunities for Stevens CS students? | Stevens is a small, expensive school near NYC with strong CS internship oppurtunities and a motivated student body; location is its biggest advantage. | There are plenty of internship oppurtunites pipelined through university programs and though the school's location in the NYC area. |Relevant|Accurate |
| 4 | Does Professor Ossowski give hard exams?|His exams can be tough, but he does tend to curve if needed and if you pay attention to his lectures and follow along, you should be in good shape. | I don't have information on that. |Off-target, because the user used "Ossowski" but all sources refer to him as "Jacek".| Inaccurate|
| 5 |  Is Sandeep a bad professor?|Students consistently rate CS334 are extremely difficult with unfair grading, for instance, exams and problem sets are extremely difficult, TAs can grade quite harshly, and most recommended taking Jacek instead for a better grade and less stress. | The system says it dosen't have enough infomration, noting only mention of Sandeep stating that the class seemed focused on proving how smart he is rather than teaching.| Partially good | Parially accurate|

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed: Does Professor Ossowski give out hard exams?**

**What the system returned: I don't have enough information on that. There is no mention of a Professor Ossowski in the provided documents. The documents only discuss Professors Bonelli, Jacek, and Paramanov, as well as an unnamed professor and Professor Sandeep.**

**Root cause (tied to a specific pipeline stage): The root cause ties to the retrieval stage because the embedding model couldn't match "Ossowski" to "Jacek" because the documents only use his first name.**

**What you would change to fix it: I would include a prompt stating that whenever a query mentions Professor Ossowski, it can also be reffered as Jacek since most student refer to his first name in the reviews.**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation: It helped me build my model step by step without feeling rushed. I was able to understand what I was doing at each step thoroughly and it helped me backtrack if I found myself stuck.**

**One way your implementation diverged from the spec, and why: In the spec, I set the chunk size to 200-400, but I ended up splitting by blank lines instead. This is because splitting by blank line preserved each review as a complete sentence, instead of cutting them off mid-sentence.**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI: My chunking strategy section from plannning.md and a sample RMP review*
- *What it produced: A chunk_text() function that split text by fixed character count (300 characters with 50 overlap)*
- *What I changed or overrode: The character-based splitting was cutting reviews-mid sentence, so I changed it to be split by blank lines instead.*

**Instance 2**

- *What I gave the AI: My retrieval approack section and pipeline diagram from planning.md*
- *What it produced: the full embedder.py script with sentence-transformers.*
- *What I changed or overrode: I tested the retrieval and adjusted top-k from  to 6-7 after seeing that relevant chunks were being missed with a lower k-value.*
