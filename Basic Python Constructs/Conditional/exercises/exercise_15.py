first_number = int(input())
second_number = int(input())

fn_fd = first_number // 10
fn_sd = first_number % 10

sd_fd = second_number // 10
sd_sd = second_number % 10

max_digit = max(fn_fd, fn_sd, sd_fd, sd_sd)

min_digit = min(fn_fd, fn_sd, sd_fd, sd_sd)

list = [fn_fd, fn_sd, sd_fd, sd_sd]

list.remove(max_digit)
list.remove(min_digit)

print(f"{max_digit}{sum(list) % 10}{min_digit}")



