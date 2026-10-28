import random
import math
import matplotlib.pyplot as plt

total = 200000
ebn0_db_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
ber_sim = []
ber_theory = []

for db in ebn0_db_list:
    ratio = 10 ** (db / 10)
    sigma = math.sqrt(1 / (2 * ratio))
    errors = 0

    for i in range(total):
        bit = random.randint(0, 1)
        signal = 2 * bit - 1
        noise = random.gauss(0, sigma)
        received = signal + noise

        if received > 0:
            decided = 1
        else:
            decided = 0

        if decided != bit:
            errors = errors + 1

    ber_sim.append(errors / total)
    ber_theory.append(0.5 * math.erfc(math.sqrt(ratio)))
    print(db, "dB -> BER", errors / total)

plt.semilogy(ebn0_db_list, ber_sim, "o-", label="Simulation")
plt.semilogy(ebn0_db_list, ber_theory, "--", label="Theory")
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("BER")
plt.title("BPSK over AWGN")
plt.grid(True, which="both")
plt.legend()
plt.savefig("ber_curve.png", dpi=150)
plt.show()