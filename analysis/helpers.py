import panel_highcharts as ph
import panel as pn
pn.extension('highchart')

from analysis.models import  AnalysisResults, NewAnalysis

def update_analysis_results(df):
    for index, row in df.iterrows():
        AnalysisResults.objects.update_or_create(
        sample_ID=row['sample_ID'],
        drugClass=row['drugClass'],
        drugName=row['drugName'],
        drugScore=row['drugScore'], 
        susceptibility=row['susceptibility'],
        project_ID=NewAnalysis.objects.get(project_ID=row['project_ID']), #take note of how to handle foreign keys in django
        )

# function to create highcharts
def charts():
    configuration = {
        "title": {"text": "Line Chart Pane"},
        "series": [
            {
                "name": "Sales",
                "data": [100, 250, 150, 400, 500],
            }
        ]
    }
    chart = ph.HighChart(object=configuration, sizing_mode= "stretch_width")
    settings = pn.WidgetBox(
        pn.Param(
            chart,
            parameters=["height", "width", "sizing_mode", "margin", "object", "event", ],
                    widgets={"object": pn.widgets.LiteralInput, "event": pn.widgets.StaticText},
            sizing_mode="fixed", show_name=False, width=250,
        )
    )
    pn.Row(settings, chart, sizing_mode="stretch_both")

    return pn