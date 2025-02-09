# Lab 3: Comparison of t-Distribution with Normal Distribution for Small Sample Sizes

# Parameters
n <- 10
N_sim <- 1000

# Generate data
set.seed(123)
t_data <- rt(N_sim, df = n - 1)
normal_data <- rnorm(N_sim)

# Graphical Output
par(mfrow = c(2, 2))

# Histogram of t-distribution
hist(t_data, breaks = 30, col = "lightblue", probability = TRUE, main = "t-Distribution", xlab = "Value", border = "white")
curve(dt(x, df = n - 1), add = TRUE, col = "red", lwd = 2)

# Histogram of normal distribution
hist(normal_data, breaks = 30, col = "lightgreen", probability = TRUE, main = "Normal Distribution", xlab = "Value", border = "white")
curve(dnorm(x), add = TRUE, col = "blue", lwd = 2)

# Density plot comparison
plot(density(t_data), col = "red", lwd = 2, main = "Density Comparison", xlab = "Value", ylim = c(0, 0.4))
lines(density(normal_data), col = "blue", lwd = 2)
legend("topright", legend = c("t-Distribution", "Normal Distribution"), col = c("red", "blue"), lwd = 2)

# Q-Q plot for t-distribution
qqplot(qt(ppoints(N_sim), df = n - 1), t_data, main = "Q-Q Plot for t-Distribution", col = "red", xlab = "Theoretical Quantiles", ylab = "Sample Quantiles")
abline(0, 1, col = "blue", lwd = 2)
