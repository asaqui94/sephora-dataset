import dash_bootstrap_components as dbc
def Navbar():
     navbar = dbc.NavbarSimple(
           children=[
              dbc.NavItem(dbc.NavLink("Data", href="/data")),
              dbc.NavItem(dbc.NavLink("Cool Graph", href="/coolgraph")),
              dbc.DropdownMenu(
                 nav=True,
                 in_navbar=True,
                 label="Menu",
                 children=[
                    dbc.DropdownMenuItem("sephora.com"),
                    dbc.DropdownMenuItem("Email Me"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Create"),
                          ],
                      ),
                    ],
          brand="Home",
          brand_href="/home",
          sticky="top",
        )
     return navbar