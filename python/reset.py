"""Scene reset scripts."""

from typing import TYPE_CHECKING, Any
from uuid import uuid4

if TYPE_CHECKING:
    App: Any = None


def reset_uvmaps(all_uvmaps: bool = False):
    """Hacky way to reset UV maps.

    Deletes all UV maps and recreates them, runs much
    faster than welding all seams.

    Args:
        all_uvmaps: Reset all UV maps or just the current one.

    """
    current_uvmap: str = App.Get("Lib.CurrentUVSetName")
    uvmaps: [str] = App.ItemNames("Lib.UVSets")

    temp_name = str(uuid4())
    App.Uvset({"Mode": "Create", "Name": temp_name})

    App.Uvset({"Mode": "SetCurrent", "Name": temp_name})

    def process_uvmap(uvmap: str):
        App.Uvset({"Mode": "Delete", "Name": uvmap})
        App.Uvset({"Mode": "Create", "Name": uvmap})
        App.Uvset({"Mode": "SetCurrent", "Name": uvmap})
        App.ResetTo3d({"WorkingSet": "Visible", "Rescale": True})

    if not all_uvmaps:
        process_uvmap(current_uvmap)
    else:
        for uvmap in uvmaps:
            process_uvmap(uvmap)

    App.Uvset({"Mode": "SetCurrent", "Name": current_uvmap})
    App.Uvset({"Mode": "Delete", "Name": temp_name})
