import csv
import re
from csv import writer
from collections import Counter


def reader(filename):
    with open(filename) as f:
        log = f.read()
        print(log)

        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.'
        ips_list = re.findall(regexp, log)
        return ips_list

def username(filename):
    with open(filename) as f:
        log = f.read()
        print(log)

        regexp = r'^(.{6})(.*) myth.*SRC=(.*?) DST=(.*?) .*SPT(.*?)'
        ips_list = re.findall(regexp, log)
        return ips_list

def count(ips_list):
    return Counter(ips_list)

def write_csv(counter):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        header = {'ip address', 'contents'}
        writer.writerow(header)

        for item in counter:
            writer.writerow((item, counter[item]))

def write_csv2(counter):
    with open('output2.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        header = {'ip address', 'contents'}
        writer.writerow(header)

        for item in counter:
            writer.writerow((item, counter[item]))

if __name__ == '__main__':
    write_csv(count(reader('log')))
    write_csv2(count(username('log')))