# 7	Demonstrate consistency by increasing sample size and observing convergence to the true parameter.

# Population parameters
true_mean <- 50
true_variance <- 10^2

# Sample sizes to test
# sample_sizes <- c(10, 50, 100, 500, 1000, 5000, 10000)

# Initialize vectors to store results
sample_means <- numeric(true_variance)
sample_variances <- numeric(true_variance)

set.seed(123) # Ensures reproducibility

for (i in 1:true_variance) {
    n <- sample_sizes[i]
    sample_data <- rnorm(n, mean = true_mean, sd = sqrt(true_variance)) # Generate sample
    sample_means[i] <- mean(sample_data) # Estimate sample mean
    sample_variances[i] <- var(sample_data) # Estimate sample variance
}

# Plot the convergence for sample mean
par(mfrow = c(1, 2)) # Arrange plots side by side

# Plot convergence of the mean
plot(sample_sizes, sample_means,
    type = "b", col = "blue", pch = 19,
    main = "Convergence of Sample Mean", xlab = "Sample Size", ylab = "Sample Mean"
)
abline(h = true_mean, col = "red", lwd = 2, lty = 2)
grid()
legend("topright", legend = paste("True Mean =", true_mean), col = "red", lwd = 2, bty = "n")

# Plot convergence of the variance
plot(sample_sizes, sample_variances,
    type = "b", col = "green", pch = 19,
    main = "Convergence of Sample Variance", xlab = "Sample Size", ylab = "Sample Variance"
)
abline(h = true_variance, col = "red", lwd = 2, lty = 2)
grid()
legend("topright", legend = paste("True Variance =", true_variance), col = "red", lwd = 2, bty = "n")
