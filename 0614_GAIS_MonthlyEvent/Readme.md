# 🚀 Global AI Bootcamp – Prompt Engineering with LangChain

📅 **Date:** 14 June 2025  
🕙 **Time:** 10:00 AM IST  
📍 **Location:** Microsoft, Hyderabad   
🔗 **Event Link:** [Register on Meetup](https://www.meetup.com/dot-net-learners-house-hyderabad/events/308109558/?eventOrigin=group_events_list)

**Speaker:** Yashasri Gudhe  
**Topic:** **Types of Prompting & Best Practices**  
🛠️ **Live Demo:** LangChain in Action!

![GAIS Banner | 100x100](../eventbanner.jpeg) 

---

### Software/Tools

> 1. OS: Windows 10/11 x64
> 1. Python / .NET 8
> 1. Visual Studio 2022
> 1. Visual Studio Code

### Prior Knowledge

> 1. Programming knowledge in C# / Python

## Technology Stack

> 1. .NET 8, AI, Open AI

---

![Information | 100x100](../Information.png)

---

 ### What are we doing today?
1. Understanding Prompt Engineering
2. What is prompting and why it matters in AI.
3. How prompts guide reasoning and improve accuracy.
4. Real-world use cases with simple examples.

---

![Seatbelt| 100x100](../SeatBelt.png)

---

## 🧠 Session Overview

Prompting is the art of crafting clear instructions for AI models using natural language.  
It helps guide the model’s reasoning, improve accuracy, and ensure structured and relevant responses.

---

## Types of Prompting Techniques
---

## 1. Single-Turn Prompting

**Definition:**  
A basic one-shot interaction where a single prompt yields a single response.  
Useful for simple tasks without context.

**Example:**
```text
Translate "Bonjour" to English.
```

---

## 2. Zero-Shot Prompting

**Definition:**  
Ask the model to perform a task without providing any examples.  
Best for general-purpose queries the model is likely pre-trained on.

**Example:**
```text
Summarize: "Artificial intelligence is a field focused on building systems that mimic human intelligence."
```

---

## 3.Few-Shot Prompting

**Definition:**  
Provide 2–3 examples to show what kind of answer is expected.  
Helps the model learn the desired pattern.

**Example:**
```text
Q: Convert 'data science' to PascalCase  
A: DataScience  
Q: Convert 'student login' to PascalCase  
A: StudentLogin  
Q: Convert 'account settings' to PascalCase  
A:
```

**Bad Prompt:**
```text
data science -> ?
student login ->
```
**Why it's wrong:** Missing consistent format (Q/A), and ambiguous intention.

---

## 4.Multi-Turn Prompting

**Definition:**  
A conversation-like interaction with multiple back-and-forth prompts.  
Ideal for scenarios requiring memory of prior context.

**Example:**
```text
User: What's the capital of France?  
AI: Paris  
User: How far is it from Berlin?  
AI: Approximately 1,050 km by road.
User: What is the best option to reach Berlin?
```

---

## 5.Role Prompting

**Definition:**  
Assign a persona or role to guide the tone, detail, or depth of the answer.  
Useful in simulations, teaching, or reviews.

**Example:**
```text
You are a senior software engineer.  
Please review the following backend code for performance.
```

**Bad Prompt:**
```text
Review this.
```
**Why it's wrong:** No context or role – too vague.

---

## 6. Chain-of-Thought Prompting (CoT)

**Definition:**  
Encourages the model to reason step-by-step before answering.  
Improves performance on math, logic, and planning tasks.

**Example:**
```text
Q: There are 10 apples. Alice eats 4, Bob eats 2. How many are left?  
Let's think step-by-step.
```

---

## 7. Prompt Chaining

**Definition:**  
Break a large task into smaller, logically connected prompts.  
Essential for workflows, automation, and integrations.

**Example:**
```text
Step 1: Summarize the issue: "Login button doesn't work on Safari."  
Step 2: Write a bug report email with that summary.
```

---

## 8. Self-Consistency Prompting

**Definition:**  
Generate multiple reasoning paths for the same prompt, then compare to ensure consistent conclusions.  
Used to verify accuracy and uncover creative variation.

**Example:**
```text
Q: Calculate 15% of 240  
(Provide multiple ways to arrive at the answer)
```

---

## 9. Conversational Prompting (Multi-Turn Memory + Role)

**Definition:**  
A deeper version of multi-turn where the model adapts its answers based on earlier inputs and assigned role.  
Powerful for agents and virtual assistants.

**Example:**
```text
You are my shopping assistant.  
User: Add a new grocery item: 'bananas'.  
AI: Added bananas to your grocery list. Anything else?
User : Add milk and eggs
```

---

## ✅ Best Practices for Prompt Engineering

- **Be clear & specific:** Avoid vague instructions.
- **Add context/examples:** Improve quality with samples.
- **Guide reasoning:** Use "Let's think step-by-step".
- **Assign roles:** Set tone and expertise.
- **Test multiple prompts:** Find what works best.
- **Break down tasks:** Use chaining for complex flows.

---

## 🖼️ Resources for reference 
1. [Prompt Engineering Guide – Covers fundamentals, techniques, and best practices.](https://www.promptingguide.ai/)
2. [Prompt Engineering Tutorial – A beginner-friendly guide with practical examples.](https://www.tutorialspoint.com/prompt_engineering/index.html)
3. [Basic Prompt Engineering – Explains different prompting techniques with examples.](https://aiengineering.academy/PromptEngineering/Basic_Prompting/)

---

## 🙌 Acknowledgements

- **Organized by:** Global AI Secunderabad
- **Supported by:** DotNet Learners House Hyderabad  
- **Special thanks:** All participants and volunteers

---

## 🔗 Stay Connected

- [LinkedIn – Yashasri Gudhe](https://www.linkedin.com/in/gyashasri341/)
- [Global AI secunderabad](https://www.meetup.com/global-ai-secunderabad/)
- [Dot Net Learner House](https://www.meetup.com/dot-net-learners-house-hyderabad/)
- Contact: yashasrigudhe@gmail.com

---
