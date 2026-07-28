# AI Vedic Astrology Assistant (RAG + AI Agent)

## Project Overview

Build an AI-powered Vedic Astrology Assistant that generates personalized astrology readings based on a user's birth details.

Unlike a normal chatbot, this system does **not** rely on the LLM to calculate astrology. Instead, it follows the same workflow as a real astrologer.

The project combines:

- FastAPI
- LangGraph
- RAG
- ChromaDB
- LLM
- Vedic Astrology Engine (Swiss Ephemeris / Flatlib)
- Prompt Engineering

---

# Goal

User provides:

- Date of Birth
- Time of Birth
- Place of Birth

The assistant should answer questions like:

- Tell me about my personality.
- What kind of career suits me?
- What are my strengths?
- What are my weaknesses?
- How is my marriage life?
- What are my financial prospects?
- Which Mahadasha am I currently in?
- What remedies should I follow?
- Which gemstone is recommended?
- Which mantra should I chant?
- Which deity should I worship?
- Which planet is weak in my horoscope?

The assistant should always explain **why** it reached a conclusion and reference the astrology knowledge used.

---

# Important Principle

❌ Do NOT let the LLM calculate astrology.

LLMs hallucinate planetary positions.

Instead,

Use deterministic software to calculate the horoscope.

Use the LLM only for interpretation.

---

# High Level Architecture

```
                 User

                   │

                   ▼

        Birth Details Input

      DOB + Time + Place

                   │

                   ▼

      Astrology Calculation Engine

      (Swiss Ephemeris / Flatlib)

                   │

                   ▼

          Birth Chart JSON

                   │

        ┌──────────┴───────────┐

        │                      │

        ▼                      ▼

 Astrology Knowledge      User Question

     (Vector DB)

        │                      │

        └──────────┬───────────┘

                   ▼

             Retriever (RAG)

                   │

                   ▼

          Retrieved Context

                   │

                   ▼

                 LLM

                   │

                   ▼

         Personalized Answer
```

---

# Tech Stack

Backend

- FastAPI

AI Framework

- LangGraph

LLM

- OpenAI / OpenRouter / Claude

Vector Database

- ChromaDB

Embeddings

- BAAI bge-small
- OpenAI Embeddings
- Nomic

Document Loader

- LangChain

Astrology Engine

- Swiss Ephemeris (Recommended)
- Flatlib

Database

- PostgreSQL

Cache

- Redis

---

# System Workflow

## Step 1

User enters

```
Date of Birth

Time of Birth

Birth Place
```

Example

```
06 April 1992

10:30 AM

Lucknow, India
```

---

## Step 2

Convert place into

```
Latitude

Longitude

Timezone
```

using

- Nominatim
- Google Maps API
- GeoPy

---

## Step 3

Generate Birth Chart

Using

Swiss Ephemeris

Output

```json
{
    "ascendant": "Gemini",
    "sun": "Aries",
    "moon": "Cancer",
    "mars": "Virgo",
    "mercury": "Pisces",
    "venus": "Taurus",
    "saturn": "Aquarius",
    "jupiter": "Libra",
    "rahu": "...",
    "ketu": "...",
    "nakshatra": "...",
    "mahadasha": "..."
}
```

---

## Step 4

User asks

```
How is my career?
```

---

## Step 5

Retriever creates search query

Instead of searching

```
Career
```

search using

```
Gemini Ascendant

Career

Jupiter in 10th House

Saturn

Profession

Raj Yoga
```

This produces much more accurate retrieval.

---

## Step 6

Retriever fetches

Relevant chapters from

- Brihat Parashara Hora Shastra
- Phaladeepika
- Saravali
- Jataka Parijata

---

## Step 7

Prompt

```
You are an experienced Vedic astrologer.

The birth chart has already been calculated.

Never invent planetary positions.

Interpret only using the retrieved context.

If information is unavailable,
say so instead of guessing.
```

---

## Step 8

LLM generates

```
Your Jupiter occupies...

According to Brihat Parashara Hora Shastra...

This indicates...

Recommended Remedies

Reason
```

---

# Knowledge Base

Recommended Books

⭐⭐⭐⭐⭐

- Brihat Parashara Hora Shastra

⭐⭐⭐⭐⭐

- Phaladeepika

⭐⭐⭐⭐

- Saravali

⭐⭐⭐⭐

- Jataka Parijata

⭐⭐⭐⭐

- Brihat Jataka

Optional

- Bhagavad Gita
- Lal Kitab
- Upanishads
- Yoga Sutras

---

# RAG Pipeline

```
PDF

↓

Loader

↓

Chunking

↓

Embeddings

↓

Vector DB

↓

Retriever

↓

Relevant Chunks

↓

LLM
```

---

# LangGraph Workflow

```
User

↓

Validate Input

↓

Generate Birth Chart

↓

Retrieve Knowledge

↓

LLM Interpretation

↓

Return Response
```

Future enhancement

```
          User

            │

            ▼

      Birth Chart Tool

            │

            ▼

      RAG Retriever

            │

            ▼

      Web Search Tool

            │

            ▼

      Remedy Generator

            │

            ▼

      Final Answer
```

---

# Future MCP Integration

Possible MCP Servers

- Calculator MCP
- Web Search MCP
- File System MCP
- PostgreSQL MCP

Example

```
User

↓

Birth Chart Tool

↓

Parallel Search MCP

↓

Retrieve Latest Remedy Research

↓

LLM
```

---

# Example Conversation

User

```
My DOB is

6 April 1992

10:30 AM

Lucknow

Tell me about my personality.
```

System

```
1. Calculate Horoscope

↓

2. Retrieve Relevant Chapters

↓

3. Interpret Chart

↓

4. Generate Response
```

Assistant

```
You have a Gemini Ascendant...

Mercury is...

According to Brihat Parashara Hora Shastra...

Your communication skills are...

Strengths

Weaknesses

Career

Remedies
```

---

# Possible Features

## Personality Analysis

- Strengths
- Weaknesses
- Emotional Nature

---

## Career

- Best Career
- Government Job
- Business
- Foreign Opportunities

---

## Marriage

- Marriage Timing
- Compatibility
- Love Marriage
- Arranged Marriage

---

## Finance

- Wealth
- Investments
- Property

---

## Health

- Weak Areas
- Planetary Effects

---

## Dasha

- Current Mahadasha
- Upcoming Mahadasha

---

## Remedies

- Mantras
- Gemstones
- Charity
- Fasting
- Temple Visits
- Deity Worship

---

## Lucky Information

- Lucky Color
- Lucky Number
- Lucky Day

---

# Phase-wise Implementation Plan

## Phase 1

✅ Build RAG

- PDF Loader
- Chunking
- ChromaDB
- Querying

---

## Phase 2

✅ Integrate Astrology Engine

- Swiss Ephemeris
- Birth Chart Generation

---

## Phase 3

✅ Connect RAG + Horoscope

Retrieve context using chart details.

---

## Phase 4

✅ Build LangGraph Agent

Nodes

- Input Validation
- Horoscope Generator
- Retriever
- LLM
- Output Formatter

---

## Phase 5

✅ FastAPI Backend

Endpoints

- Generate Chart
- Ask Question
- Get Remedies
- Chat History

---

## Phase 6

✅ Frontend

- Chat Interface
- Kundli Form
- Conversation History

---

# Key AI Engineering Principle

Use deterministic software for calculations.

Use the LLM for reasoning and interpretation.

This hybrid approach produces significantly more reliable results than asking an LLM to calculate astrology directly.