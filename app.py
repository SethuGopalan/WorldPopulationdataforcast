import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
import dash_auth



app = dash.Dash(__name__, plugins=[dl.plugins.pages],
                external_stylesheets=[dbc.themes.SLATE])
                


navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page['name'], href=page["path"])
            for page in dash.page_registry.values()
            if page['module'] != "page .not_found_404"
        ],
        nav=True,
        label="More Pages",
    ),
    brand='Wold Population data forcast ',
    color="primary",
    dark=True,
    className="mb-2"

)
app.layout = dbc.Container(
    [navbar, dl.plugins.page_container],
    fluid=True,
)
if __name__ == "__main__":
    app.run_server(debug=True,port=8052)
