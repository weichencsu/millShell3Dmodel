import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, date
#import plotly.graph_objects as go
import pandas as pd
#import pytz
import requests
#import pyecharts.options as opts
#from pyecharts.charts import Gauge
# mapbox_access_token = open(".mapbox_token").read()
#def SMOOTH_CURVE(data, window):
#    yhat = savgol_filter(data, window, 3)
#    return yhat

#@st.cache(persist=True)
def read_file_from_url(url):
    return requests.get(url).content


def serieschart_plot(df):
    # plot time sereis chart
    #dtm = []
    #wl = []

    #for df in sensorSeri:
    #    dtm_tmp, wl_tmp = WEAR_DATA_PARSE(df)
    #    dtm.append(dtm_tmp)
    #    wl.append(wl_tmp)

    # wl = SMOOTH_CURVE(wl, 21)
    #np.savetxt("wearData.csv", wl, delimiter=",")
    fig2 = go.Figure()
    config = {'displayModeBar': False}
    fig2.add_trace(
        go.Scatter(x=df["日期"], y=df["磨损传感器"],
                   line=dict(color='royalblue', width=5),
                   name="Underflow Pipe Wear Sensor Current Diameter - [mm]"
                   )
    )

    #margin=dict(l=5, r=5, t=5, b=5),

    fig2.update_xaxes(showline=True,
    linewidth=1,
    linecolor='black',
    mirror=True)

    fig2.update_yaxes(showline=True,
    linewidth=1,
    linecolor='black',
    mirror=True)

    fig2.update_layout(
        xaxis_title="Date",
        yaxis_title="Current Sensor Thickness - [mm]",
        yaxis_range=[100, 150],
        autosize=False,
        #width=1600,
        height=600,
        showlegend=False,
        margin=dict(l=10, r=10, t=10, b=10),
        font=dict(
            family="sans serif, regular",
            size=14,
            color="Black"
        )
    )
    #fig2.write_html("timeSeriesSensor.html", config=config)
    return fig2

def WEAR_DATA_PARSE(wf):
    date = wf.split('.txt')[0].split('/')[-1].split('_')[0]
    # hours, minutes, secends = wf.split('.txt')[0].split('_')[1].split('-')
    hours, minutes, secends = wf.split('.txt')[0].split(date)[1].split('_')[1].split('-')
    dtm_obj = date + ' ' + hours + ':' + minutes + ':' + secends
    with open(wf) as f:
        lines = f.readlines()
    wl_obj = int(lines[9].split('\n')[0]) - 2
    ss_obj = int(lines[4].split('\n')[0])
    return dtm_obj, wl_obj, ss_obj

#@st.cache(persist=True)
#def local_pvModel(file_name):
#    st.markdown(
#            f'<iframe src=' + file_name + ' height = "600" width = "100%"></iframe>',
#            unsafe_allow_html=True,
#    )


