#!/usr/bin/env ruby
# REGEX that matches a string that starts with h and ends with nwith any single character in-between

puts ARGV[0].scan(/h.n/).join
