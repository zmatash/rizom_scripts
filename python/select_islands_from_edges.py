"""Select islands from edges."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    App: Any = None


def select_islands_from_edges():
    """Convert a selection of edges to the containing islands."""
    islands: dict = App.Get("Lib.Mesh.Islands")
    selected_polyedge_ids: list[int] = App.Get("Lib.Mesh.SelectedPolyEdgeIDs")
    edge_ids = selected_polyedge_ids[::2]

    edge_to_island = {}
    for island_id, props in islands.items():
        for edge_id in props["PolyIDs"]:
            edge_to_island[edge_id] = int(island_id)

    islands_to_select = {edge_to_island[edge] for edge in edge_ids if edge in edge_to_island}

    App.Set({"Path": "Vars.EditMode.ElementMode", "Value": 3})
    App.Select(
        {
            "PrimType": "Island",
            "WorkingSet": "Visible",
            "ResetBefore": True,
            "Select": True,
            "IDs": list(islands_to_select),
            "List": True,
        }
    )


select_islands_from_edges()
