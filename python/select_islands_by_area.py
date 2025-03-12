"""Select islands by area."""

from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    App: Any = None


def select_islands_by_area(area: float, mode: Literal["greater", "less"]):
    """Select UV islands based on area.

    Args:
        area: Area threshold in pixels.
        mode: "greater" selects islands where area exceeds threshold.
              "less" selects islands where area is below threshold.

    """
    App.Set({"Path": "Vars.EditMode.ElementMode", "Value": 3})

    current_uvmap: str = App.Get("Lib.CurrentUVSetName")
    resolution: int = App.Get(f"Lib.UVSets.{current_uvmap}.RootGroup.Properties.Pack.MapResolution")
    islands: dict = App.Get("Lib.Mesh.Islands")

    islands_to_select = []
    for id in islands.keys():
        island_area = App.Eval("Lib.Mesh.Islands.0.GetAreaUVW")

        if mode == "greater":
            if island_area * resolution >= area:
                islands_to_select.append(int(id))
        elif mode == "less":
            if island_area * resolution <= area:
                islands_to_select.append(int(id))

    if len(islands_to_select) == 0:
        print("No islands match the criteria.")
        return

    App.Select(
        {
            "PrimType": "Island",
            "WorkingSet": "Visible",
            "ResetBefore": True,
            "Select": True,
            "IDs": islands_to_select,
            "List": True,
        }
    )
