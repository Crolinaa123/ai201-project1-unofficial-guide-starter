# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
> course and professor reviews 
> Knowing what a professor is like and what a course covers before the semester starts helps students come in prepared. Without this information, students risk falling behind, either because a professor is hard to follow, the coursework is more demanding than expected, or the course structure doesn't match their learning style.
---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------| 
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

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size: 150 - 400**

**Overlap: 50 characters**

**Reasoning: Because each review is its own complete thought, and it doesn't continue into the next review. So there's no risk of a key idea being split across two chunks.**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model: all-MiniLM-L6-v2**

**Top-k: 7**

**Production tradeoff reflection: A general model might not understand certain terms, such as, "curved the exam", or couse code like "CS 392". A model that is aware or is trained on such specificity would be more accurate and efficient, however it would be more difficult to find and costly.**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | Is Professor Zumrat a good professor?| Yes, she has a fun personality, and is very engaging with her lectures and dosen't overcomplicate complex topics.|
| 2 | Does Professor Jacek give out hard exams?| His exams can be tough, but he does tend to curve if needed and if you pay attention to his lectures and follow along, you should be in good shape.|
| 3 | Is CS496 a hard course? | It can get quite diffcult, since it consists of complex topics. However, Professor Bonelli is a great lecturer, and is available whenever you have any questions.|
| 4 | What do students say about internship opportunities for Stevens CS students? | Stevens is a small, expensive school near NYC with strong CS internship oppurtunities and a motivated student body; location is its biggest advantage. |
| 5 | Is Sandeep a bad professor? | Students consistently rate CS334 are extremely difficult with unfair grading, for instance, exams and problem sets are extremely difficult, TAs can grade quite harshly, and most recommended taking Jacek instead for a better grade and less stress. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. A student might ask more about the course content, rather than the professor. However, the source may only contain reviews regarding the professor. 

2. Reddit threads might go off-topic and can get quite messy. This can confuse the AI model leading to misleading results. 

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

     [Document Ingestion] --> [Chunking] --> [Embedding] --> [Vector Store] --> [Retrieval] --> [Generation]
     (Python)             (Python)    (sentence-        (ChromaDB)        (ChromaDB)      (Groq/
                                      transformers)                                       llama-3.3)

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

     Document Ingestion: I'll use Claude, give it my Documents sections from planning.md, and ask it to write an ingest_documents() functions that fetches the content from each URL using BeautifulSoup and saves it to a file. I'll verify it by running it on one URL and checking that the output text matches what is visible on the page. 
     Chunking: I'll use Claude and give it information from my Chunking strategy section and ask it to implement a function, chunk_text() function according to specific size and overlap. I'll verify it by running it on one RMP review and checking that each chunk contains only one review. 
     Embedding: I'll use Claude and using my Retrival Approach sections, and I will ask it write a embed_chucks() function that takes the text chunks and converts them into vectors. I'll verify it by checking that the function returns a list of vectors with teh same length as my list of chunks. 
     Vector Store: I'll use Claude for to implement a store_embeddings() functions that takes my vectors and store them in ChromaDB. I'll verify using ChromaDB after storing and checking tha tthe chunks can be retrieved. 
     Retrieval: I'll use Calude to implement a retrieve_chunks() function based on the Retrieval Approach section that takes a user input, converts it to a vector and searches ChromaDB for the top 6-7 most similar chunks. I'll verify it by runnign a test query and checking that the returned chunks are actually relevant to the question.
     Generation: I'll use Claude to implement a function generate_response() function that take the retrieved chunks and user query, sends them to Groq model, and returns a specific answers based on the user input. I'll verify by running one of my  questions and checking the the answer is accurate based on the sources. 



**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
