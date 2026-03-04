import gradio as gr
from assistant import ask_assistant

def chat(question):
    return ask_assistant(question)

interface = gr.Interface(
    fn=chat,
    inputs="text",
    outputs="text",
    title="AI Code Assistant",
    description="Ask coding questions in Python, Java, JavaScript, PHP, Go, Ruby"
)

interface.launch()