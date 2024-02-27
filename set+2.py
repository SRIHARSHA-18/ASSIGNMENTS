
# 1) The time required for servicing transmissions is normally distributed with μ = 45 minutes and σ = 8 minutes. The service manager plans to have work begin on the transmission of a customer’s car 10 minutes after the car is dropped off and the customer is told that the car will be ready within 1 hour from drop-off. What is the probability that the service manager cannot meet his commitment? 
 
mu = 45
sigma = 8
target_time=60

# probability that the service manager cannot meet his commitment (>60)
import scipy.stats as stats
cdf_target = stats.norm.cdf(mu,sigma,target_time);
cdf_target

X = 1-cdf_target
X

# 2). The current age (in years) of 400 clerical employees at an insurance claims processing center is normally distributed with mean μ = 38 and Standard deviation σ =6. For each statement below, please specify True/False. If false, briefly explain why.
# Given data

total_size = 400
mean = 38
std = 6

# A). More employees at the processing center are older than 44 than between 38 and 44.
import scipy.stats as stats
older_than_44 = 1-stats.norm.cdf(44,mean,std)
older_than_44

prob_between_38_and_44 = stats.norm.cdf(44,mean,std) - stats.norm.cdf(38,mean,std)
prob_between_38_and_44

if prob_between_38_and_44 > older_than_44:
    print("Statement Is True")
else:
    print("Statement Is False")

# B). A training program for employees under the age of 30 at the center would be expected to attract about 36 employees.
prob_under_30 = stats.norm.cdf(30,mean,std)
prob_under_30  

prob_expected_under_30 = prob_under_30 * total_size
prob_expected_under_30

if prob_expected_under_30 > 36:
    print("Statement Is True")
else:
    print("Statement Is False")
    
# 4). Let X ~ N(100, 20^2). Find two values, a and b, symmetric about the mean, such that the probability of the random variable taking a value between them is 0.99. 

# Given parameters of the normal distribution
mean = 100
variance = 20**2
standard_deviation = (variance) ** 0.5

# Desired probability for X to be between a and b
probability_between_a_and_b = 0.99

import scipy.stats as stats
# Find the critical z-scores for the desired probability
z_lower = stats.norm.ppf((1 - probability_between_a_and_b) / 2)
z_upper = stats.norm.ppf(1 - (1 - probability_between_a_and_b) / 2)

# Calculate the values a and b symmetric about the mean
a = mean + (z_lower * standard_deviation)
b = mean + (z_upper * standard_deviation)

print(f"The values a and b are:",a,"And",b)

# 5). Consider a company that has two different divisions. The annual profits from the two divisions are independent and have distributions Profit1 ~ N(5, 3^2) and Profit2 ~ N(7, 4^2) respectively. Both the profits are in $ Million. Answer the following questions about the total profit of the company in Rupees. Assume that $1 = Rs. 45
# A). Specify a Rupee range (centered on the mean) such that it contains 95% probability for the annual profit of the company.
# Given parameters of Profit1 and Profit2 in $ Million
p1_mean = 5
p2_mean = 7
p1_var = 3**2
p2_var = 4**2

# Conversion rate: $1 = Rs. 45
conversion_rate = 45

# Calculate the mean and standard deviation of the total profit in $ Million
mean_total_profit = p1_mean + p2_mean
mean_total_profit
var_total_profit = p1_var + p2_var
var_total_profit
std_total_profit = var_total_profit**0.5
std_total_profit

# Convert the total profit to Rupees
mean_total_profit_rupees = mean_total_profit*conversion_rate
mean_total_profit_rupees
std_total_profit_rupees = std_total_profit*conversion_rate
std_total_profit_rupees

# calculate the Z_critical score for the probability
import scipy.stats as stats
Z_lower = stats.norm.ppf((1-0.95)/2)
Z_lower
Z_upper = stats.norm.ppf(1-(1-0.95)/2)
Z_upper

#calculate the vales a and b symmetric about the mean
a = mean_total_profit_rupees + (Z_lower * std_total_profit_rupees)
a
b = mean_total_profit_rupees + (Z_upper * std_total_profit_rupees)
b
# B). Specify the 5th percentile of profit (in Rupees) for the company
import scipy.stats as stats
percentile_of_profit = stats.norm.ppf(0.05,mean_total_profit_rupees,std_total_profit_rupees)
percentile_of_profit

# C). Which of the two divisions has a larger probability of making a loss in a given year?

# A:
p1_mean = 5
p2_mean = 7
p1_var = 32
p2_var = 42
conversion_rate = 45
mean_profit1 = p1_mean *conversion_rate
mean_profit2 = p2_mean *conversion_rate
var_profit1 = p1_var * conversion_rate
var_profit2 = p2_var * conversion_rate
std_profit1 = var_profit1**0.5
std_profit2 = var_profit2**0.5

import scipy.stats as stats
# Calculate the probability of making a loss for Profit (normal distribution CDF)
prob_loss_profit1 = stats.norm.cdf(0,mean_profit1,std_profit1)

# Calculate the probability of making a loss for Profit2 (normal distribution CDF)
prob_loss_profit2 = stats.norm.cdf(0, mean_profit2,std_profit2)

if prob_loss_profit1 > prob_loss_profit2:
    print("prob_loss_profit1 is Larger Probability")
else:
    print("prob_loss_profit2 is Larger Probability")

