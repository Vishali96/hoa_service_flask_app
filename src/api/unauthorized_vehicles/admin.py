from flask_admin.contrib.sqla import ModelView

class UnauthorizedVehiclesAdminView(ModelView):
    column_searchable_list = (
        "vehicle",
        "license",
    )
    column_editable_list = (
        "vehicle",
        "license",
        "created_date"
    )
    column_filters = (
        "vehicle",
        "license"
    )
    column_sortable_list = (
        "vehicle",
        "license"
    )
    column_default_sort = ("created_date", True)
