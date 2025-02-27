"""Select islands by pixel size.

Tested on versions:
    - Rizom 2024.1
"""

from typing import Any

App: Any = None


def select_islands_by_pixel_size(max_u: int, max_v: int):
    """Select islands whose U or V pixel width is <= the given value.

    Args:
        max_u (int): Minimum U size to select.
        max_v (int): Minimum V size to select.

    """
    current_uvmap: str = App.Get("Lib.CurrentUVSetName")
    resolution: int = App.Get(f"Lib.UVSets.{current_uvmap}.RootGroup.Properties.Pack.MapResolution")
    islands: dict = App.Get("Lib.Mesh.Islands")

    islands_to_select = []
    for id in islands.keys():
        u_minus, u_plus, v_minus, v_plus, *_ = App.Eval(f"Lib.Mesh.Islands.{id}.GetBBoxUVW")
        u = (u_plus - u_minus) * resolution
        v = (v_plus - v_minus) * resolution

        if u <= max_u or v <= max_v:
            islands_to_select.append(int(id))

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
