#!/usr/bin/env ruby
# regex that matches a 10 digit number

puts ARGV[0].scan(/^\d{10}$/).join
