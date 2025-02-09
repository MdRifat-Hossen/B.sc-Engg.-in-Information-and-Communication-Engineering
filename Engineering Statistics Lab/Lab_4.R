# Lab 4: Simulation of F-Distributed Data and Its Relationship with χ2-Distributions

# Parameters
df1 <- 5 # Degrees of freedom for the first χ² distribution
df2 <- 10 # Degrees of freedom for the second χ² distribution
N_sim <- 1000 # Number of simulations

# Generate F-distributed data
set.seed(123) # Ensures reproducibility
chi2_1 <- rchisq(N_sim, df = df1)
chi2_2 <- rchisq(N_sim, df = df2)
f_data <- (chi2_1 / df1) / (chi2_2 / df2) # F-distribution formula
# print(f_data)
# Graphical Output
par(mfrow = c(2, 2)) # Arrange plots in a 2x2 grid

# Histogram with theoretical F-distribution curve
hist(f_data,
    breaks = 30, col = "lightblue", probability = TRUE,
    main = "F-Distribution", xlab = "Value", border = "white"
)
curve(df(x, df1 = df1, df2 = df2), add = TRUE, col = "red", lwd = 2)

# Density plot with theoretical F-distribution curve
plot(density(f_data), col = "blue", lwd = 2, main = "Density Plot", xlab = "Value")
curve(df(x, df1 = df1, df2 = df2), add = TRUE, col = "red", lwd = 2)

# Q-Q plot for F-distribution
qqplot(qf(ppoints(N_sim), df1 = df1, df2 = df2), f_data,
    main = "Q-Q Plot for F-Distribution", col = "blue",
    xlab = "Theoretical Quantiles", ylab = "Sample Quantiles"
)
abline(0, 1, col = "red", lwd = 2)

# Boxplot
boxplot(f_data, col = "lightgreen", main = "Boxplot of F-Distributed Data", ylab = "Value")
