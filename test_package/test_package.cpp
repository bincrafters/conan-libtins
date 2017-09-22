#include <tins/tins.h>

int main() {
    Tins::EthernetII eth = Tins::EthernetII() / Tins::IP() / Tins::TCP();
}