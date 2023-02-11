#puts "helloworld"
puts"TextCal ELD 1.9.4"
sleep(1)
def runit
    puts"Enter expression or type help"
    prob= gets
    pdob= prob.split
    case prob[1]
    when "+","-","*","%","/"
      puts eval("prob[0].to_i"+prob[1]+"prob[2].to_i")
    if gets.chomp.casecmp('again').zero?
      runit
    else
      puts "Done." end
   when "ex" 
      puts prob[0].to_i**prob[2].to_i
      if gets.chomp.casecmp('again').zero?
        runit
      else
        puts "Done." end
    else 
      if 
      prob[0].casecmp('help').zero?
        puts "use operators +,*,-,% for modul(reminder of a divison problem), and ex(EXPONENTIAL growth). For more info,please type details.To calculate,press enter."
       if gets.chomp.casecmp('details').zero?
         puts "You need to put spaces between number and operator.Commands you can use are help,info,details."
       else
         runit
       end
         runit
        elsif prob[0].casecmp('info').zero?
        puts"Copy of other(Text Calc 1.9.4)"
        puts"Build new name Epic Laughing Desktop"
        puts"Running Ruby version"+RUBY_VERSION 
        runit
      elsif   prob[0].casecmp("nextversion").zero?
        puts"Version 2.0.1 "
        puts"Infinite Evil Backpack"
        runit
      else puts"Error- Invalid input" 
        sleep(0.5)
        puts"Retype answer."
        sleep(0.5)
        runit
    end
  end
end
runit