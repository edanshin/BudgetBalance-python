BALANCE_HISTORY = [107, 201, 201, 225, 216]

# BALANCE_HISTORY = [107, 201, 201, 225, 216]
#                     ^--5-^--4-^--3-^--2-^ days ago

# define maximum allowed history length
history_length = len(BALANCE_HISTORY)

# There is absolutely no need to create any slices from BALANCE_HISTORY.
# Instead, we get the required balances directly from BALANCE_HISTORY by simply providing an index.
# This approach is more simple, efficient and way better than slicing.

# Furthermore, besides creating unnecessary slices, the old code was
# subtracting balances to get difference between them, instead of simply comparing them.
# Also, getting a balance from specific day was done incorrectly,
# which was leading to index-out-of-range error.

# Also, iteration over the day range() is wrong in the old code:
# function parameters are set incorrectly.

def get_balance_history(number_of_days):
  # if entered number of days is out of allowed range, set default value
  if number_of_days < 2:
    number_of_days = 2
  elif number_of_days > history_length:
    number_of_days = history_length

  # iterate through history backwards - to get the correct index
  for day in range(number_of_days - 2, -1, -1):
    # balance from more recent day
    recent_balance = BALANCE_HISTORY[day]

    # balance from previous day in history
    previous_balance = BALANCE_HISTORY[day - 1]

    # define output message
    balance = f'Balance from {day + 2} days ago'

    # compare balances from both days
    if recent_balance == previous_balance:
      print(f'{balance} stayed THE SAME!')
    if recent_balance > previous_balance:
      print(f'{balance} INCREASED!')
    if recent_balance < previous_balance:
      print(f'{balance} DECREASED!')

# get number of days from console input
d = int(input('How many days of data? '))

# output the resulting balance history
get_balance_history(d)
