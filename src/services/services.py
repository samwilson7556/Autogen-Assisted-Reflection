# File: src/services/service.py

import requests  # To make HTTP requests to the external AI service

def call_external_ai_service(episode_text):
    # Mocking the external AI service call for now
    # This should be replaced with actual service call
    return {'insights': 'some insights based on {}'.format(episode_text)}

def capture_episode(episode_text):
    # Validate the input
    if not episode_text:
        raise ValueError("Episode text cannot be empty")

    # Call the external AI service to derive insights
    insights = call_external_ai_service(episode_text)

    return insights
