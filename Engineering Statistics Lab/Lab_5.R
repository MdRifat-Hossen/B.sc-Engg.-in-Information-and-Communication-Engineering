# Lab 5: Distribution of Medians and Ranges from Sampled Populations

# Parameters
mu <- 0
sigma <- 1
n <- 20
N_sim <- 1000

# Initialize vectors
medians <- numeric(N_sim)
ranges <- numeric(N_sim)

# Simulation
set.seed(123)
for (i in 1:N_sim) {
    data <- rnorm(n, mean = mu, sd = sigma)
    medians[i] <- median(data)
    ranges[i] <- max(data) - min(data)
}

# Graphical Output
par(mfrow = c(2, 2))

# Histogram of medians
hist(medians, breaks = 30, col = "lightblue", probability = TRUE, main = "Distribution of Medians", xlab = "Median", border = "white")
curve(dnorm(x, mean = mu, sd = sigma / sqrt(n)), add = TRUE, col = "red", lwd = 2)

# Histogram of ranges
hist(ranges, breaks = 30, col = "lightgreen", probability = TRUE, main = "Distribution of Ranges", xlab = "Range", border = "white")

# Density plot of medians
plot(density(medians), col = "blue", lwd = 2, main = "Density Plot of Medians", xlab = "Median")
curve(dnorm(x, mean = mu, sd = sigma / sqrt(n)), add = TRUE, col = "red", lwd = 2)

# Boxplot of medians and ranges
boxplot(list(Medians = medians, Ranges = ranges), col = c("lightblue", "lightgreen"), main = "Boxplot of Medians and Ranges", ylab = "Value")
