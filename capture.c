#include <pcap.h>
#include <stdio.h>

int main() {
    pcap_t *handle;
    char errbuf[PCAP_ERRBUF_SIZE];
    struct pcap_pkthdr header;
    const u_char *packet;

    // ネットワークインターフェースのオープン
    handle = pcap_open_live("eth0", BUFSIZ, 1, 1000, errbuf);
    if (handle == NULL) {
        printf("Error opening pcap: %s\n", errbuf);
        return 1;
    }

    // パケットキャプチャの開始
    packet = pcap_next(handle, &header);
    printf("Captured a packet of length %d\n", header.len);

    pcap_close(handle);
    return 0;
}
