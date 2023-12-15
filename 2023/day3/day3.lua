local schema, row = {}, 1

-- read input file and store it in a 2D array
for line in io.lines("input.txt") do
    schema[row] = {}
    for c in line:gmatch(".") do
        table.insert(schema[row], c)
    end
    row = row + 1
end

-- getNumber composes the full number starting from the current position by
-- shifting left and right.
local function getNumber(i, j)
    local row, number = schema[i], schema[i][j]

    -- left part of number
    if j > 1 then
        local col = j - 1
        while tonumber(row[col]) do
            number = row[col] .. number
            if col == 1 then break end
            col = col - 1
        end
    end

    -- right part of number
    if j < #row then
        local col = j + 1
        while tonumber(row[col]) do
            number = number .. row[col]
            if col == #row then break end
            col = col + 1
        end
    end

    return tonumber(number)
end

-- getAdjacent looks for adjacent numbers. If a number is found it is added
-- to the list of adjacent numbers.
local function getAdjacent(row, col)
    local adjacents = {}
    for i = row - 1, row + 1 do
        for j = col - 1, col + 1 do
            if i >= 1 and i <= #schema and j >= 1 and j <= #schema[i] and (i ~= row or j ~= col) then
                local v = schema[i][j]
                if tonumber(v) then
                    table.insert(adjacents, getNumber(i, j))
                end
            end
        end
    end

    return adjacents
end

-- removeDuplicates removes duplicates from a list of numbers.
local function removeDuplicates(nums)
    local hash = {}
    local res = {}

    for _, v in ipairs(nums) do
        if not hash[v] then
            res[#res + 1] = v
            hash[v] = true
        end
    end

    return res
end

-- compose a map for each gear => [adjacent numbers]
local partNumbers = {}
for idxRow, row in ipairs(schema) do
    for idxCol, value in ipairs(row) do
        if value == "*" then
            local numbers = getAdjacent(idxRow, idxCol)
            partNumbers[idxRow .. "," .. idxCol] = removeDuplicates(numbers)
        end
    end
end

-- calculate the ratios sum
local ratiosSum = 0
for _, numbers in pairs(partNumbers) do
    if #numbers == 2 then
        ratiosSum = ratiosSum + numbers[1] * numbers[2]
    end
end
print(ratiosSum)