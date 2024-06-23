local wibox = require("wibox")
local awful = require("awful")

mocp_widget = wibox.widget.textbox()
mocp_widget:set_align("right")

function update_mocp(widget)
    local fd = io.popen("mocp -i")
    local infos = fd:read("*a")
    fd:close()

    -- local mocp = tonumber(string.match(infos, "(%d?%d?%d)%%")) / 100

    -- local text = string.match(infos, "PAUSE")
    local text = ""
    if string.find(infos, "State") then
        local state = string.match(infos, "State: (%C*)")
        if state == "PLAY" or state == "PAUSE" then
            if state == "PLAY" then
                -- text = "<span font='Underdog 12' color='#ebdbb2'>"
                text = "<span font='Underdog 12' color='#000000'>"
            -- else
            --     text = "<span color='grey'>"
            end
            local artist = string.match(infos, "Artist: (%C*)")
            local title = string.match(infos, "SongTitle: (%C*)")
            --local totalTime = string.match(infos, "TotalTime: (%C*)")
            --local currentTime = string.match(infos, "CurrentTime: (%C*)")
            --text = text .. title .. " - " .. artist .. " (" .. currentTime .. "/" .. totalTime .. ")</span>"
            text = text ..  title .. " - " .. artist .. " </span>"
        end
    -- else
    --     text = "<span color='grey'>No music</span>"
    end
    if not pcall(function() widget:set_markup(text) end) then
        text = "moc: error"
        widget:set_markup(text)
    end
end

update_mocp(mocp_widget)

mytimer = timer({ timeout = 2 })
mytimer:connect_signal("timeout", function () update_mocp(mocp_widget) end)
mytimer:start()
