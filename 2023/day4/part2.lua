-- load games
local cards = {}
for line in io.lines("input.txt") do
    local cardNo, winningNo, haveNo = line:match("(%d+): (.+)|(.+)")

    local winningList = {}
    for num in winningNo:gmatch("%d+") do
        winningList[num] = true
    end

    local haveList = {}
    for num in haveNo:gmatch("%d+") do
        haveList[num] = true
    end

    cards[tonumber(cardNo)] = { winning = winningList, have = haveList }
end

-- getWins returns the number of wins a card has
local function getWins(card)
    local wins = 0
    for winningNo, _ in pairs(card.winning) do
        if card.have[winningNo] then
            wins = wins + 1
        end
    end
    return wins
end

-- play returns the total number of cards played from the given card
local function play(cardNo, card)
    local wins = getWins(card)
    local count = 1
    for i = 1, wins do
        local nextCardNo = cardNo + i
        if not cards[nextCardNo] then return 0 end
        count = count + play(nextCardNo, cards[nextCardNo])
    end
    return count
end

-- play all cards
local totalCards = 0
for cardNo, card in pairs(cards) do
    totalCards = totalCards + play(cardNo, card)
end
print(totalCards)
