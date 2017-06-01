
#Variables
ORIGIN_FILE_NAME = 'resultados-cilk'
DESTINATION_FILE_NAME = 'stats-cilk'


#Open File
results_file  = open(ORIGIN_FILE_NAME, 'r')

sum_real = 0.0
sum_user = 0.0
sum_sys = 0.0
sum_total = 0.0

last_real = 0.0
last_user = 0.0
last_sys = 0.0

test_number = 0
test_aux = 0

#Read file and get sum
for linha in results_file:
    if 'real' in linha:
        print 'Processando: ' + linha
        linha = linha.replace('real\t', '')
        print '\tResultado: ' + linha

        minutos, segundos = linha.split("m")
        segundos = segundos.replace("s", "")
        print '\tMinutos: ' + minutos
        print '\tSegundos: ' + segundos

        final = float(minutos) * 60.0 + float(segundos)
        print '\tFinal: ' + str(final)
        last_real = final
        sum_real += final

        test_aux += 1
    else:
        if 'user' in linha:
            print 'Processando: ' + linha
            linha = linha.replace('user\t', '')
            print '\tResultado: ' + linha

            minutos, segundos = linha.split("m")
            segundos = segundos.replace("s", "")
            print '\tMinutos: ' + minutos
            print '\tSegundos: ' + segundos

            final = float(minutos) * 60.0 + float(segundos)
            print '\tFinal: ' + str(final)
            last_user = final
            sum_user += final

            test_aux += 1
        else:
                if 'sys' in linha:
                    print 'Processando: ' + linha
                    linha = linha.replace('sys\t', '')
                    print '\tResultado: ' + linha

                    minutos, segundos = linha.split("m")
                    segundos = segundos.replace("s", "")
                    print '\tMinutos: ' + minutos
                    print '\tSegundos: ' + segundos

                    final = float(minutos) * 60.0 + float(segundos)
                    print '\tFinal: ' + str(final)
                    last_sys = final
                    sum_sys += final

                    print '\tTotal: ' + str(last_real + last_user + last_sys)
                    sum_total += last_real + last_user + last_sys

                    test_aux += 1
    if test_aux > 2:
        test_aux = 0
        test_number += 1

#Average
average_real = sum_real / test_number
average_user = sum_user / test_number
average_sys = sum_sys / test_number
average_total = sum_total / test_number


#Variancia
variance_real = 0.0
variance_user = 0.0
variance_sys = 0.0
variance_total = 0.0

results_file.seek(0)
for linha in results_file:
    if 'real' in linha:

        linha = linha.replace('real\t', '')
        minutos, segundos = linha.split("m")
        segundos = segundos.replace("s", "")
        final = float(minutos) * 60.0 + float(segundos)
        last_real = final
        variance_real += pow(final - average_real, 2)
    else:
        if 'user' in linha:
            linha = linha.replace('user\t', '')
            minutos, segundos = linha.split("m")
            segundos = segundos.replace("s", "")
            final = float(minutos) * 60.0 + float(segundos)
            last_user = final
            variance_user += pow(final - average_user, 2)
        else:
                if 'sys' in linha:
                    linha = linha.replace('sys\t', '')
                    minutos, segundos = linha.split("m")
                    segundos = segundos.replace("s", "")
                    final = float(minutos) * 60.0 + float(segundos)
                    last_sys = final
                    variance_sys += pow(final - average_sys, 2)

                    variance_total += pow((last_real + last_user + last_sys) - average_total, 2)

variance_real /= (test_number - 1)
variance_user /= (test_number - 1)
variance_sys /= (test_number - 1)
variance_total /= (test_number - 1)

#Standard Deviation
standard_deviation_real = pow(variance_real, 0.5)
standard_deviation_user = pow(variance_user, 0.5)
standard_deviation_sys = pow(variance_sys, 0.5)
standard_deviation_total = pow(variance_total, 0.5)

#Debug
print "------------------------------------------"
print "Sum:"
print "Real: " + str(sum_real)
print "User: " + str(sum_user)
print "Sys: " + str(sum_sys)
print "Total: " + str(sum_total)
print "------------------------------------------"
print "Average:"
print "Real: " + str(average_real)
print "User: " + str(average_user)
print "Sys: " + str(average_sys)
print "Total: " + str(average_total)
print "------------------------------------------"
print "Variance:"
print "Real: " + str(variance_real)
print "User: " + str(variance_user)
print "Sys: " + str(variance_sys)
print "Total: " + str(variance_total)
print "------------------------------------------"
print "Standard Deviation:"
print "Real: " + str(standard_deviation_real)
print "User: " + str(standard_deviation_user)
print "Sys: " + str(standard_deviation_sys)
print "Total: " + str(standard_deviation_total)
print "------------------------------------------"
print "OBS: time in seconds"

#Close file
results_file.close()

#Write results to file
stats_file = open(DESTINATION_FILE_NAME, 'w')
stats_file.write("------------------------------------------\n")
stats_file.write("Sum:\n")
stats_file.write("Real: " + str(sum_real) + "\n")
stats_file.write("User: " + str(sum_user) + "\n")
stats_file.write("Sys: " + str(sum_sys) + "\n")
stats_file.write("Total: " + str(sum_total) + "\n")
stats_file.write("------------------------------------------\n")
stats_file.write("Average:\n")
stats_file.write("Real: " + str(average_real) + "\n")
stats_file.write("User: " + str(average_user) + "\n")
stats_file.write("Sys: " + str(average_sys) + "\n")
stats_file.write("Total: " + str(average_total) + "\n")
stats_file.write("------------------------------------------\n")
stats_file.write("Variance:\n")
stats_file.write("Real: " + str(variance_real) + "\n")
stats_file.write("User: " + str(variance_user) + "\n")
stats_file.write("Sys: " + str(variance_sys) + "\n")
stats_file.write("Total: " + str(variance_total) + "\n")
stats_file.write("------------------------------------------\n")
stats_file.write("Standard Deviation:\n")
stats_file.write("Real: " + str(standard_deviation_real) + "\n")
stats_file.write("User: " + str(standard_deviation_user) + "\n")
stats_file.write("Sys: " + str(standard_deviation_sys) + "\n")
stats_file.write("Total: " + str(standard_deviation_total) + "\n")
stats_file.write("------------------------------------------\n")
stats_file.close()

