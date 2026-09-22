success_rate <- function(speed) {
  if (speed >= 1 && speed <= 4){
    rate <- 1
  } else if (speed >= 5 && speed <= 8) {
    rate <- 0.9
  } else if (speed == 9) {
    rate <- 0.8
} else if (speed == 10) {
    rate <- 0.77
  } else {
    rate <- 0
  }
}

production_rate_per_hour <- function(speed) {
  rate <- speed * 221 * success_rate(speed)
}

working_items_per_minute <- function(speed) {
  items <- as.integer(production_rate_per_hour(speed) / 60)
}
