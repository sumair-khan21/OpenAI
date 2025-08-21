from agents import Agent
from my_config.conf import MODEL, MODEL2

math_teacher_agent = Agent(
    name="Math Teacher",
    instructions="You are a math teacher. You will help students with their math problems.",
    model=MODEL,
)


english_teacher_agent = Agent(
    name="English Teacher",
    instructions="You are an English teacher. You will help students with their English language questions.",
    model=MODEL,
)


python_teacher_agent = Agent(
    name="Python Teacher",
    instructions="You are an Python teacher. You will help students with their Python language questions.",
    model=MODEL,
)
# Add more agents as needed