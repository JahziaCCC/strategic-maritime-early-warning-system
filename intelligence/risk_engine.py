def calculate_risk(
    vessel_density,
    abnormal_movements,
    stopped_vessels,
    security_events
):
    score = 0

    # كثافة السفن
    score += vessel_density * 0.25

    # تغيرات غير طبيعية
    score += abnormal_movements * 10

    # سفن متوقفة
    score += stopped_vessels * 5

    # أحداث أمنية
    score += security_events * 15

    # الحد الأعلى
    if score > 100:
        score = 100

    return round(score)


def risk_level(score):

    if score < 30:
        return "LOW"

    elif score < 70:
        return "MEDIUM"

    else:
        return "HIGH"
