---
doc: learner-profile
---
<!-- Capture only context later skills can use. Keep it scannable and short, not a transcript.
     Record what the learner shared or demonstrated, with brief evidence where useful.
     Don't infer beyond the evidence or assign fixed labels. "Not established" is useful.
     Optional sections need not be filled; don't turn this template into a questionnaire. -->

# Learner Profile

## Initial Idea
A web app for medical physics students that calculates photon attenuation. The user picks a material (water, air, lead, bone), a photon energy (keV/MeV), and a thickness. The app shows the transmitted fraction, the HVL and TVL, and plots the attenuation curve (I = I₀ × e^(-μx)) using NIST XCOM data. Intended users: medical physics students. Motivation: a portfolio project for a first job in AI/LLMs that demonstrates both domain knowledge and the ability to build a working web tool.

## Demonstrated Technical and Agent Experience
Medical physics student at UNSAM. Learning Python, data science, and AI/LLMs. Has a basic ML certificate from Kaggle plus Anthropic's "Claude 101" and "AI Fluency" certifications. Has used Claude in chat mode but this is their first time using a coding agent (Claude Code) inside a repository. Evidence: "I've used Claude in chat, but this is my first time using a coding agent like Claude Code inside a repository."

## Planning-Workflow Experience
New. Has never written a PRD or technical spec, and hasn't done spec-driven development before. Evidence: "I haven't done spec-driven development before: I've never written a PRD or a technical spec."

## Desired Learning Outcome
Learn how to work with AI in a structured, plan-first workflow so they can build projects they can actually explain. Use this as a portfolio project for a first job in AI/LLMs. Understand the code the agent writes, not just copy it.

## Learning Moments
(To be populated during the project)

## Interests, Inspirations, and Goals
- Medical physics background — wants to apply domain knowledge
- Portfolio project for first AI/LLM job
- Wants to understand the generated code, not just have it work
- Outside coding: medical physics studies at UNSAM

## Vocabulary and Concepts Likely to Need Explanation
- Coding agent workflows in a repository (first time using Claude Code in a repo)
- Plan-first / spec-driven development terms: PRD, spec, scope, proof of concept
- Web app architecture basics (frontend/backend, framework choices, deployment)
- NIST XCOM data access and interpolation
- HVL (Half-Value Layer) and TVL (Tenth-Value Layer) calculations
- Attenuation curve plotting libraries

## Collaboration and Communication Preferences
Guided explanations (explain tools and decisions in simple terms). One question at a time preferred — new to planning workflow.

## Areas Where the Learner Wants Ownership
- Project idea and scope decisions (medical physics domain)
- Technology choices with explanation of tradeoffs
- Understanding and explaining the generated code

## Likely Support Needs
- Walkthrough of each planning artifact (scope, PRD, spec) before moving on
- Clear explanations of agent workflow and tool use at each step
- Code explanations in accessible language, not jargon
- Help with NIST XCOM data access strategy
- Portfolio-ready project structure guidance

## Review Format

markdown

## Notes and Open Questions
- NIST XCOM data: will need a strategy (download CSV, API, or embed pre-computed tables)
- Framework choice: Streamlit? Flask + HTML/JS? React? — explain tradeoffs
- Deployment target: local only, or shareable (GitHub Pages, Streamlit Cloud, etc.)
- Keep scope small enough for an afternoon build as stated