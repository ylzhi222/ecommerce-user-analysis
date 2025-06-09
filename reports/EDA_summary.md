# 🛍️ E-commerce 行为数据分析报告（EDA Summary）

> 基于 2019 年 10 月电商平台 4240 万条用户行为数据，完成用户活跃度、转化路径、留存率与用户价值分群等关键指标分析。

---

## 📅 1. 用户活跃度分析（DAU / WAU）

每日活跃用户数（DAU）与每周活跃用户数（WAU）如下图所示：

### 🔹 DAU（每日活跃用户）
![image](https://github.com/user-attachments/assets/c0e030af-77e5-41d9-bbfd-5241316c22a9)


### 🔹 WAU（每周活跃用户）
![image](https://github.com/user-attachments/assets/aa295892-3312-4805-90fc-2ed04c797ada)


结论：
- 活跃用户在 10 月中旬达到高峰，峰值超 23 万人。
- 每周波动呈周期性，可能受到周末或促销节奏影响。

---

## 🔁 2. 行为事件趋势分析

![image](https://github.com/user-attachments/assets/a6bd01d8-24e5-49bf-b296-e7d6cf25597b)


用户行为中：
- 浏览事件每日超百万，远高于加购与购买；
- 转化路径中明显存在流失漏斗。

---

## 📉 3. 浏览 → 加购 → 购买 转化率

![image](https://github.com/user-attachments/assets/192b97ca-ba31-46dd-b28e-34027f425320)


- 平均浏览转加购率（View → Cart）：约 1–2%
- 平均加购转购买率（Cart → Purchase）：60–120%，呈高波动（含异常天）

---

## 📈 4. 留存率分析（Retention）

![image](https://github.com/user-attachments/assets/c597be73-f16d-4150-b0b9-df0f6d4631d4)


- 平均次日留存率 Day‑1：9.82%
- 平均第 7 日留存率 Day‑7：4.55%
- 用户回访明显递减，需关注首日激活后的触达策略

---

## 🏷️ 5. 热门品牌 & 品类分析

### 🔸 Top 10 品牌
![image](https://github.com/user-attachments/assets/c1f3cd6f-d48e-42eb-89e5-a90b16176954)


### 🔹 Top 10 类别
![image](https://github.com/user-attachments/assets/1497e582-347e-4b00-a879-c6f3041bba8e)


- electronics.smartphone 占比最大，品牌集中在 samsung / apple / xiaomi。
- 高价值人群集中在主流数码产品上，适合主打高单价和高复购品类。

---

## 👥 6. 用户价值分群（RFM）

### 📊 RFM 分群柱状图
![image](https://github.com/user-attachments/assets/81d0cc3d-451e-4303-ae4f-86dd47d62195)


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
