import matplotlib.pyplot as plt

df["Contract"].value_counts().plot(kind="bar")

plt.title("Distribuição de tipos de contrato")
plt.show()
