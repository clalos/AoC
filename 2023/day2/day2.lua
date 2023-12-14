local gamePattern, cubePattern = "Game (%d+): (.+)", "(%d+) (%w+)"
local pow = 0
for line in io.lines("input.txt") do
    local id, sets = line:match(gamePattern)
    local maxRed, maxBlue, maxGreen = 1, 1, 1
    for qty, color in sets:gmatch(cubePattern) do
        qty = tonumber(qty)
        if color == "red" and qty > maxRed then
            maxRed = qty
        elseif color == "blue" and qty > maxBlue then
            maxBlue = qty
        elseif color == "green" and qty > maxGreen then
            maxGreen = qty
        end
    end
    pow = pow + maxRed * maxBlue * maxGreen
end
print(pow)
