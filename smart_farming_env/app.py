import gradio as gr
import requests
import plotly.graph_objects as go

URL = "http://127.0.0.1:8000"  # local API

history = {
    "soil": [],
    "water": [],
    "profit": []
}

def reset_env():
    res = requests.get(f"{URL}/reset").json()
    history["soil"].clear()
    history["water"].clear()
    history["profit"].clear()
    return res, create_chart()

def get_state():
    res = requests.get(f"{URL}/state").json()
    update_history(res)
    return res, create_chart()

def take_action(action):
    res = requests.get(f"{URL}/step/{action}").json()
    update_history(res["state"])
    return res, create_chart()

def update_history(state):
    history["soil"].append(state["soil"])
    history["water"].append(state["water"])
    history["profit"].append(state["profit"])

def create_chart():
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=history["soil"], mode='lines', name='🌱 Soil'))
    fig.add_trace(go.Scatter(y=history["water"], mode='lines', name='💧 Water'))
    fig.add_trace(go.Scatter(y=history["profit"], mode='lines', name='💰 Profit'))

    fig.update_layout(
        title="📈 Farm Performance",
        template="plotly_dark",
        height=400
    )
    return fig

with gr.Blocks() as demo:

    gr.Markdown("""
    # 🌾 Smart Farming AI Dashboard
    ### 🚀 Monitor and control your farm intelligently
    """)

    with gr.Row():
        reset_btn = gr.Button("🔄 Reset", variant="primary")
        state_btn = gr.Button("📊 Get State")

    output = gr.JSON(label="📦 System Output")
    chart = gr.Plot()

    reset_btn.click(reset_env, outputs=[output, chart])
    state_btn.click(get_state, outputs=[output, chart])

    gr.Markdown("## 🌱 Perform Action")

    action = gr.Radio(
        ["irrigate", "fertilize", "harvest"],
        label="Choose Action"
    )

    action_btn = gr.Button("▶️ Execute Action", variant="primary")

    action_btn.click(take_action, inputs=action, outputs=[output, chart])

    gr.Markdown("### 💡 Tips:")
    gr.Markdown("""
    - 💧 Irrigate when water is low  
    - 🌱 Fertilize for better soil  
    - 🌾 Harvest at the right time for profit  
    """)

demo.launch(theme=gr.themes.Soft())