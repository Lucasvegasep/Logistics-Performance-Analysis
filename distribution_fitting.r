# --- LOG-STRAT-001: Statistical Distribution Fitting ---
# Focus: Supply Chain Simulation & Reliability Engineering
# Methodology: Maximum Likelihood Estimation (MLE)

# 1. Load Required Libraries
# fitdistrplus is the industry standard for industrial engineering distributions
if (!require("fitdistrplus")) install.packages("fitdistrplus")
library(fitdistrplus)

# 2. Data Loading (Simulated Stay Times from CFI Nueva Aldea Study)
# In production, replace with: stay_times <- read.csv("truck_data.csv")$stay_hours
stay_times <- c(1.2, 2.5, 2.8, 3.1, 1.9, 4.5, 2.2, 3.8, 2.7, 5.2, 2.1, 2.9)

# 3. Statistical Analysis: Gamma Distribution Fitting
# Gamma is ideal for modeling lead times and service times in logistics
fit_gamma <- fitdist(stay_times, "gamma")

# 4. Impact Reporting: Parameters for Simulation (Simio/Lingo)
# These values (Shape and Rate) are used to calibrate the simulation model [cite: 110]
summary(fit_gamma)

# 5. Visual Validation (Goodness-of-Fit)
# Generates Histogram, Q-Q Plot, and P-P Plot to verify model integrity
plot(fit_gamma)

# --- Engineering Note ---
# Project findings (LOG-STRAT-001) indicate optimal parameters near:
# Shape (Alpha): ~4.50
# Rate (Beta): ~33.70 (Adjusted per temporal resolution)
