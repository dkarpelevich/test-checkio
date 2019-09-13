def checkio(addresses):
    bin_ips = []
    for ip in addresses:
        bin_ips.append(''.join([format(int(i), '08b') for i in ip.split('.')]))

    first_ip = bin_ips[0]
    for i in range(1, len(bin_ips)):
        match = ''
        for j in range(len(first_ip)):
            if int(first_ip[j]) ^ int(bin_ips[i][j]) == 0:
                match += bin_ips[i][j]
            else:
                break
        first_ip = match
    common_part = first_ip.ljust(32, '0')
    aggregated_ip = "%d.%d.%d.%d" % (int(common_part[0:8], 2), int(common_part[8:16], 2),
                      int(common_part[16:24], 2), int(common_part[24:32], 2))
    return aggregated_ip + '/' + str(len(first_ip))

if __name__ == '__main__':
    assert checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"
    assert checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"
    assert checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"
    assert checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"