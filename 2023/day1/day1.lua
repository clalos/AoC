textNumbers = {
    ["one"] = 1,
    ["two"] = 2,
    ["three"] = 3,
    ["four"] = 4,
    ["five"] = 5,
    ["six"] = 6,
    ["seven"] = 7,
    ["eight"] = 8,
    ["nine"] = 9,
    ["1"] = 1,
    ["2"] = 2,
    ["3"] = 3,
    ["4"] = 4,
    ["5"] = 5,
    ["6"] = 6,
    ["7"] = 7,
    ["8"] = 8,
    ["9"] = 9
}

sum = 0
for line in io.lines("input.txt") do
    indexes = {}
    for i, v in pairs(textNumbers) do
        searchFrom = 1
        while true do
            startIdx = line:find(i, searchFrom, true)
            if not startIdx then break end
            table.insert(indexes, { startIdx, v })
            searchFrom = startIdx + 1
        end
    end
    table.sort(indexes, function(a, b) return a[1] < b[1] end)
    sum = sum + (indexes[1][2] .. indexes[#indexes][2])
end
print(sum)
