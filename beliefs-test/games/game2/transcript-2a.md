# Game 2 Transcript

## Question
"You have two ropes that each take an hour to burn; however, they burn at inconsistent rates. How can you measure 45 minutes? (You can light one or both ropes at one or both ends at the same time.)"

## Solution

**Answer: Measure 45 minutes by lighting ropes strategically to use their burn rates for timing.**

### Step-by-step procedure:

1. **At t = 0 minutes:** Light both ends of Rope 1, AND light one end of Rope 2
   - Rope 1 burns from both ends toward the middle
   - Rope 2 burns from one end

2. **At t = 30 minutes:** Rope 1 is completely burned
   - Why? When you burn a rope from both ends simultaneously, it takes half the normal time (30 minutes instead of 60)
   - Rope 2 has been burning for 30 minutes from one end, so 30 minutes worth of rope remains

3. **At t = 30 minutes:** Light the other end of Rope 2
   - The remaining 30 minutes of rope now burns from both ends
   - This takes 15 more minutes instead of 30

4. **At t = 45 minutes:** Rope 2 is completely burned

### Why this works:
- The key insight is that lighting both ends of a rope halves its burn time, independent of burn rate inconsistencies
- We don't need to know the exact burn rate of either rope
- We use the physical constraint that a rope burned from both ends reaches the middle in half the time

**Total elapsed time: 30 + 15 = 45 minutes**
