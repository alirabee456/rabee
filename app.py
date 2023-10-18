

import plotly.express as px
import pandas as pd





data=pd.read_csv('https://raw.githubusercontent.com/alirabee456/deploy/main/sales.csv')




d1=data['Sales'].groupby(data['Product']).sum().reset_index().sort_values(by='Sales',ascending=True)






fig1=px.bar(d1,y='Product',x='Sales',title='sum of sales by product')
fig1.show()



d2=data['Discounts'].groupby(data['Discount Band']).sum().reset_index().iloc[0:3,:]





fig2=px.pie(d2,names='Discount Band',values='Discounts',title="sum of discount by dicount band")
fig2.show()




d3=data['Sales'].groupby(data['Country']).sum().reset_index()



def W(df):
    if df['Country']=='Canada':
        return 'CAN'
    elif df['Country']=='France':
        return 'FRA'
    elif df['Country']=='United States of America':
        return 'USA'
    elif df['Country']=='Germany':
        return 'DEU'
    else:
        return 'MEX'
d3['iso_alpha']=d3.apply(W,axis=1)






fig3=px.scatter_geo(d3,locations='iso_alpha',projection='orthographic',color='Country',hover_data='Sales',size='Sales',title='sum of sales by country')
fig3.show()




d4=data['Sales'].groupby(data['Date']).sum().reset_index()





fig4=px.line(d4,x='Date',y='Sales',title='sum of sales by month')
fig4.show()




d5=data['Profit'].groupby(data['Date']).sum().reset_index()
d5





fig5=px.line(d5,x='Date',y='Profit',title='sum of Profit by month')
fig5.show()




d6=data['Sales'].groupby(data['Segment']).sum().reset_index().sort_values(by='Sales',ascending=False)





fig6=px.bar(d6,x='Segment',y='Sales',title='sum of sales by Segment')
fig6.show()




total_sales=round((data['Sales'].sum()/1000000),2)





total_units=round((data['Units Sold'].sum()/100000),2)




total_cogs=round((data['COGS'].sum()/1000000),2)





total_profits=round((data['Profit'].sum()/1000000),2)






profits_percentage=round(((total_profits/total_sales)*100),2)








from dash import Dash, html, dcc





import dash_bootstrap_components as dbc
app=Dash(__name__)

app.layout=html.Div([
           html.H1("SalesDashboard",style={'text-align':'center'}),
           dbc.Card(dbc.CardBody([html.H4('sum of sales',className='card-title',style={'fontsize':'24px'}),
                                 html.H2(f"{total_sales}M")],style={'width':'18rem','position':'absolute',
                                                                   'top':'40px','left':'100px'})),
           dbc.Card(dbc.CardBody([html.H4('sum of units sold',className='card-title',style={'fontsize':'24px'}),
                                 html.H2(f"{total_units}M")],style={'width':'18rem','position':'absolute',
                                                                   'top':'40px','left':'400px'})),
    
           dbc.Card(dbc.CardBody([html.H4('sum of COGS',className='card-title',style={'fontsize':'24px'}),
                                 html.H2(f"{total_cogs}M")],style={'width':'18rem','position':'absolute',
                                                                   'top':'40px','left':'700px'})),
           dbc.Card(dbc.CardBody([html.H4('sum of profits',className='card-title',style={'fontsize':'24px'}),
                                 html.H2(f"{total_profits}M")],style={'width':'18rem','position':'absolute',
                                                                   'top':'40px','left':'1000px'})),
           dbc.Card(dbc.CardBody([html.H4('profits%',className='card-title',style={'fontsize':'24px'}),
                                 html.H2(f"{profits_percentage}%")],style={'width':'18rem','position':'absolute',
                                                                   'top':'40px','left':'1300px'})),
    
    
           dcc.Graph(figure=fig2,style={'width':'25%','height':'300px','position':'absolute',
                                                                   'top':'200px','left':'100',
                                                                     'borderRadius':'50px','padding':'10px'}),

           dcc.Graph(figure=fig3,style={'width':'25%','height':'300px','position':'absolute',
                                                                   'top':'200px','left':'700px',
                                                                     'borderRadius':'50px','padding':'10px'}),
           dcc.Graph(figure=fig4,style={'width':'25%','height':'300px','position':'absolute',
                                                                   'top':'200px','left':'1200px',
                                                                     'borderRadius':'50px','padding':'10px'}) ,
           dcc.Graph(figure=fig1,style={'width':'25%','height':'300px','position':'absolute',
                                                                   'top':'500px','left':'100px',
                                                                     'borderRadius':'50px','padding':'10px'}),
           dcc.Graph(figure=fig6,style={'width':'25%','height':'300px','position':'absolute',
                                                                   'top':'500px','left':'700px',
                                                                     'borderRadius':'50px','padding':'10px'}),
           dcc.Graph(figure=fig5,style={'width':'25%','height':'300px','position':'absolute',
                                                                   'top':'500px','left':'1200px',
                                                                     'borderRadius':'50px','padding':'10px'})
    
    
    
    
    
    
    
],style={'backgroundColor':'gold'}
)

if __name__=='__main__':
    app.run(port=8050)


