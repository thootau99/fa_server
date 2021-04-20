require 'discordrb'
require 'net/http'
geturi = URI('http://192.168.76.16:3000/api/v1/dialog/get')
imageuri = URI('http://192.168.76.16:3000/api/v1/dialog/getimage')
begin
  eventSave = ''
  sendMessage = false
  main = Thread.new do
    Thread.pass    # ????????�T??join?????
    while true

      result = Net::HTTP.get(geturi)
      resultJSON = JSON.parse(result)
      if (resultJSON['lock'] == true)
        image = Net::HTTP.get(imageuri)
        image = JSON.parse(image)
        File.open('./result.png', 'wb') do |file|
          file.write(Base64.decode64(image['image']))
        end
        if (eventSave != '' && sendMessage == false)
          eventSave.user.pm "検証が出って来ました！"
          eventSave.send_file(File.open('result.png', 'r'))
          sendMessage = true
        end
      else
        sendMessage = false
      end
      sleep 1
    end
    raise "unhandled exception"
  end

  botThread = Thread.new do
    Thread.pass
    bot = Discordrb::Bot.new token: ''
    bot.mention do |event|
      eventSave = event
      # The `pm` method is used to send a private message (also called a DM or direct message) to the user who sent the
      # initial message.
      event.user.pm('You have mentioned me!')
    end
    
    bot.message(contains: /^(action)/) do |event|
      content = event.content
      content = content.split(' ')
      event.respond("あなたが#{content[-1]}番のアクションを選びました")
      uri = URI("http://192.168.76.16:3000/api/v1/action/create?id=#{content[-1]}")
      puts uri
      response = Net::HTTP.get(uri)
    end
    
    bot.run
  end
  main.join
  botThread.join
rescue
  p $!  # => "unhandled exception"
end

