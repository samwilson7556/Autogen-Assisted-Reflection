# File: tests/test_services.py

import pytest
from src.services.service import capture_episode

def test_capture_episode():
    # Test with valid input
    episode_text = "Today was a productive day. I managed to finish the report and also had a great workout."
    insights = capture_episode(episode_text)
    assert 'insights' in insights, f'Expected insights in the result, but got {insights}'

    # Test with empty input
    with pytest.raises(ValueError):
        capture_episode("")

