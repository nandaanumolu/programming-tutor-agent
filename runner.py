from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from agent import root_agent

# Create a runner for the agent
runner = Runner(
    app_name="programming-tutor-app",
    agent=root_agent,
    session_service=InMemorySessionService()
)

if __name__ == "__main__":
    # You can add code here to test the agent's functionality
    print("Programming Tutor Agent is ready to run.")
    print("To start the agent, you would typically use the ADK CLI.")
