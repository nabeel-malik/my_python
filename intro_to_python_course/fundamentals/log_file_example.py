def logger(log):
    log_entry = input('Enter log item (enter to quit): ')
    count = 0

    while log_entry:
        count += 1
        log.write(str(count) + ": " + log_entry + "\n")
        log_entry = input('Enter log item (enter to quit): ')
    return count

# ------------------------------------------------------------------------------------------------------------------ #

log_file = open('m4_files\log_file.txt', 'w')
log_file.close()

log_file = open('m4_files\log_file.txt', 'a+')

num_logs = logger(log_file)

log_file.seek(0,0)
log_text = log_file.read()

print("\nNumber of logs entered:",num_logs,"\n")
print(log_text)
log_file.close()





