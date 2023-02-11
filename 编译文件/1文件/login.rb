require 'replit'

@db= Replit::Database::Client.new

def s_or_l
  puts "[1]SignUp\n[2]LogIn"
  if gets.strip== "1"
    puts `clear`
    puts "Enter new username"

    @db.set('new_user',gets.strip)

    puts "Enter new password"

    @db.set('new_pass',gets.strip)
    puts `clear`
    s_or_l()
  else
    puts `clear`
    puts "Enter Username"
    user= gets.strip

    puts "New Password"
    pass= gets.strip

    new_user = @db.get('new_user')
    new_pass = @db.get('new_pass')
    if user== new_user and pass== new_pass
      puts `clear`
      puts "Hello,#{user} !"
    else
      puts "Incorrect username or password"
    end
  end
end
s_or_l()