# -*- coding: utf-8 -*-
import sys

import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import random
import csv


class GraphAnalysis:

    def __init__(self):
        self.nodes = set()
        self.edges = set()
        self.dimensions = dict()

        self.viz_nodes = list()
        self.viz_edges = list()
        self.table_selector_list = None
        self.shared_table_selector = None

    def get_random_color(self):
        color_list = [
            "rgba(31, 119, 180, 0.8)",
            "rgba(255, 127, 14, 0.8)",
            "rgba(44, 160, 44, 0.8)",
            "rgba(214, 39, 40, 0.8)",
            "rgba(148, 103, 189, 0.8)",
            "rgba(140, 86, 75, 0.8)",
            "rgba(227, 119, 194, 0.8)",
            "rgba(127, 127, 127, 0.8)",
            "rgba(188, 189, 34, 0.8)",
            "rgba(23, 190, 207, 0.8)",
            "rgba(31, 119, 180, 0.8)",
            "rgba(255, 127, 14, 0.8)",
            "rgba(44, 160, 44, 0.8)",
            "rgba(214, 39, 40, 0.8)",
            "rgba(148, 103, 189, 0.8)",
            "rgba(140, 86, 75, 0.8)",
            "rgba(227, 119, 194, 0.8)",
            "rgba(127, 127, 127, 0.8)",
            "rgba(188, 189, 34, 0.8)",
            "rgba(23, 190, 207, 0.8)",
            "rgba(31, 119, 180, 0.8)",
            "rgba(255, 127, 14, 0.8)",
            "rgba(44, 160, 44, 0.8)",
            "rgba(214, 39, 40, 0.8)",
            "rgba(148, 103, 189, 0.8)",
            "rgba(140, 86, 75, 0.8)",
            "rgba(227, 119, 194, 0.8)",
            "rgba(127, 127, 127, 0.8)",
            "rgba(188, 189, 34, 0.8)",
            "rgba(23, 190, 207, 0.8)",
            "rgba(31, 119, 180, 0.8)",
            "rgba(255, 127, 14, 0.8)",
            "rgba(44, 160, 44, 0.8)",
            "rgba(214, 39, 40, 0.8)",
            "rgba(148, 103, 189, 0.8)",
            "magenta",
            "rgba(227, 119, 194, 0.8)",
            "rgba(127, 127, 127, 0.8)",
            "rgba(188, 189, 34, 0.8)",
            "rgba(23, 190, 207, 0.8)",
            "rgba(31, 119, 180, 0.8)",
            "rgba(255, 127, 14, 0.8)",
            "rgba(44, 160, 44, 0.8)",
            "rgba(214, 39, 40, 0.8)",
            "rgba(148, 103, 189, 0.8)",
            "rgba(140, 86, 75, 0.8)",
            "rgba(227, 119, 194, 0.8)",
            "rgba(127, 127, 127, 0.8)"]

        return random.choice(color_list)

    def get_graph_components(self, file_path, header_list, delimiter):

        headers = dict()

        for header_position, header in enumerate(header_list, 1):
            headers[header_position] = header

        with open(file_path, "r") as f:
            reader = csv.reader(f, delimiter=delimiter)
            for i, line in enumerate(reader):

                source_db = line[0]
                source_obj = line[1]
                source_obj_kind = line[2]
                target_db = line[3]
                target_obj = line[4]
                target_obj_kind = line[5]

                # quality check: start
                line_is_valid = True
                bad_values = []

                for column_position, line_value in enumerate(line, 1):
                    if line_value == '':
                        line_is_valid = False
                        bad_values.append(headers.get(column_position))

                if line_is_valid is False:
                    continue
                # quality check: end

                source_node = "{}*{}*{}".format(source_db, source_obj, source_obj_kind)
                target_node = "{}*{}*{}".format(target_db, target_obj, target_obj_kind)

                if source_node not in self.nodes:

                    self.dimensions[source_node] = {
                        "db_name": source_db,
                        "object_name": source_obj,
                        "object_kind": source_obj_kind,
                        "node_name": source_node
                    }
                    self.nodes.add(source_node)

                if target_node not in self.nodes:
                    self.dimensions[target_node] = {
                        "db_name": target_db,
                        "object_name": target_obj,
                        "object_kind": target_obj_kind,
                        "node_name": target_node
                    }
                    self.nodes.add(target_node)

                self.edges.add((source_node, target_node))

    def prepare_vis_parts(self):

        self.name_mapping = dict()
        id_mapping = dict()
        colour_mapping = dict()

        for id, node_name in enumerate(self.dimensions, 0):
            self.viz_nodes.append(
                {
                    "db_name": self.dimensions[node_name]["db_name"],
                    "object_name": self.dimensions[node_name]["object_name"],
                    "object_kind": self.dimensions[node_name]["object_kind"],
                    "color": self.get_random_color(),
                    "value": 1,
                    "full_name": node_name,
                    "id": id
                }
            )

            self.name_mapping[node_name] = id
            id_mapping[id] = node_name
            colour_mapping[id] = self.get_random_color()

        for edge in self.edges:
            source, target = edge
            self.viz_edges.append(
                {
                    "source": self.name_mapping[source],
                    "target": self.name_mapping[target],
                    "value": 1,
                    "label": "{}->{}".format(source, target)
                }
            )

        self.table_selector_list = [{"label": "All values","value": "all_values"}] + [{'label': node, "value": self.name_mapping[node]} for node in self.nodes]

    def run_visualization(self, input_file):

        #input_file = "data/obj_dependency_data.csv"

        header_list = [
            "source_db",
            "source_obj",
            "source_obj_kind",
            "target_db",
            "target_obj",
            "target_obj_kind"
        ]

        delimiter = "|"
        self.get_graph_components(input_file, header_list, delimiter)
        self.prepare_vis_parts()

        # ---------------------------------------------------------

        styles = {
            'pre': {
                'border': 'thin lightgrey solid',
                'overflowX': 'scroll'
            }
        }

        external_stylesheets = ['https://codepen.io/amyoshino/pen/jzXypZ.css']

        app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

        app.layout = html.Div([
            html.H1('SQL Object Dependencies'),

            html.Div([

                html.Div([
                    "Object Name",
                    dcc.Dropdown(
                        id="tables",
                        options=self.table_selector_list,
                        multi=True,
                        value=[153, 154]
                    )],
                    className="six columns"
                ),
                html.Div([
                    "Mode",
                    dcc.Dropdown(
                        id="mode",
                        options=[
                            {"label": "Show Sources and Targets for selected objects", "value": 1},
                            {"label": "Show Sources for selected objects", "value": 2},
                            {"label": "Show Targets for selected objects", "value": 3},
                        ],
                        multi=False,
                        value=1
                    )],
                    className="two columns"
                ),

                html.Div([
                    "Arrangement",
                    dcc.Dropdown(
                        id="arrangement",
                        options=[
                            {"label": "Free", "value": "freeform"},
                            {"label": "Fixed", "value": "fixed"},
                            {"label": "Perpendicular", "value": "perpendicular"},
                            {"label": "Snap", "value": "snap"},
                        ],
                        multi=False,
                        value="fixed"
                    )],
                    className="two columns"
                ),

            ],
                className="row"
            ),

            html.Div(
                dcc.Graph(id='gr3', style={'height': '800px', 'width': '100%'}),
                className="row"
            ),

            html.Div([
                dcc.Markdown(("Click Data")),
                html.Pre(id='click-data', style=styles['pre']),
            ], className='row'),

        ],
            className="ten columns offset-by-one"
        )

        shared_table_selector = list()


        @app.callback(
            dash.dependencies.Output('click-data', 'children'),
            [
                dash.dependencies.Input('gr3', 'clickData'),
                dash.dependencies.Input("tables", "value")
            ]
        )
        def display_click_data(clickData, value):
            node_name = None
            if clickData:
                first_point = clickData["points"][0]

                if first_point.get("group", "+") != "+":
                    node_name = first_point["label"]

            if node_name is None:
                return

            else:
                return node_name



        @app.callback(
            dash.dependencies.Output("gr3", "figure"),
            [
                dash.dependencies.Input("tables", "value"),
                dash.dependencies.Input("mode", "value"),
                dash.dependencies.Input("arrangement", "value")
            ])
        def get(selector, mode, arrangement):

            self.shared_table_selector = selector

            global shared_table_selector
            shared_table_selector = selector

            link_source = list()
            link_target = list()
            link_value = list()
            link_label = list()

            if "all_values" not in selector:

                if mode == 1:

                    link_source = [link["source"] for link in self.viz_edges if
                                   link["source"] in selector or link["target"] in selector]

                    link_target = [link["target"] for link in self.viz_edges if
                                   link["source"] in selector or link["target"] in selector]

                    link_value = [link["value"] for link in self.viz_edges if
                                  link["source"] in selector or link["target"] in selector]

                    link_label = [link["label"] for link in self.viz_edges if
                                  link["source"] in selector or link["target"] in selector]

                elif mode == 2:

                    for node_id in selector:
                        link_source = link_source + [link["source"] for link in self.viz_edges if link["target"] == node_id]
                        link_target = link_target + [link["target"] for link in self.viz_edges if link["target"] == node_id]
                        link_value = link_value + [link["value"] for link in self.viz_edges if link["target"] == node_id]
                        link_label = link_label + [link["label"] for link in self.viz_edges if link["target"] == node_id]

                elif mode == 3:

                    for node_id in selector:
                        link_source = link_source + [link["source"] for link in self.viz_edges if link["source"] == node_id]
                        link_target = link_target + [link["target"] for link in self.viz_edges if link["source"] == node_id]
                        link_value = link_value + [link["value"] for link in self.viz_edges if link["source"] == node_id]
                        link_label = link_label + [link["label"] for link in self.viz_edges if link["source"] == node_id]

            else:

                link_source = [link["source"] for link in self.viz_edges][:200]
                link_target = [link["target"] for link in self.viz_edges][:200]
                link_value = [link["value"] for link in self.viz_edges][:200]
                link_label = [link["label"] for link in self.viz_edges][:200]

            return go.Figure(
                data=[
                    go.Sankey(
                        valueformat=".0f",
                        valuesuffix=" in tbls",
                        arrangement=arrangement,

                        # Define nodes
                        node=dict(
                            pad=20,
                            thickness=15,
                            line=dict(color="black", width=0.5),
                            label=[node["full_name"] for node in self.viz_nodes],
                            color=[node["color"] for node in self.viz_nodes],
                        ),

                        # Add links
                        link=dict(
                            source=link_source,
                            target=link_target,
                            value=link_value,
                            label=link_label
                        )
                    )
                ],
                layout={'clickmode': 'event+select'}
            )

        @app.callback(
            dash.dependencies.Output("tables", "value"),
            [
                dash.dependencies.Input('gr3', 'clickData')
            ]
        )
        def display_click_data(clickData):

            id = None

            if clickData:
                first_point = clickData["points"][0]

                node_name = None
                if first_point.get("group", "+") != "+":
                    node_name = first_point["label"]

                id = self.name_mapping.get(node_name, None)

            if self.shared_table_selector is None:
                self.shared_table_selector = [154, 153]

            if id is not None and id not in self.shared_table_selector:
                self.shared_table_selector.append(id)

            return self.shared_table_selector

        app.run_server(debug=True, host='0.0.0.0', port=8050)


if __name__ == '__main__':

    analysis = GraphAnalysis()
    analysis.run_visualization(sys.argv[1])
