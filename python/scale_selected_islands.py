"""Island scaling script."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    App: Any = None


def scale_selected_islands(scaling_factor: float):
    """Add scaling factor to selected islands.

    Args:
        scaling_factor: Scaling factor to set to each island."

    """
    islands: dict = App.Get("Lib.Mesh.Islands")
    selected_island_ids = [
        int(id) for id in islands.keys() if islands[id]["Properties"]["Selected"]
    ]

    App.IslandProperties(
        {
            "IslandIDs": selected_island_ids,
            "Properties": {"Pack": {"Scaling": {"Factor": scaling_factor}}},
        }
    )


scale_selected_islands(2.5)
