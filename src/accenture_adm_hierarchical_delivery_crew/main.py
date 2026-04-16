#!/usr/bin/env python
import sys
from accenture_adm_hierarchical_delivery_crew.crew import AccentureAdmHierarchicalDeliveryCrew


def get_inputs() -> dict:
    """Gather crew inputs from CLI args or defaults."""
    if len(sys.argv) >= 4:
        return {
            "engagement_type": sys.argv[2],
            "client_name": sys.argv[3],
        }
    engagement_type = input("Engagement type: ").strip() or "Digital Transformation - Cloud-Native POS Modernization"
    client_name = input("Client name: ").strip() or "NovaMart"
    return {
        "engagement_type": engagement_type,
        "client_name": client_name,
    }


def run():
    """Run the crew."""
    inputs = get_inputs()
    AccentureAdmHierarchicalDeliveryCrew().crew().kickoff(inputs=inputs)


def train():
    """Train the crew for a given number of iterations."""
    inputs = get_inputs()
    try:
        AccentureAdmHierarchicalDeliveryCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs,
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """Replay the crew execution from a specific task."""
    try:
        AccentureAdmHierarchicalDeliveryCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """Test the crew execution and returns the results."""
    inputs = get_inputs()
    try:
        AccentureAdmHierarchicalDeliveryCrew().crew().test(
            n_iterations=int(sys.argv[1]),
            openai_model_name=sys.argv[2],
            inputs=inputs,
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
