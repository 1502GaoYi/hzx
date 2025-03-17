from graphviz import Digraph

# 创建一个有向图
dot = Digraph(comment='深度学习过程')

# 设置字体为支持中文的字体
dot.attr(fontname='SimSun')  # SimSun 是 Windows 系统常见的中文字体

# 添加节点
dot.node('A', '数据准备', fontname='SimSun')
dot.node('B', '模型选择', fontname='SimSun')
dot.node('C', '模型构建', fontname='SimSun')
dot.node('D', '模型训练', fontname='SimSun')
dot.node('E', '模型验证', fontname='SimSun')
dot.node('F', '模型测试', fontname='SimSun')
dot.node('G', '模型部署', fontname='SimSun')
dot.node('H', '模型优化', fontname='SimSun')

# 添加边
dot.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'GH'])

# 渲染并保存为文件
dot.render('deep_learning_process', format='png', cleanup=True)

# 显示流程图
dot.view()