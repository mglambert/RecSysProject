import pandas as pd
import numpy as np
from itertools import cycle


class VotingMethods:

    @staticmethod
    def plurality_voting(df: pd.DataFrame) -> str:
        """
        Elige el ítem que es calificado como el mejor más a menudo.
        En caso de empate, devuelve el primer ítem encontrado.
        """
        max_items = df.idxmax(axis=1)
        return max_items.mode()[0]

    @staticmethod
    def average(df: pd.DataFrame) -> pd.Series:
        """
        Promedia las calificaciones individuales para cada ítem
        """
        return df.mean(axis=0)

    @staticmethod
    def multiplicative(df: pd.DataFrame) -> pd.Series:
        """
        Multiplica las calificaciones individuales para cada ítem.
        """
        return df.prod(axis=0)

    @staticmethod
    def borda_count(df: pd.DataFrame) -> pd.Series:
        """
        Calcula el puntaje Borda para cada ítem.
        Los ítems se clasifican para cada usuario y se asignan puntos.
        """
        num_items = len(df.columns)
        ranks = df.rank(axis=1, method='average', ascending=False)
        borda_points = num_items - ranks
        return borda_points.sum(axis=0)

    @staticmethod
    def copeland_score(df: pd.DataFrame) -> pd.Series:
        """
        Para cada ítem, cuenta las victorias por mayoría paritaria menos las derrotas.
        """
        items = df.columns
        scores = pd.Series(0, index=items)
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                item1 = items[i]
                item2 = items[j]

                item1_wins = (df[item1] > df[item2]).sum()
                item2_wins = (df[item2] > df[item1]).sum()

                if item1_wins >= item2_wins:
                    scores[item1] += 1
                    scores[item2] -= 1
                elif item2_wins > item1_wins:
                    scores[item2] += 1
                    scores[item1] -= 1
        return scores

    @staticmethod
    def approval_voting(df: pd.DataFrame, threshold: float = 6) -> pd.Series:
        """
        Cuenta cuántas calificaciones están por encima de un umbral de aprobación.
        """
        return (df > threshold).sum(axis=0)

    @staticmethod
    def least_misery(df: pd.DataFrame) -> pd.Series:
        """
        Toma el mínimo de las calificaciones individuales para cada ítem.
        """
        return df.min(axis=0)

    @staticmethod
    def most_pleasure(df: pd.DataFrame) -> pd.Series:
        """
        Toma el máximo de las calificaciones individuales para cada ítem.
        """
        return df.max(axis=0)

    @staticmethod
    def average_without_misery(df: pd.DataFrame, threshold: float=4) -> pd.Series:
        """
        Promedia las calificaciones, excluyendo ítems con cualquier calificación
        por debajo de un umbral.
        """
        items_to_keep = df.columns[(df >= threshold).all(axis=0)]
        return df[items_to_keep].mean(axis=0)

    @staticmethod
    def fairness(df: pd.DataFrame, user_order: list) -> list:
        """
        Clasifica los ítems haciendo que los usuarios elijan por turnos.
        En caso de empate en la calificación de un usuario, se elige el
        primer ítem según el orden de las columnas.
        """
        available_items = df.columns.tolist()
        selection_order = []
        user_cycle = cycle(user_order)

        while available_items:
            current_user = next(user_cycle)
            user_ratings = df.loc[current_user, available_items]
            best_item = user_ratings.idxmax()
            selection_order.append(best_item)
            available_items.remove(best_item)

        return selection_order

    @staticmethod
    def most_respected_person(df: pd.DataFrame, user: str) -> pd.Series:
        """
        Utiliza únicamente las calificaciones del individuo más respetado.
        """
        if user not in df.index:
            raise ValueError(f"User '{user}' not found in DataFrame index.")
        return df.loc[user]


if __name__ == '__main__':
    data = {
        'A': [10, 1, 10], 'B': [4, 9, 5], 'C': [3, 8, 2],
        'D': [6, 9, 7], 'E': [10, 7, 8], 'F': [9, 9, 8],
        'G': [6, 6, 5], 'H': [8, 9, 6], 'I': [10, 3, 7],
        'J': [8, 8, 6]
    }
    users = ['Pedro', 'Juan', 'Diego']
    a = pd.DataFrame(data, index=users)
