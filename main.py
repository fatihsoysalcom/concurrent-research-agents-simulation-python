import multiprocessing
import time
import os

def ml_research_agent(agent_id):
    """
    Simulates a machine learning research agent training a model.
    Represents one of the "multi-faceted research agents" mentioned in the article.
    """
    pid = os.getpid()
    print(f"[{time.strftime('%H:%M:%S')}] Agent {agent_id} (PID: {pid}) - ML Research: Starting model training...")
    # Simulate complex computation, e.g., training an ML model
    time.sleep(5)
    print(f"[{time.strftime('%H:%M:%S')}] Agent {agent_id} (PID: {pid}) - ML Research: Model training completed.")

def genetics_research_agent(agent_id):
    """
    Simulates a genetics research agent analyzing DNA sequences.
    """
    pid = os.getpid()
    print(f"[{time.strftime('%H:%M:%S')}] Agent {agent_id} (PID: {pid}) - Genetics Research: Starting DNA sequence analysis...")
    # Simulate data processing, e.g., genetic sequencing analysis
    time.sleep(7)
    print(f"[{time.strftime('%H:%M:%S')}] Agent {agent_id} (PID: {pid}) - Genetics Research: DNA sequence analysis completed.")

def chemistry_research_agent(agent_id):
    """
    Simulates a chemistry research agent simulating molecular interactions.
    """
    pid = os.getpid()
    print(f"[{time.strftime('%H:%M:%S')}] Agent {agent_id} (PID: {pid}) - Chemistry Research: Starting molecular simulation...")
    # Simulate scientific simulation, e.g., chemical reaction dynamics
    time.sleep(4)
    print(f"[{time.strftime('%H:%M:%S')}] Agent {agent_id} (PID: {pid}) - Chemistry Research: Molecular simulation completed.")

if __name__ == "__main__":
    print("--- OpenResearch: Concurrent Research Agents Simulation ---")
    print("This example demonstrates running multiple 'research agents' concurrently,")
    print("mimicking the 'eş zamanlı' (concurrent) and 'çok yönlü' (multi-faceted)")
    print("aspects of the OpenResearch platform described in the article.")
    print("-" * 60)

    # Define a list of research tasks to be run by different agents
    # Each tuple contains (agent_function, agent_id)
    research_tasks = [
        (ml_research_agent, 1),
        (genetics_research_agent, 2),
        (chemistry_research_agent, 3),
        (ml_research_agent, 4), # Another ML agent, demonstrating multiple agents of the same type
    ]

    processes = []
    start_time = time.monotonic()

    # Create and start a process for each research agent
    for i, (agent_func, agent_id) in enumerate(research_tasks):
        # Using multiprocessing.Process to simulate isolated environments for each agent.
        # This aligns with the article's emphasis on "güvenli ve izole bir ortamda"
        # (in a secure and isolated environment).
        p = multiprocessing.Process(target=agent_func, args=(agent_id,))
        processes.append(p)
        p.start() # Start the agent process concurrently

    print(f"\n[{time.strftime('%H:%M:%S')}] All research agents started. Waiting for them to complete...")

    # Wait for all processes (research agents) to finish
    for p in processes:
        p.join()

    end_time = time.monotonic()
    print("-" * 60)
    print(f"[{time.strftime('%H:%M:%S')}] All research agents completed in {end_time - start_time:.2f} seconds.")
    print("--- Simulation Finished ---")
