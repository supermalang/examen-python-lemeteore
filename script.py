import typing as t

class DitSeries:
    """ """

    def __init__(self, name: str, data: t.Dict[int, t.Any]):
        """ Constructeur qui reçoit:
        - le nom d'une colonne
        - le contenu de la colonne sous forme de Dictionnaire
        - La clé du Dictionnaire est un entier
        - La valeur du Dictionnaire est de n'importe quel type"""

    def __mul__(self, other: int) -> "DitSeries":
        """ Implementation de l'opération de multiplication.
        - L'argument est de type entier
        - La valeur renvoyée est de type DitSeries
        - Chaque élément de la série est multiplié par l'argument
        """

    def __div__(self, other: int) -> "DitSeries":
        """ Implementation de l'opération de division.
        - L'argument est de type entier
        - La valeur renvoyée est de type DitSeries
        - Chaque élément de la série est divisé par l'argument
        """

    def __sub__(self, other: int) -> "DitSeries":
        """Soustraction """


    def __add__(self, other: int) -> "DitSeries":
        """Addition"""

    def __gt__(self, other: int) -> "DitSeries":
        """Comparaison (supérieur) """

    def __getitem__(self, key: "DitSeries") -> "DitSeries":
        """ """

    def __repr__(self) -> str:
        """ Affiche une representation de l'objet DitSeries. """
        return f"<DitSeries: {self.name} {self.data}>"


class DitDataFrame:
    """ """
    def __init__(self, d: t.Dict[str, t.List[t.Any]]):
        """ Constructeur prenant un seul parametre
        - un dictionnaire
        - la clé du dictionnaire est une chaine de caractère
        - la valeur du dictionnaire est une liste contenant des elements de n'importe quel type
        - les attributs initialisés seront:
        - self.series_map, correspondra à un dictionnaire de type DitSeries
        - self.length, la longueur du DataFrame
        """


    def __getitem__(self, key: str) -> DitSeries:
        return self.series_map[key]

    def __setitem__(self, key: str, value: DitSeries) -> None:
        if key not in self.series_map:
            self.series_map[key] = DitSeries(key, {})
        for i, v in value.data.items():
            self[key].data[i] = v

    def __repr__(self):
        width = 5
        headers = " | ".join(header.rjust(width) for header in self.series_map)
        divider = "-" * len(headers)
        rows = tuple(
            " | ".join(
                str(self.series_map[k].data.get(i, "NaN")).rjust(width)
                for k in self.series_map
            )
            for i in range(self.length)
        )
        return "\n".join((headers, divider) + rows) + "\n"


if __name__ == "__main__":
    ds = DitSeries("serie", {0: 45, 1: 46, 2: 47})
    print(ds)     # <DitSeries: serie {0: 45, 1: 46, 2: 47}>

    ds2 = ds * 2
    print(ds2)    # <DitSeries: serie {0: 90, 1: 92, 2: 94}>

    ds3 = ds2 + 5
    print(ds3)    # <DitSeries: serie {0: 95, 1: 97, 2: 99}>

    ds4 = ds3 > 95
    print(ds4)   # <DitSeries: serie {0: False, 1: True, 2: True}>

    df = DitDataFrame(
        {
            "id": [18, 23, 11],
            "names": ["foo", "bar", "baz"],
            "weights": [42.3, 57.6, 89.1],
            "heights": [160, 192, 173],
        }
    )
    print(df)
# affiche le tableau suivant

#       id | names | weights | heights
#    ---------------------------------
#       18 |   foo |  42.3 |   160
#       23 |   bar |  57.6 |   192
#       11 |   baz |  89.1 |   173

    print(df.length)  # affiche 3

    names = df["names"]
    print(names)  # <DitSeries: names {0: 'foo', 1: 'bar', 2: 'baz'}>

    where = df["heights"] > 160
    print(df["names"][where])  # <DitSeries: names {1: 'bar', 2: 'baz'}>