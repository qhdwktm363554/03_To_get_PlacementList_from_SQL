import pymssql, os
import pandas as pd
import math

# recipe_name = input("recipe_name: ")

#LINE HOST 정보
server_df = pd.read_excel("00_LINE_HOST_TABLE.xlsx")

line_name = input("line_name: ")
final_directory = input("final_directory: ")
host_name = server_df.loc[server_df["LINE"] == line_name,"HOST"]
#DB 정보
server = host_name.values[0]  # host_name이 object 형태로 값을 return 해서 value 값만 추출한거다. .item() 이것도 동일
username = 'sa'
password = 'Siplace%Sa.1.Pwd'
database = 'SIPLACEPro'

#RECIPE 이름 추출
CURRENT_DIR = os.getcwd()
list = os.path.join(CURRENT_DIR,'00_BOM_LIST.xlsx')
df = pd.read_excel(list)
# final_directory = "IBU1.0_NSMK"

for i in df['MLFB'].index:
    # recipe_name과 final_directory 입력
    recipe_name = df.loc[i, 'MLFB']

    sql_query1 = 'SELECT DISTINCT f.ObjectName, d.ObjectName, b.bstrRefDesignator,b.dOffsetX, b.dOffsetY, b.dAngle, b.bOmit FROM CPanel a\n\t\tLeft Outer Join CComponentPlacement as b ON a.spPlacementListRef = b.PID\n\t\tLeft Outer Join CComponent as c ON b.spComponentRef = c.OID\n\t\tLeft Outer Join AliasName as d ON c.OID = d.PID\n\t\tLeft Outer Join CFolder as e ON d.FolderID = e.OID\n\t\tLeft Outer Join AliasName as f ON a.spPlacementListRef = f.PID\nWHERE a.PID in (SELECT spPanelMatrix FROM CPanelLink WHERE PID IN (SELECT  a.PID FROM AliasName a LEFT OUTER JOIN CFolder b ON a.FolderID = b.OID WHERE a.ObjectName = \'A2C_PART#\' and b.bstrDisplayName= \'DIRECTORY\')) ORDER BY b.bstrRefDesignator'
    sql_query2 = sql_query1.replace("A2C_PART#", recipe_name)
    sql_query = sql_query2.replace("DIRECTORY", final_directory)

    # mssql 접속하고 connection으로부터 cursor를 생성
    cnxn = pymssql.connect(server, username, password, database)
    curs = cnxn.cursor()
    # sql문 실행문
    curs.execute(sql_query)
    row = curs.fetchall()
    # dataframe column 이름 설정
    Column_names = ['SMD#', 'Part#', 'Ref#', 'x', 'y', 'angle', 'omit']
    df2 = pd.DataFrame(row, columns=Column_names)
    df2['Angle_degree'] = df2['angle'] * 180/math.pi
    df2 = df2[['SMD#', 'Part#', 'Ref#', 'x', 'y', 'Angle_degree', 'omit']]
    cnxn.close()
    if df2.empty:
        print(recipe_name + " is EMPTY")
        break
    else:
        print("recipe_"+recipe_name+" is completed")
        df2.to_csv(recipe_name + ".csv", index=False, header=False)
print("END")






