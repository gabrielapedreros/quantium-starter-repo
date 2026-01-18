import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app import app

"""
Task 5
Testing presence of elements
import app: from app import app
1. start app
2. wait for the element to exist (wait_for_element)
3. assert no JS errors

"""

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#page-title", timeout=4)
    assert dash_duo.find_element("#page-title").text == "Sales Over Time of Pink Morsels"
    assert dash_duo.get_logs() == [], "browser console should contain no errors"


def test_graph_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-graph", timeout=4)
    assert dash_duo.get_logs() == [], "browser console should contain no errors"


def test_region_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=4)
    assert dash_duo.get_logs() == [], "browser console should contain no errors"