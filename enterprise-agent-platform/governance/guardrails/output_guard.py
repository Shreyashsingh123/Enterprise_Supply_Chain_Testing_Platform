def validate_report(
    report: str
):

    if not report:

        raise ValueError(
            "Empty report"
        )

    if len(report) < 50:

        raise ValueError(
            "Report too short"
        )

    if len(report) > 10000:

        raise ValueError(
            "Report too large"
        )

    return True