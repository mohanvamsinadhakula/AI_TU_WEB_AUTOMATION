# Testcases/device_stats_testcase.py

DEVICE_STATS_TEST_CASES = {

    "TC_017": {
        "module": "Device Stats",
        "description": "Verify Device Stats page navigation",
        "action": "device_stats_navigation",
        "expected": "Device Stats page should open successfully."
    },

    "TC_018": {
        "module": "Device Stats",
        "description": "Verify 1 Day filter",
        "action": "one_day_filter",
        "expected": "One-day statistics should be displayed with correct graph."
    },

    "TC_019": {
        "module": "Device Stats",
        "description": "Verify 7 Days filter",
        "action": "seven_days_filter",
        "expected": "Seven-day statistics should be displayed with correct graph."
    },

    "TC_020": {
        "module": "Device Stats",
        "description": "Verify 30 Days filter",
        "action": "thirty_days_filter",
        "expected": "Thirty-day statistics should be displayed with correct graph."
    },

    "TC_021": {
        "module": "Device Stats",
        "description": "Verify Refresh functionality",
        "action": "refresh",
        "expected": "Statistics should refresh successfully."
    }

}