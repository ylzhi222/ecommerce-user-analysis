# 🛍️ E-commerce 行为数据分析报告（EDA Summary）

> 基于 2019 年 10 月电商平台 4240 万条用户行为数据，完成用户活跃度、转化路径、留存率与用户价值分群等关键指标分析。

---

## 📅 1. 用户活跃度分析（DAU / WAU）

每日活跃用户数（DAU）与每周活跃用户数（WAU）如下图所示：

### 🔹 DAU（每日活跃用户）
![DAU](./full_dau.png)

### 🔹 WAU（每周活跃用户）
![WAU](./full_wau.png)

结论：
- 活跃用户在 10 月中旬达到高峰，峰值超 23 万人。
- 每周波动呈周期性，可能受到周末或促销节奏影响。

---

## 🔁 2. 行为事件趋势分析

![Event Trend](./full_event_trend.png)

用户行为中：
- 浏览事件每日超百万，远高于加购与购买；
- 转化路径中明显存在流失漏斗。

---

## 📉 3. 浏览 → 加购 → 购买 转化率

![Conversion Funnel](./full_conversion.png)

- 平均浏览转加购率（View → Cart）：约 1–2%
- 平均加购转购买率（Cart → Purchase）：60–120%，呈高波动（含异常天）

---

## 📈 4. 留存率分析（Retention）

![Retention Bar](./full_retention_bar.png)

- 平均次日留存率 Day‑1：9.82%
- 平均第 7 日留存率 Day‑7：4.55%
- 用户回访明显递减，需关注首日激活后的触达策略

---

## 🏷️ 5. 热门品牌 & 品类分析

### 🔸 Top 10 品牌
![Top Brands](./full_top_brands.png)

### 🔹 Top 10 类别
![Top Categories](./full_top_categories.png)

- electronics.smartphone 占比最大，品牌集中在 samsung / apple / xiaomi。
- 高价值人群集中在主流数码产品上，适合主打高单价和高复购品类。

---

## 👥 6. 用户价值分群（RFM）

### 📊 RFM 分群柱状图
![RFM Segments](./rfm_segments.png)

| Segment        | 用户数  | 洞察 / 建议                      |
|----------------|--------|-----------------------------------|
| Champions      | 47,709 | 重点维护，推送专属优惠和提前购资格 |
| Loyal          | 18,680 | 激励复购频率，建设会员成长体系     |
| Big Spenders   | 46,445 | 推高端新品，定期送出 VIP 礼遇       |
| Recent         | 57,625 | 发欢迎优惠券，引导完成首次复购      |
| Frequent       | 46,412 | 推积分兑换、捆绑销售提升客单        |
| High Revenue   | 21,320 | 推高单价礼包产品，开展感恩反馈活动    |
| Others         | 108,927| 尝试挽回，发送召回提醒或折扣促活    |

---

## ✅ 总结与建议

1. 用户首日留存仅 9.8%，建议通过欢迎推送、优惠激励提升首周活跃；
2. 大部分购买来自高价值人群，RFM 分群清晰，可做差异化运营；
3. 浏览量巨大但转化率偏低，漏斗优化空间大；
4. 推荐进一步挖掘：
   - Session 转化路径；
   - 不同分群用户的品类偏好；
   - 留存提升策略 AB 测试模拟。

📎 数据来源：[Kaggle - E-commerce Behavior Data](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)
