local totalPoints = 0
for line in io.lines("input.txt") do
    local winning = {}
    local _, wins, have = line:match("(%d+): (.+)|(.+)")
    for num in wins:gmatch("%d+") do
        winning[num] = true
    end
    local winningNumbers = 0
    for num in have:gmatch("%d+") do
        if winning[num] then
            winningNumbers = winningNumbers + 1
        end
    end
    if winningNumbers > 0 then
        totalPoints = totalPoints + 2 ^ (winningNumbers - 1)
    end
end
print(totalPoints)
