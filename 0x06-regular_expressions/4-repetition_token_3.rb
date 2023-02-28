#!/usr/bin/env ruby
# Regex matching hbn, hbtn, hbttn....

puts ARGV[0].scan(/(hbn|hbt+n)/).join
