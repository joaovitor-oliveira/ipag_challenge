import pandas as pd


class Sales:

    def __init__(self, file_path: str) -> None:
        self.__file_path = file_path
        self.__dataframe = None
        self.load_file()

    def load_file(self) -> bool:
        try:
            self.__dataframe = pd.read_csv(self.__file_path)
            return True
        except FileNotFoundError as error:
            print(f"Arquivo não encontrado. Caminho informado: {error.filename}")

    def sample(self) -> pd.DataFrame:
        '''Get a sample of data'''
        return self.__dataframe.sample().transpose()

    def get_units_sold_by_item_type(self) -> pd.DataFrame:
        '''Returns the number of units sold group by item type'''
        return self.__dataframe.groupby("Item Type")["Units Sold"].sum()

    def get_total_revenue_by_item_type(self) -> pd.DataFrame:
        '''Returns the total revenue group by item type'''
        return self.__dataframe.groupby("Item Type")["Total Revenue"].sum()

    def get_total_cost_by_item_type(self) -> pd.DataFrame:
        '''Returns the total cost group by item type'''
        return self.__dataframe.groupby("Item Type")["Total Cost"].sum()

    def get_total_profit_by_item_type(self) -> pd.DataFrame:
        '''Returns the total profit group by item type'''
        return self.__dataframe.groupby("Item Type")["Total Profit"].sum()

    def get_unit_solds_by_item_type_and_region(self) -> pd.DataFrame:
        '''Returns the number of units sold group by item type and region'''
        return self.__dataframe.groupby(["Item Type", "Region"])["Units Sold"].sum()

    def get_item_type_with_highest_revenue_by_country(self) -> pd.DataFrame:
        country_type_total_revenue = self.__dataframe.groupby(["Country", "Item Type"])["Total Revenue"].sum()
        selection = country_type_total_revenue.groupby("Country").idxmax()
        return country_type_total_revenue[selection]
