# 6	Estimate population parameters (mean, variance) from sample data.
# Generate sample data
set.seed(123) # Ensures reproducibility
n <- 100
sample_data <- rnorm(n, mean = 50, sd = 10) # 100 random samples from N(50, 10^2)

# Estimate sample mean and variance
sample_mean <- mean(sample_data)
sample_variance <- var(sample_data) # Unbiased sample variance (divides by n-1)

# Print the results
print(paste("Sample Mean:", sample_mean))
print(paste("Sample Variance:", sample_variance))
