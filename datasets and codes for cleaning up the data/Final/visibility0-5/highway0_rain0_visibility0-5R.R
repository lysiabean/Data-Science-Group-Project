mydata = read.csv("highway0_rain1_visibility0-5.csv")

hour = mydata$Hour

hour <- table(hour)
hour
barplot(hour, ylab = "Number of Car Accidents", xlab = "Time (Hours)", main = "Total Car Accidents Over Time")
plot(hour, type = "l", ylab = "Number of Car Accidents", xlab = "Time (Hours)", main = "Total Car Accidents Over Time")

