# TestCases/dashboard_testcases.py

DASHBOARD_TEST_CASES = {

    "TC_006": {
        "action": "dashboard_load",
        "expected": "Dashboard should load successfully"
    },

    "TC_007": {
        "action": "profile_dropdown",
        "expected": "Profile dropdown should be displayed"
    },

    "TC_008": {
        "action": "device_selection",
        "expected": "Selected device information should load"
    },

    "TC_009": {
        "action": "refresh_videos",
        "expected": "Videos should refresh successfully"
    },

    "TC_010": {
        "action": "video_summary",
        "expected": "Video Summary and all sequential hourly video ranges should be displayed correctly"
    },

    "TC_011": {
        "action": "key_metrics",
        "expected": "Key Metrics should load correctly"
    },

    "TC_012": {
        "action": "peak_hourly",
        "expected": "Peak Hourly Crowd trends summary data should display completely"
    },
    "TC_032": {
        "action": "today_filter",
        "expected": "Videos should be present until the time"
    },

    "TC_033": {
        "action": "yesterday_filter",
        "expected": "Videos should be present from 9am to 10pm"
    },

    "TC_034": {
        "action": "all_videos_filter",
        "expected": "Videos should be present according to the date"
    }
}
