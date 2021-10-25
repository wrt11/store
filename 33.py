import xlrd

xs = xlrd.open_workbook(filename=r"C:\Users\灵\Desktop\day07\任务\2020年每个月的销售情况.xlsx",encoding_override=True)

xs_len = len(xs.sheets())

zong_sales = 0
gross_sales = 0
annual_sales_dict = {}  # 每件衣服总销售量
yue_sales_dict = {}  # 每月总销量
unit_monthly_sales_dict = {}  # 每件每月销售额
unit_price_dict = {}  # 商品单价
jidu_sales = {"春": {}, "夏": {}, "秋": {}, "冬": {}}  # 季度单件销售量
for i in range(xs_len):
    st = xs.sheet_by_index(i)
    rows = st.nrows
    for j in range(1, rows):
        data = st.row_values(j)
        zong_sales += data[4]  # 总销量
        gross_sales += (data[2] * data[4])  # 总销售额
        name = data[1]
        if name not in unit_price_dict:
            unit_price_dict[name] = data[2]
        if i not in yue_sales_dict:
            yue_sales_dict[i] = data[4]
        else:
           yue_sales_dict[i] += data[4]  # 每月总销售量
        if name not in annual_sales_dict:
            annual_sales_dict[name] = data[4]
        else:
            annual_sales_dict[name] += data[4]
        if name not in unit_monthly_sales_dict:
            unit_monthly_sales_dict[name] = {i: data[4]}
        else:
            if i not in unit_monthly_sales_dict[name]:
                unit_monthly_sales_dict[name][i] = data[4]
            else:
                unit_monthly_sales_dict[name][i] += data[4]

zong_sales_sum = zong_sales  # 总销售量
# 总销售额
print("总销售额:")
print("总销售额为:", gross_sales)
print('\n')

# 每件衣服的销售占比
print("每件衣服的销售占比:")
for i in annual_sales_dict.keys():
    print(i, "的总销售占比为：", ((annual_sales_dict[i]) / zong_sales_sum) * 100, "%")
print('\n')

# 每件衣服的月销售量占比
print("每件衣服的月销售量占比:")
for i in unit_monthly_sales_dict.keys():
    print(i, "的月销售量占比如下：")
    for j in unit_monthly_sales_dict[i].keys():
        print(j + 1, "月的销售占比为：", (unit_monthly_sales_dict[i][j] / yue_sales_dict[j]) * 100, "%")
    print('\n')

# 每件衣服的销售额占比
print("每件衣服的销售额占比:")
for i in unit_price_dict.keys():
    print(i, "的总销售额占比为：", (unit_price_dict[i] * annual_sales_dict[i] / gross_sales) * 100, "%")
print('\n')

# 最畅销的衣服
print(annual_sales_dict)
print("最畅销的衣服:")
print(max(annual_sales_dict, key=annual_sales_dict.get), "共销售了：",
      annual_sales_dict[max(annual_sales_dict, key=annual_sales_dict.get)], "件")
print("\n")

# 每季度最畅销的衣服
for i in unit_monthly_sales_dict.keys():
    for j in unit_monthly_sales_dict[i].keys():
        if 1 <= j <= 3:
            if i not in jidu_sales["春"]:
                jidu_sales["春"][i] = unit_monthly_sales_dict[i][j]
            else:
                jidu_sales["春"][i] += unit_monthly_sales_dict[i][j]
        elif 4 <= j <= 6:
            if i not in jidu_sales["夏"]:
                jidu_sales["夏"][i] = unit_monthly_sales_dict[i][j]
            else:
                jidu_sales["夏"][i] += unit_monthly_sales_dict[i][j]
        elif 7 <= j <= 9:
            if i not in jidu_sales["秋"]:
                jidu_sales["秋"][i] = unit_monthly_sales_dict[i][j]
            else:
                jidu_sales["秋"][i] += unit_monthly_sales_dict[i][j]
        elif 10 <= j <= 11 or 0 <= j < 1:
            if i not in jidu_sales["冬"]:
                jidu_sales["冬"][i] = unit_monthly_sales_dict[i][j]
            else:
                jidu_sales["冬"][i] += unit_monthly_sales_dict[i][j]
for i in jidu_sales:
    print(i, "季最畅销的衣服为：", max(jidu_sales[i], key=jidu_sales[i].get), "共销售了：", jidu_sales[i][max(jidu_sales[i], key=jidu_sales[i].get)], "件")
print("\n")

# 全年销量最低的衣服是：
print("全年销量最低的衣服:")
print(min(annual_sales_dict, key=annual_sales_dict.get), "仅销售了：",
      annual_sales_dict[min(annual_sales_dict, key=annual_sales_dict.get)], "件")