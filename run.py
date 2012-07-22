#!/usr/bin/env python

# pretty sure this is an awful way to do this
# looked on the thinking python answers page, and there answer isn't very accurate.
# it shows 7:30 but the real answer would be 7:30:21
# My method sucks too, however.

hour = int(6)
minuteStart = int(52)

easyPaceMinutes = int(8)
easyPaceSeconds = int(15)

tempoMinutes = int(7)
tempoSeconds = int(12)

print("Start %s:%s\tEnd %s:%s") % ( hour, minuteStart, ( (easyPaceMinutes * 2) + (tempoMinutes * 3)), ((easyPaceSeconds * 3) + (tempoSeconds *3)) ) 
