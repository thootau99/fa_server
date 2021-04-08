require 'discordrb'

bot = Discordrb::Bot.new token: 'ODI5MjQ3MjIxOTI4MDM0MzA1.YG1WqA.Et025YyGlo8F0KC_23th115-bfY'
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
