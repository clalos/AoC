-- moveSeeds moves seeds according to the map
local function moveSeeds(seeds, map)
    local seedsMoved = {}
    for _, instr in ipairs(map) do
        for k, seed in ipairs(seeds) do
            if not seedsMoved[k] and instr.source + instr.length > seed and instr.source <= seed then
                seeds[k] = instr.dest + (seed - instr.source)
                seedsMoved[k] = true
            end
        end
    end
end

-- read input
local isMap, seeds, map = false, {}, {}
for line in io.lines("input.txt") do
    if line:find("seeds") then
        for s in line:gmatch("%d+") do
            table.insert(seeds, tonumber(s))
        end
    end
    if isMap and line ~= "" then
        local dest, source, length = line:match("(%d+) (%d+) (%d+)")
        table.insert(map, { dest = tonumber(dest), source = tonumber(source), length = tonumber(length) })
    end
    if line:find("map") then
        isMap = true
    end
    if line == "" then
        moveSeeds(seeds, map)
        map = {}
        isMap = false
    end
end

moveSeeds(seeds, map)
table.sort(seeds)
print(seeds[1])
