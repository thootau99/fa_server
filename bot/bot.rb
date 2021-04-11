require 'discordrb'

bot = Discordrb::Bot.new token: ''
eventSave = ''
bot.mention do |event|
  eventSave = event
  # The `pm` method is used to send a private message (also called a DM or direct message) to the user who sent the
  # initial message.
  event.user.pm('You have mentioned me!')
end

bot.message(content: 'check') do |event|
  while true
    eventSave.respond "ㄏ."
    sleep 0.5
  end
end

bot.run

