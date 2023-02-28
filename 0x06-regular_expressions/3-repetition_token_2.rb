#!/usr/bin/env ruby
# REgex that matches hbtn, hbttn, hbtttn, hbttttn

puts ARGV[0].scan(/hbt{2,5}n/).join
