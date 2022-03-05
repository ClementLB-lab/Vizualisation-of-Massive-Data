
        plt.title("TEMPF")
        heartDiseases["TEMPF"].plot(kind='hist')
        plt.savefig("tempf.pdf")
        plt.clf()

        heartDiseases["PULSE"].unique()

        plt.title("PULSE")
        heartDiseases["PULSE"].plot(kind='hist')
        plt.savefig("pulse.pdf")
        plt.clf()


        heartDiseases["RESPR"] = heartDiseases["RESPR"]
        heartDiseases["RESPR"].unique()

        plt.title("RESPR")
        heartDiseases["RESPR"].plot(kind='hist')
        plt.savefig("respr.pdf")
        plt.clf()


        heartDiseases["BPSYS"] = heartDiseases["BPSYS"]
        heartDiseases["BPSYS"].unique()

        plt.title("BPSYS")
        heartDiseases["BPSYS"].plot(kind='hist')
        plt.savefig("bpsys.pdf")
        plt.clf()


        heartDiseases["BPDIAS"] = heartDiseases["BPDIAS"]
        heartDiseases["BPDIAS"].unique()

        plt.title("BPDIAS")
        heartDiseases["BPDIAS"].plot(kind='hist')
        plt.savefig("bpdias.pdf")
        plt.clf()


        heartDiseases["POPCT"] = heartDiseases["POPCT"]
        heartDiseases["POPCT"].unique()

        plt.title("POPCT")
        heartDiseases["POPCT"].plot(kind='hist')
        plt.savefig("popct.pdf")
        plt.clf()


        heartDiseases["SCORE"] = heartDiseases["SCORE"]
        heartDiseases["SCORE"].unique()

        plt.title("SCORE")
        heartDiseases["SCORE"].plot(kind='hist')
        plt.savefig("score.pdf")
        plt.clf()