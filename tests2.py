import cross_sections as xsect
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    data = xsect.getXsections(
        url="https://clas.sinp.msu.ru/cgi-bin/jlab/db.cgi?beam=1&beam_pol=0&tgt=proton&tz=&ta=&target_pol=0&final=2&final_pol=0&q2min=&q2max=&wmin=&wmax=&xmin=&xmax=&ephmin=&ephmax=&quantity=19&authors=&year=&eid=&texttable=on&selected-fields=id&selected-fields=final&selected-fields=q2min&selected-fields=q2max&selected-fields=wmin&selected-fields=wmax&selected-fields=quantity&selected-fields=title&selected-fields=authors&selected-fields=year&limit=100&search=Start+search"
    )

    data.parseDataSets()

    for sets in data.datasets:
        fig, ax = plt.subplots(figsize=[12, 8])
        for cos_t in sets.dataFrame["cos(theta_pi)"].unique():
            cut = sets.dataFrame["cos(theta_pi)"] == cos_t
            x = np.radians(sets.dataFrame[cut]["phi_pi"])
            y = sets.dataFrame[cut]["dsigma/dOmega"]
            yerr = sets.dataFrame[cut]["Data errors"]
            ax.errorbar(x, y, yerr=yerr, fmt=".", label=f"{cos_t}")

        ax.legend()
        fig.savefig(
            f"plots/W {sets.experiment['W range']} Q2 {sets.experiment['Q^2 range']}.png"
        )
        plt.close()

