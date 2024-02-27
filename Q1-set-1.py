# 1)Look at the data given below. Plot the data, find the outliers and find out  μ,σ,σ^2
import numpy as np
Measure_X = [24.23,25.53,25.41,24.14,29.62,28.25,25.81,24.39,40.26,32.95,91.36,25.99,39,42,26.71,35.00]

mean = np.average(Measure_X)
mean
variance = np.var(Measure_X)
variance
standard_deviation = np.std(Measure_X)
standard_deviation

# 4). AT&T was running commercials in 1990 aimed at luring back customers who had switched to one of the other long-distance phone service providers. One such commercial shows a businessman trying to reach Phoenix and mistakenly getting Fiji, where a half-naked native on a beach responds incomprehensibly in Polynesian. When asked about this advertisement, AT&T admitted that the portrayed incident did not actually take place but added that this was an enactment of something that “could happen.” Suppose that one in 200 long-distance telephone calls is misdirected. What is the probability that at least one in five attempted telephone calls reaches the wrong number? (Assume independence of attempts.)

poplation_size = 200
one_is_200_misdirected = 1/200
sample_size = 5

from scipy.stats import binom
Bi=binom(sample_size,one_is_200_misdirected)
Bi
p = 1-Bi.cdf(0)
p
print("at least one in five attempted telephone calls reaches the wrong number is:",(p*100).round(4),"%")

# 5(iV) What is the good measure of the risk involved in a venture of this kind? Compute this measure
import numpy as np
X =[-2000,-1000,0,1000,2000,3000]
X
probability_X =[0.1,0.1,0.2,0.2,0.3,0.1]
probability_X

mean = np.average(X,weights=probability_X)
mean
std = np.sqrt(np.average((X-mean)**2,weights=probability_X))
std
