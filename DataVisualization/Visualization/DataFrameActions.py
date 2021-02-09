import pandas as pd
from Visualization.BarClass import BarClass

class DataFrameActions():
    @staticmethod
    def PrepareDataFrame(bars):
        names = []
        manual = []
        automated = []

        for bar in bars:
            names.append(bar.headFolderdName)
            manual.append(bar.countManualTestCases)
            automated.append(bar.countAutomatedTestCases)

        df = pd.DataFrame({
            'Factor': names,
            'manual': manual,
            'automated': automated
        })

        tidyData = df.melt(id_vars='Factor').rename(columns=str.title)
        return tidyData