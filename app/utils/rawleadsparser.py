from .. import models


def parse_meta_lead(payload: dict) -> models.RawLead:
    entry = payload["entry"][0]
    value = entry["changes"][0]["value"]

    # Flatten field_data
    field_map = {field["name"]: field["values"] for field in value["field_data"]}

    return models.RawLead(
        name = field_map["full_name"][0],
        email=field_map["email"][0],
        ph_number=field_map["phone_number"][0],
        city=field_map["city"][0],
        state=field_map["state"][0],
        brand=field_map["preferred_brand"][0],
        budget=field_map["investment_budget"][0],
        years_exp=field_map["years_of_experience"][0],
        interest=field_map["why_interested"][0],
        source=entry["platform"],
        ad_id=entry["ad_id"]
    )
