def calculate_risk_score(cve_list):
    num_cves = len(cve_list)

    if num_cves == 0:
        return 10, "Low"
    elif num_cves <= 3:
        return 40, "Medium"
    elif num_cves <= 6:
        return 70, "High"
    else:
        return 90, "Critical"
