require 'discordrb'

bot = Discordrb::Bot.new token: ''
eventSave = ''
bot.mention do |event|
  eventSave = event
  # The `pm` method is used to send a private message (also called a DM or direct message) to the user who sent the
  # initial message.
  event.user.pm('You have mentioned me!')
end

bot.message(content: 'checkEvent') do |event|
  eventSave.respond "testfromold"
end

bot.run
