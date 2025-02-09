# Parameters
mu <- 5
sigma <- 2
n <- 30
N_sim <- 1000

# Initialize vectors
sample_means <- numeric(N_sim)
sample_vars <- numeric(N_sim)

# Simulation
set.seed(123)
for (i in 1:N_sim) {
    data <- rnorm(n, mean = mu, sd = sigma)
    # print(data)
    sample_means[i] <- mean(data)
    sample_vars[i] <- var(data)
}
# print(sample_means)
# print(sample_vars)
# Check correlation
correlation <- cor(sample_means, sample_vars)
print(paste("Correlation between sample mean and sample variance:", correlation))

# Graphical Output
par(mfrow = c(2, 2))

# Histogram of sample means
hist(sample_means, breaks = 30, col = "lightblue", main = "Distribution of Sample Means", xlab = "Sample Mean", border = "white")
curve(dnorm(x, mean = mu, sd = sigma / sqrt(n)), add = TRUE, col = "red", lwd = 2)

# Histogram of sample variances
hist(sample_vars, breaks = 30, col = "lightgreen", main = "Distribution of Sample Variances", xlab = "Sample Variance", border = "white")
curve(dchisq((x * (n - 1)) / sigma^2, df = n - 1) * (n - 1) / sigma^2, add = TRUE, col = "blue", lwd = 2)

# Scatterplot of sample means vs. sample variances
plot(sample_means, sample_vars, pch = 19, col = rgb(0, 0, 1, 0.5), main = "Sample Mean vs. Sample Variance", xlab = "Sample Mean", ylab = "Sample Variance")
abline(h = sigma^2, col = "red", lwd = 2)

# Q-Q plot for sample means
qqnorm(sample_means, main = "Q-Q Plot for Sample Means", col = "blue")
qqline(sample_means, col = "red", lwd = 2)
