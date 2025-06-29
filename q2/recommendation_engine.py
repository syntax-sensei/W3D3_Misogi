import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_agents():
    with open('agents_db.json', 'r') as f:
        return json.load(f)

def llm_prompt(task_description, agents):
    agents_descriptions = "\n".join(
        [f"### {a['name']}\nStrengths: {', '.join(a['strengths'])}\nBest For: {', '.join(a['best_for'])}\nLimitations: {', '.join(a['limitations'])}\n"
         for a in agents]
    )

    return f"""
You are an expert AI assistant helping a developer choose the best AI coding agent.

The developer gives you a coding task. You have a database of coding agents, each with their own strengths, best-use cases, and limitations.

Your job is to:
1. Understand the task.
2. Analyze which agents are most suitable.
3. Recommend the **top 3 agents** based on alignment with the task.
4. Provide a justification for each recommendation.

---

## Task:
{task_description}

---

## Available Agents:
{agents_descriptions}

---

Now, give your top 3 agent recommendations in this format:

1. [Agent Name] - [Short justification]  
2. [Agent Name] - [Short justification]  
3. [Agent Name] - [Short justification]
"""

def recommend_agents(task_description):
    agents = load_agents()
    prompt = llm_prompt(task_description, agents)

    chat_completion = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are an expert AI recommender for coding assistants."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return chat_completion.choices[0].message.content
