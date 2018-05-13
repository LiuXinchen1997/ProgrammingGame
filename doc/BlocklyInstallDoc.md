# Blockly 模块使用

### 安装

#### 环境配置

首先安装所需的编译环境

使用 npm 安装

```
npm install --global --production windows-build-tools
```
#### Blockly 安装
使用npm安装node-blockly
```
npm install node-blockly
```

安装后在App.vue中写的代码是：
```
<template> 
 <div class="BlocklyTest"> 
   <div id="blocklyDiv" style="height: 480px; width: 600px;">
   </div> 
    <xml id="toolbox" ref=toolbox style="display: none"> 
     <block type="controls_if"></block> 
     <block type="text"></block> <block type="text_print"></block> 
    </xml> 
   </div> 
</template> 
<script> 
 import Blockly from 'node-blockly/browser'
 import En from 'node-blockly/lib/i18n/en'
 Blockly.setLocale(En)
 
 export default { 
   name: 'BlocklyTest',
   data(){
     return {
       workspace: null
     }
   },
   mounted(){
     this.workspace = Blockly.inject('blocklyDiv', {toolbox: document.getElementById('toolbox')});
 } 
</script>
```
可以看到正常显示并且能够拖动了。
