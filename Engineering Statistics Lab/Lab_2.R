# Lab 2: Generation and Analysis of χ2-Distributed Data

# Parameters
k <- 5
N_sim <- 1000

# Generate chi-squared data
set.seed(123)
chi2_data <- rchisq(N_sim, df = k)

# Compute mean and variance
mean_chi2 <- mean(chi2_data)
var_chi2 <- var(chi2_data)
print(paste("Mean:", mean_chi2))
print(paste("Variance:", var_chi2))

# Graphical Output
par(mfrow = c(3, 3))

# Histogram
hist(chi2_data, breaks = 30, col = "lightblue", probability = TRUE, main = "Chi-Squared Distribution", xlab = "Value", border = "white")
curve(dchisq(x, df = k), add = TRUE, col = "red", lwd = 2)

# Density plot
plot(density(chi2_data), col = "blue", lwd = 2, main = "Density Plot", xlab = "Value")
curve(dchisq(x, df = k), add = TRUE, col = "red", lwd = 2)

# Q-Q plot
qqplot(qchisq(ppoints(N_sim), df = k), chi2_data, main = "Q-Q Plot for Chi-Squared Data", col = "blue", xlab = "Theoretical Quantiles", ylab = "Sample Quantiles")
abline(0, 1, col = "red", lwd = 2)