def main():
    st.set_page_config(page_title="Oresome IoT", layout="wide", initial_sidebar_state='auto')
    st.markdown(
            f"""
            <style>
                .reportview-container .main .block-container{{
                    max-width: 1600px;
                    padding-top: 1rem;
                    padding-right: 1rem;
                    padding-left: 1rem;
                    padding-bottom: 1rem;
                }}

                .fullScreenFrame > div {{
                    display: flex;
                    justify-content: left;
                }}
            </style>
            """,
            unsafe_allow_html=True,
        )
    #page = st.markdown(
    ##            f"""
    #            <style>
    #            .stApp {{
    #                background: url("https://kycg.s3.ap-east-1.amazonaws.com/sidebarBG.png");
    #                background-size: cover
    #            }}
    #            </style>
    #            """,
    #            unsafe_allow_html=True,
    #)

    # define files dir for all inputs
    #     cwd = os.getcwd()
    #cwd = "E:\\2项目资料\\耐普云平台demo"
    #sensorDataDir = 'UDP/'

    #df1 = pd.read_csv("https://raw.githubusercontent.com/oresome/dexing34ftsag/main/sensorThickness.csv")
    #df1 = pd.read_csv("sensorThickness.csv")
    #today = date(2023, 3, 14)

    #df1['日期'] = pd.to_datetime(df1['日期'], format="%d/%m/%Y")
    #mask = df1['日期'].dt.date == today
    #filterDF = df1.loc[mask]

    #sensen1_data = int(filterDF["磨损传感器"].iloc[0])
    #sensen2_data = int(filterDF["Sensor2"].iloc[0])
    #sensen3_data = int(filterDF["Sensor3"].iloc[0])
    #sensen4_data = 0
    #datindex = filterDF.index
    #filterDF_plot = df1.loc[:datindex[0]]
    #filterDF_plot = df1.loc[:]


    ###  第一部分  模型展示  ###
    top = st.container()
    with top:
        colll1, colll3 = st.columns([5,1])
        with colll1:
            st.title("Mill Shell Liner Wear Monitoring System - 3D Printed Model")
            st.header("One Shell Liner with Bolt Hole Wear Sensor Insert")
            st.header("One shell liner with Multiple Wear Sensor Fusion Insert")
            #st.title("云南驰宏锌锗-会泽矿业")
            #st.subheader("当前状态（在运行） ")

        #with colll3:
        #    st.markdown("###")
        #    st.image("logo.png")



    #st.markdown("###")
    st.markdown("----------------------------------")
    #col1, col2, col3 = st.columns(3)
    #with col1:
    st.subheader("Bills of Materials for 3D Assembly")
    #current_thickness1 = str(sensen1_data) + " mm"
    #delta_thickness1 = str(sensen1_data-133) + " mm"
    #hktimez = pytz.timezone("Asia/Hong_Kong") 
    #timenowhk = datetime.now(hktimez)
    #lastDate = date(2023, 3, 14)
    #st.markdown("Latest Sensor Reporing Time: " + lastDate.strftime('%Y-%m-%d'))
    #st.metric(label="Current State:", value=current_thickness1, delta=delta_thickness1)
    df = pd.read_csv("partList.csv")
    st.dataframe(
        df,
        hide_index=True,
        use_container_width = True,
        height = 700
    )


        #with col4:
    #with col3:
    #    # echats
    #    PLOT_GAUGE(3.4)
    #    HtmlFile = open("gauge_base.html", "r", encoding='utf-8')
    #    source_code_2 = HtmlFile.read()
    #    components.html(source_code_2, height=400)
        
    
    
    #installDate = date(2022, 9, 19)
    #currentDate = date(2023, 3, 14)
    #deltaDays = (currentDate - installDate).days
    #st.subheader("Installed Date: " + installDate.strftime('%Y-%m-%d'))
    #st.subheader("Completed Date: " + currentDate.strftime('%Y-%m-%d'))
    #st.subheader("Total Campaign Days: " + str(deltaDays) + " Days")
    st.markdown("_______________________________________________________________________")
    #pyLogo = Image.open("install.png")
    st.subheader("Web Interactive 3D Model")
    #st.info("如果您正在使用微软EDGE浏览器或谷歌Chrome浏览器，浏览器的设置可能会导致您无法预览三维模型。如需预览，请更换为火狐浏览器，或者请在当前浏览器：设置->Cookie和网站权限->Cookie 和已存储数据/ Cookie 和网站数据->阻止第三方 Cookie ，选项关闭，并刷新页面！")
    #HtmlFile_tSS1 = open("dexxxing.html", 'r', encoding='utf-8').read()
    #components.html(HtmlFile_tSS1, height=500)
    #imgcol1, imgcol2, imgcol3 = st.columns(3)
    #with imgcol1:
    ##im1 = Image.open("install.png")
    #st.image(im1)
    #with imgcol2:
    #    im2 = Image.open("photos/image2.jpg")
    #    st.image(im2)
    #with imgcol3:
    #    im3 = Image.open("photos/image3.jpg")
    #    st.image(im3)
    #@st.cache
    #st.markdown("建设中，敬请期待！")
    iframeLINK = "https://kitware.github.io/glance/app/?name=millShellWearMonitoring.vtkjs&url=https://webify-1306024390.cos.ap-shanghai.myqcloud.com/millShellWearMonitoring.vtkjs"
    #local_pvModel(iframeLINK)
    #pvOBJ = read_file_from_url(iframeLINK)
    #components.html(pvOBJ, height=1000)
    
    #HtmlFile_tSS1 = open("hydrocyclone.html", 'r', encoding='utf-8').read()
    #components.html(HtmlFile_tSS1, height=1000)

    st.write(
            f'<iframe src=' + iframeLINK + ' height = "1200" width = "100%"></iframe>',
            unsafe_allow_html=True,
    )
    #st.markdown("_______________________________________________________________________")

    ###  第三部分  磨损趋势  ###
    #st.subheader("Wear Data History")
    #df = pd.read_csv("sensorThickness.csv")
    #plotlyfig = serieschart_plot(filterDF_plot)

    #st.plotly_chart(plotlyfig, theme="streamlit", use_container_width=True)

    #st.subheader("Time Series Wear History")
    #HtmlFile_tSS = open("timeSeriesSensor.html", 'r', encoding='utf-8').read()
    #components.html(HtmlFile_tSS, height=800)


    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


    footer = """  
            <style>
                .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #50575b;
                color: white;
                text-align: center;
                }
            </style>

            <div class="footer">
                <p>All company names, logos, product names, and identifying marks used throughout this website are the property of their respective trademark owners. Visit us @ www.oresome.com.cn<br></p>
            </div>
        """

    st.markdown(footer,unsafe_allow_html=True)



if __name__ == "__main__":
    main()











