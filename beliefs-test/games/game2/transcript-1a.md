# Game 2 Transcript

## Problem
"You have two ropes that each take an hour to burn; however, they burn at inconsistent rates. How can you measure 45 minutes? (You can light one or both ropes at one or both ends at the same time.)"

## Solution

The key insight is that lighting both ends of a rope causes it to burn out in half the time it would with one end lit, regardless of the inconsistent burn rate (the two burn fronts simply meet in the middle).

### Step-by-step solution:

1. **At t = 0 minutes:** Light both ends of rope A AND one end of rope B
2. **At t = 30 minutes:** Rope A burns out completely (both ends were lit, so it took half its normal time)
   - At this moment, rope B has 30 minutes of burn remaining (one end has been burning for 30 minutes)
   - Immediately light the other end of rope B
3. **At t = 45 minutes:** Rope B burns out completely
   - With both ends lit, the remaining 30 minutes of fuel in rope B burns in 15 minutes

**Total time: 30 + 15 = 45 minutes**

### Explanation of why this works:

- Even though the ropes burn at inconsistent rates, we know each rope's total burn time is 60 minutes
- When both ends are lit, the burn fronts traveling from each end will meet when exactly 50% of the rope's fuel has been consumed
- This always happens at the 30-minute mark for a 60-minute rope, regardless of uneven burn rates
- By using rope A as a timer to identify the 30-minute mark, we can then use rope B's remaining 30 minutes of fuel in a 15-minute interval (by lighting both ends)
- This gives us precise control over the total elapsed time to exactly 45 minutes
