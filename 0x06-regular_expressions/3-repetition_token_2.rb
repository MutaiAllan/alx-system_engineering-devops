#!/usr/bin/env ruby
# REgex that matches hbtn, hbttn, hbtttn, hbttttn...

puts ARGV[0].scan(/hbt+n/).join
