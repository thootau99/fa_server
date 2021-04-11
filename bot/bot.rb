require 'discordrb'

begin
  main = Thread.new do
    Thread.pass    # ????????�T??join?????
    while true
      sleep 1
      print "test"
    end
    raise "unhandled exception"
  end

  botThread = Thread.new do
    Thread.pass
    bot = Discordrb::Bot.new token: ''
    eventSave = ''
    bot.mention do |event|
      eventSave = event
      # The `pm` method is used to send a private message (also called a DM or direct message) to the user who sent the
      # initial message.
      event.user.pm('You have mentioned me!')
    end
    
    bot.message(content: 'checkEvent') do |event|
      while true
        eventSave.user.pm "test"
        sleep 1
      end
    end
    
    bot.run
  end
  main.join
  botThread.join
rescue
  p $!  # => "unhandled exception"
end

