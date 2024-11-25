# ======================================================================
# homepage 初步组合导航栏和功能模块，虽然功能模块嵌入了导航栏里面，但很好看，可以作为版本 1
# ======================================================================
import streamlit as st
import streamlit.components.v1 as components

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css">
    <style>
        html, body {
            height: 100%;
            width: 100%;
            margin: 0;
            padding: 0;
            font-family: Roboto, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            overflow: hidden;
            background: linear-gradient(to top right, #2c3338 65%, #FF4E88);
        }
        .main-header {
            width: 100vw;
            height: 25vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;
            padding-left: 18%;  /* 增大左侧内边距，右移整体内容 */
        }

        /* Data Nexus 网站名 */
        .main-header h1 {
            position: absolute;
            top: 120px; /* 距离页面顶部 */
            font-size: 4em;
            margin: 0;
            text-shadow: 1px 1px 3px #000000;
        }

        /* 页面右上角的网页浓缩介绍 */
        .top-right-info {
            position: absolute;  
            top: 80px; /* 距离页面顶部 */
            right: 30px; /* 距离页面右侧 */
            width: 600px; /* 容器宽度 */
            color: #fff;
            padding: 15px;
            border-radius: 8px;
            font-size: 1.1em;
            line-height: 1.8; /* 行间距 */
        }

        .main-header h1 span {
            color: #FDF5E6;
        }
        .main-header h1 .highlight {
            color: #FF4E88;
        }

        /* Data Nexus 下面的标语 Unlock the Power of Data*/
        .main-header p {
            position: absolute;
            top: 190px; /* 距离页面顶部 */
            font-size: 1.2em;
            margin: 10px 0;
            color: #eee;
            font-style: italic;
        }

        /* getting started 按钮 */
        .cta-button {
            position: absolute;
            background: linear-gradient(to right, #ff6aa5, #ea4c88);
            color: #fff;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            margin-top: 20px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .cta-button:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 15px rgba(234, 76, 136, 0.4);
        }
        .content-sections {
            width: 90%;
            display: flex;
            justify-content: space-around;
            margin-top: -30px;
            gap: 15px;
            flex-wrap: wrap;
        }
        .section {
            width: 27%;
            height: 580px;  /* 设置每个模块的固定高度为 n 像素 */
            background: #444;
            color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease;
            margin-bottom: 20px;
            transform: translateY(-100px); /* 向上移动 20px */
        }
        .section:hover {
            transform: translateY(-100px) scale(1.05);
        }
        .section h2 {
            color: #FF4E88;
            margin-bottom: 10px;
        }
        .section p {
            font-size: 1em;
            line-height: 1.8; /* 增加行间距 */
            margin-bottom: 5px; /* 增加段落间距 */
        }

        /* 插图样式 */
        .module-image {
            width: 100%;
            max-height: 300px;
            object-fit: cover;
            margin-top: 10px;
            border-radius: 8px;
        }
    </style>
</head>

<body>
    <header id="app-header" class="main-header">
        <h1>
            <span>Data</span> 
            <span class="highlight">Nexus</span>
        </h1>
        <p><strong>Unlock the Power of Data</strong></p>
        <button class="cta-button">Getting Started</button>
    </header>

    <!-- 添加右上角文字描述 -->
    <div class="top-right-info">
        <p><strong>· Simplifying the data workflow for everyone.</strong></p>
        <p><strong>· Transforming complex data into actionable insights.</strong></p>
        <p><strong>· Built on Python's powerful libraries</strong></p>
        <p><strong>· From datasets to decisions – fast, flexible, and smart.</strong></p>
    </div>

    <div class="content-sections">
        <div class="section">
            <h2>Exploring</h2>
            <p>Gain insights into data structure, patterns, and inconsistencies.</p>
            <p>
                <strong>Applications:</strong> Initial data profiling, outlier detection, descriptive statistics.
                <br>
                <strong>Methods:</strong> Exploratory data analysis (EDA), data summarization, anomaly detection, and more...
            </p>
            <!-- 使用 Google Drive 存好的图片 -->
            <img src="https://seaborn.pydata.org/_images/scatterplot_matrix.png" alt="Exploring Data" class="module-image">
        </div>
        <div class="section">
            <h2>Proccessing</h2>
            <p>Simplify messy data to make it usable and reliable.</p>
            <p>
                <strong>Applications:</strong> Data cleaning, normalization, encoding categorical variables.
                <br>
                <strong>Methods:</strong> Missing value imputation, one-hot encoding, scaling, and feature engineering, and more...
            </p>
            <!-- 使用 Google Drive 存好的图片 -->
            <img src="https://seaborn.pydata.org/_images/strip_regplot.png" alt="processing" class="module-image", style="height: 300px;">
        </div>
        <div class="section">
            <h2>Modeling</h2>
            <p>Build predictive models and uncover patterns in your data. </p>
            <p>
                <strong>Applications:</strong> Predictive analytics, customer segmentation, trend forecasting.
                <br>
                <strong>Methods:</strong> Supervised and unsupervised learning, decision trees, neural networks, k-means, and more...
            <!-- 使用 Google Drive 存好的图片 -->
            <img src="https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_digits_thumb.png" alt="modeling" class="module-image", style="max-width: 380px; height: 360px;">
            </p>
        </div>
        <div class="section">
            <h2>Visualizing</h2>
            <p>Present data and insights effectively with clear and interactive visuals. </p>
            <p>
                <strong>Applications:</strong> Dashboard creation, report generation.
                <br>
                <strong>Methods:</strong> Charts, interactive dashboards using libraries like plotly, pygwalker and more...
            </p>
            <!-- 使用 Google Drive 存好的图片 -->
            <img src="https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_qda_001.png" alt="visualizing" class="module-image", style="height: 340px;">
        </div>
        <div class="section">
            <h2>Business Analysis</h2>
            <p>Turn data into actionable strategies with advanced analytics. </p>
            <p>
                <strong>Applications:</strong>  Includes commonly used business models in analytics.
                <br>
                <strong>Methods:</strong> Funnel analysis, RFM modeling, and A/B testing, Matrix、Retention analysis, and more...
            </p>
            <!-- 使用 Google Drive 存好的图片 -->
            <img src="https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_002.png" alt="visualizing" class="module-image", style="height: 340px;">
        </div>
        <div class="section">
            <h2>Tutorials and Support</h2>
            <p>Access step-by-step guides and community-driven solutions to master data workflows.</p>
            <p>
                <strong>Applications:</strong> Learning new techniques, solving challenges, sharing knowledge.
                <br>
                <strong>Methods:</strong> Code examples, video tutorials, forums, and expert advice, and more...
            </p>
        </div>
    </div>

</body>
</html>
"""

html_footer = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Footer with Bubbles</title>
    <style>
        /* 提供的 CSS 样式 */
        .body_footer {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            margin: 0;
            overflow-x: hidden;
            background: linear-gradient(to top right, #2c3338 65%, #FF4E88);
            font-family: 'Open Sans', sans-serif;
        }
        .main {
            flex: 1;
        }
        .footer {
            z-index: 1;
            /*尝试过的还行颜色：#ED5565*/
            --footer-background: #e34b7e;
            position: relative;
            min-height: 12rem;
            width: 100%;
            bottom: 0;
            box-sizing: border-box;
        }
        .bubbles {
            z-index: 1;
            position: absolute;
            top: -2px;
            left: 0;
            right: 0;
            height: 1rem;
            background: var(--footer-background);
            filter: url("#blob");
        }
        .bubbles .bubble {
            position: absolute;
            left: var(--position, 50%);
            background: var(--footer-background);
            border-radius: 100%;
            animation: bubble-size var(--time, 4s) ease-in infinite var(--delay, 0s),
                bubble-move var(--time, 4s) ease-in infinite var(--delay, 0s);
            transform: translate(-50%, 100%);
        }
        .content_footer {
            position: relative; /* 确保内容在泡泡之上显示 */
            z-index: 2;
            display: grid;
            grid-template-columns: 1fr auto;
            grid-gap: 4rem;
            padding: 2rem;
            background: var(--footer-background);
            width: 100%;
            box-sizing: border-box;
        }
        .content_footer a, .content_footer p {
            color: #F5F7FA;
            text-decoration: none;
        }
        .content_footer b {
            color: white;
        }
        .content_footer p {
            margin: 0;
            font-size: .75rem;
        }
        .content_footer > div {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .content_footer > div > div {
            margin: 0.25rem 0;
        }
        .content_footer > div > div > * {
            margin-right: .5rem;
        }
        .content_footer .image {
            align-self: center;
            width: 4rem;
            height: 4rem;
            margin: 0.25rem 0;
            background-size: cover;
            background-position: center;
        }

        @keyframes bubble-size {
            0%, 75% {
                width: var(--size, 4rem);
                height: var(--size, 4rem);
            }
            100% {
                width: 0rem;
                height: 0rem;
            }
        }

        @keyframes bubble-move {
            0% {
                bottom: -4rem;
            }
            100% {
                bottom: var(--distance, 10rem);
            }
        }
    </style>
</head>
<body class="body_footer">
    <div class="main">
        <!-- 主体内容 -->
    </div>
    <div class="footer">
        <div class="bubbles"></div>
        <div class="content_footer">
            <div>
                <div>
                    <b>About us</b>
                    <a href="#">We make data workflows fast, flexible, and accessible to everyone.</a>
                </div>
                <div>
                    <b>Quick Links</b>
                    <a href="#">Services</a>
                    <a href="#">Products</a>
                    <a href="#">Blogs</a>
                </div>
                <div>
                    <b>Contact</b>
                    <a href="#">Gmail</a>
                    <a href="#">Wechat</a>
                    <a href="#">CSDN</a>
                    <a href="https://www.zhihu.com/people/luo-bu-37-66-92">知乎</a>
                </div>
                <div>
                    <b>Designers</b>
                    <a href="#">Robert（Bowei Luo）</a>
                    <a href="#">Kewin（Dibin Ke）</a>
                </div>
            </div>
            <div>
                <a class="image" href="#" target="_blank" style="background-image: url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/199011/happy.svg');"></a>
                <p>©2024 Data Nexus</p>
            </div>
        </div>
        <svg style="position: fixed; bottom: 0;">
            <defs>
                <filter id="blob">
                    <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur" />
                    <feColorMatrix
                        in="blur"
                        mode="matrix"
                        values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 19 -9"
                        result="blob"
                    />
                </filter>
            </defs>
        </svg>
    </div>
    <script>
        // 动态生成泡泡
        document.addEventListener('DOMContentLoaded', () => {
            const bubblesContainer = document.querySelector('.bubbles');
            for (let i = 0; i < 128; i++) {
                const bubble = document.createElement('div');
                bubble.className = 'bubble';
                bubble.style.setProperty('--size', `${2 + Math.random() * 4}rem`);
                bubble.style.setProperty('--distance', `${6 + Math.random() * 4}rem`);
                bubble.style.setProperty('--position', `${-5 + Math.random() * 110}%`);
                bubble.style.setProperty('--time', `${2 + Math.random() * 2}s`);
                bubble.style.setProperty('--delay', `${-1 * (2 + Math.random() * 2)}s`);
                bubblesContainer.appendChild(bubble);
            }
        });
    </script>
</body>
</html>

"""

html_content = html_content + html_footer


st.set_page_config(page_title="Data-Nexus Homepage", layout="wide")
components.html(html_content, height=2000)