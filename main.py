import earthkit
import earthkit.plots
import cartopy.crs as ccrs
import os
from datetime import datetime, timedelta

# 创建目标文件夹（如果不存在）
output_dir = "khanun_data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 从 CDS 获取 ERA5 再分析数据
source = 'cds'
dataset = 'reanalysis-era5-single-levels'

# 定义时间范围
start_time = datetime(2023, 7, 31, 2)
end_time = datetime(2023, 8, 12, 2)

# 循环遍历每个小时
current_time = start_time
while current_time <= end_time:
    year = current_time.strftime('%Y')
    month = current_time.strftime('%m')
    day = current_time.strftime('%d')
    time_str = current_time.strftime('%H:%M')
    
    print(f"正在处理 {year}-{month}-{day} {time_str} 的数据...")

    # 构建请求参数
    request = {
        'product_type': 'reanalysis',
        'variable': [
            '2m_temperature',
            'mean_sea_level_pressure',
            '10m_u_component_of_wind',
            '10m_v_component_of_wind',
        ],
        'year': year,
        'month': month,
        'day': day,
        'time': time_str,
    }

    # 加载数据
    data = earthkit.data.from_source(source, dataset, request)

    # 保存数据
    output_filename = f"era5_{current_time.strftime('%Y%m%d_%H%M')}.nc"
    data_path = os.path.join(output_dir, output_filename)
    data.save(data_path)
    print(f"数据已保存为: {output_filename}")

    # 向图形添加“卡努”所在区域的地图
    chart = earthkit.plots.Map(domain=[0, 50, 110, 150])

    # 使用我们偏好的单位绘制温度、压力和风速数据
    # 绘图样式来自样式库，并根据源数据的元数据进行选择
    temperature, pressure, u10, v10 = data
    chart.quickplot(temperature, units="celsius")
    chart.quickplot(pressure, units="hPa")
    chart.quiver(data)

    # 添加海岸线和图例
    chart.coastlines()
    chart.legend()

    # 添加标题，使用从源数据中提取元数据的格式字符串
    chart.title(
        "ERA5 hourly {variable_name!l} "
        "at {time:%H:%M} on {time:%d %B %Y}"
    )

    # 保存地图
    map_filename = f"era5_map_{current_time.strftime('%Y%m%d_%H%M')}.png"
    map_path = os.path.join(output_dir, map_filename)
    chart.save(map_path)
    print(f"地图已保存为: {map_filename}")

    # chart.show()  # 可选：注释掉以避免在循环中显示每张图

    # 移动到下一个小时
    current_time += timedelta(hours=1)

print("\n所有数据已处理完成！")