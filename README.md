# 🛒 电商用户行为分析项目

本项目基于一个大型多品类线上商城的用户行为数据（含 4200 万行原始记录），完成了用户活跃、转化、留存与用户价值分层的全面分析，并通过交互式 Streamlit 看板完成结果可视化。

---

### 📂 数据说明

本项目未包含原始数据文件（因体积超过 GitHub 限制），请前往以下链接下载：

👉 [数据集地址 - Kaggle](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)

下载后请将所需 CSV 文件（如 `2019-Oct.csv.gz`）放置于项目根目录的 `data/` 文件夹中。

也可以使用 `output/cleaned_data_sample.csv` 进行快速体验。

---

## 📌 项目亮点

* **数据规模**：4200 万条行为日志（浏览、加购、购买）
* **技术栈**：Python · Pandas · DuckDB · Streamlit · Matplotlib · Seaborn
* **核心分析功能**：

  * DAU / WAU 活跃度分析
  * 漏斗分析（浏览 → 加购 → 购买）
  * 用户留存分析（次日、7日留存）
  * RFM 用户价值分群
  * 可交互 Streamlit 数据可视化看板

---

## 📁 项目结构

```text
ecommerce_behavior_analysis/
├── data/ # 存放原始 CSV 数据（可包含多个月份）
│ ├── 2019-Oct.csv
│ ├── 2019-Oct.csv.gz
│ └── 2019-Nov.csv
│
├── notebooks/ # Jupyter Notebook 分析脚本
│ ├── 01_eda_cleaning.ipynb # 样本清洗与数据预览
│ ├── 02_basic_eda.ipynb # 样本级 EDA 分析（活跃、转化、品类）
│ └── 03_full_analysis_duckdb.ipynb # DuckDB 全量分析（留存、RFM）
│
├── output/ # 输出文件（中间数据与图表）
│ ├── cleaned_data_sample.csv # 样本数据（10 万条）
│ ├── rfm_segments.csv # 全量 RFM 分群结果
│ ├── figures/ # 样本EDA图表文件
│ └── figures_full/ # 全量图表文件
│
├── reports/
│ └── EDA_summary.md # Markdown 格式的项目报告摘要
│
├── streamlit_dashboard.py # 可交互数据看板（Streamlit）
├── requirements.txt # 项目依赖包列表
└── README.md # 项目说明文档（本文件）
```

---

## 🔍 核心分析说明

### 1. 👥 活跃用户分析

* DAU / WAU 趋势图识别活跃增长与业务高峰

### 2. 🔄 用户行为漏斗

* 计算 view → cart → purchase 的转化率
* 分析用户在各行为节点的流失情况

### 3. 📈 用户留存分析

* Cohort 分组留存率矩阵
* 次日留存、7日留存统计

### 4. 💎 RFM 用户价值分群

* 根据 R（最近一次购买）、F（频率）、M（金钱） 打分
* 自动分为 7 类：

  * Champions
  * Loyal
  * Recent
  * Big Spenders
  * Frequent
  * High Revenue
  * Others（沉默用户）

---

## 📊 Streamlit 看板

交互式仪表盘，功能包含：

* 日期选择器（Sidebar）
* 活跃用户趋势（DAU / WAU）
* 行为事件趋势图（浏览 / 加购 / 购买）
* 转化漏斗变化曲线
* RFM 分群柱状分布图（读取自全量分析 CSV）

运行命令：

```bash
streamlit run streamlit_dashboard.py
```

---

## 📈 图表示例（部分截图见 `/output/figures_full/`）

* DAU 趋势图
* 转化率漏斗图
* 留存矩阵
* RFM 分群分布

---

## 📦 项目依赖环境

```text
pandas
numpy
matplotlib
seaborn
duckdb
streamlit
```
