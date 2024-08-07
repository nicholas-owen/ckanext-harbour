import ckan.plugins.toolkit as tk
import ckanext.harbour.logic.schema as schema


@tk.side_effect_free
def harbour_get_sum(context, data_dict):
    tk.check_access(
        "harbour_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.harbour_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'harbour_get_sum': harbour_get_sum,
    }
