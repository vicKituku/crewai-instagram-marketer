#!/usr/bin/env python
import sys
from instagram.crew import InstagramCrew
from datetime import datetime


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        "current_date": datetime.now(),
        "instagram_description": input("Enter the page description here"),
        "topic_of_the_week": input("Enter the topic of the week here"),
    }
    InstagramCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        InstagramCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
