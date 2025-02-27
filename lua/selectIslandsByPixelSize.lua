-- Works with Rizom 2022.0

--- Get islands by bounding box size, islands with U or V <= maxU or maxV will be selected.
-- @param maxU (number) Maximum U size in pixels.
-- @param maxV (number) Maximum V size in pixels.
local function selectIslandsByPixelSize(maxU, maxV)
	ZomSet({ Path = "Vars.EditMode.ElementMode", Value = 3 })

	local currentUVMap = ZomGet("Lib.CurrentUVSetName")
	local resolution = ZomGet("Lib.UVSets." .. currentUVMap .. ".RootGroup.TopoStable.Pack.MapResolution")
	local islands = ZomGet("Lib.Mesh.Islands")

	local islandsToSelect = {}
	for id, _ in pairs(islands) do
		local uMinus, uPlus, vMinus, vPlus = table.unpack(ZomEval("Lib.Mesh.Islands." .. id .. ".GetBBoxUVW"))

		local u = (uPlus - uMinus) * resolution
		local v = (vPlus - vMinus) * resolution

		if u <= maxU or v <= maxV then
			table.insert(islandsToSelect, tonumber(id))
		end
	end

	if #islandsToSelect == 0 then
		print("No islands meet the criteria")
		return
	end

	ZomSelect({
		PrimType = "Island",
		WorkingSet = "Visible",
		ResetBefore = true,
		Select = true,
		IDs = islandsToSelect,
		List = true,
	})
end

selectIslandsByPixelSize(3, 3)
