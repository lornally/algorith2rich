
### 官网
* https://docs.github.com/en/copilot/getting-started-with-github-copilot?tool=vscode


### 样例
```js
 function calculateDaysBetweenDates(begin, end)
```

### 问题
- 菊花一直在右下角转, 猪头出不来
  - 左边github的tab登录
* 修改vscode 的key绑定
```json
 {
  "key": "tab",
  "command": "editor.action.inlineSuggest.commit",
  "when": "textInputFocus && inlineSuggestionHasIndentationLessThanTabSize && inlineSuggestionVisible && !editorTabMovesFocus"
 },
```

### 按键
* alt + []
* ctrl + enter