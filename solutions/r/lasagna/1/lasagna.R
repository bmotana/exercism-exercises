# TODO: define the 'expected_minutes_in_oven()' function
expected_minutes_in_oven <- function(x = 60){
  x
}

# TODO: define the 'remaining_time_in_minutes()' function
remaining_time_in_minutes <- function(min) {
  expected_minutes_in_oven() - min
}

# TODO: define the 'prep_time_in_minutes()' function
prep_time_in_minutes <- function(min) {
  2 * min
}

# TODO: define the 'elapsed_time_in_minutes()' function
elapsed_time_in_minutes <- function(x,y) {
  prep_time_in_minutes(x) + y
}