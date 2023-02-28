#!/usr/bin/env ruby
# Regexp that matches hbttn, hbtttn, hbttttn and hbtttttn

puts ARGV[0].scan(/hbt{2,5}n/).join
