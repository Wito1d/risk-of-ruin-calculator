from random import randrange

# user input

# If False we always risk the same fixed amount in each trade
# If True we always risk the same percentage of current capital in each trade
capitalization = False
base_capital = 100.0
# How much of capital we are risking in each trade. Check also capitalization.
# Examples:
# .5 we are risking half of our capital
# .1 we are risking 10% of our capital
risk_per_trade = .05
# How often w expcect to win
# Example:
# .5 - we expect to win 50% of the time
success_rate = .6
# How much we expect to win versus how much we expect to lose
# Example:
# 3 - you expect to win 3 times what you are risking
# .5 - every time you win you expect to win 50% of what you are risking
reward_risk = 1.784
num_of_trades = 2 * 21

# end of user input

max_cap = float(base_capital)
min_cap = float(base_capital)
max_drawndown = .0
valley = float(base_capital)
prev_outcome = -1
consecutive_wins = 0
consecutive_losses = 0
max_consecutive_wins = 0
max_consecutive_losses = 0

print("initial risk per trade: ", risk_per_trade * float(base_capital))
print("base capital: ", base_capital)
print("success rate: ", success_rate)
print("reward/risk: ", reward_risk)
print("num_of_trades: ", num_of_trades)
print("capitalization: ", capitalization)

capital = float(base_capital)

for x in range(num_of_trades):
    random_num = randrange(1,101)
    #print(random_num)
    if random_num > success_rate * 100:
        if capitalization:
            result = risk_per_trade * capital * -1
        else:
            result = risk_per_trade * float(base_capital) * -1
        #print("loss")
    else:
        if capitalization == 1:
            result = risk_per_trade * capital * reward_risk
        else:
            result = risk_per_trade * float(base_capital) * reward_risk
        #print("profit")

    capital += result
    #print(int(capital))
    if capital > max_cap:
        max_cap = capital
        valley = capital
    elif capital < min_cap:
        min_cap = capital

    if capital < valley:
        valley = capital

    drawdown = 1 - valley/max_cap
    if drawdown > max_drawndown:
        max_drawndown = drawdown

    if prev_outcome == 1 and result > 0:
        consecutive_wins = consecutive_wins + 1
        if max_consecutive_wins < consecutive_wins:
            max_consecutive_wins = consecutive_wins + 1
    elif prev_outcome == 0 and result < 0:
        consecutive_losses = consecutive_losses + 1
        if max_consecutive_losses < consecutive_losses:
            max_consecutive_losses = consecutive_losses + 1
    else:
        consecutive_wins = 0
        consecutive_losses = 0

    if result > 0:
        prev_outcome = 1
    elif result < 0:
        prev_outcome = 0


print("\n")
print("Max: ", end =" ")
print(int(max_cap))
print("Min: ", end =" ")
print(int(min_cap))

print("Max consecutive_wins: ", end =" ")
print(int(max_consecutive_wins))
print("Max consecutive_losses: ", end =" ")
print(int(max_consecutive_losses))

print("Max drawdown: ", end =" ")
print('{0:.0%}'.format(max_drawndown))
print("Net result: ", end =" ")
print(int(capital - base_capital))
print("\n")

