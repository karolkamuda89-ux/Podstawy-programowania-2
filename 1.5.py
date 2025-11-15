###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
tasks_ok = int(input('podaj liczbe poprawnie wykonanych zadan:'))
test_passed = False

if tasks_ok >= total_tasks  :
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Egzamin nie zdany')