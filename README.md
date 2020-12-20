# Calculator

## 2
### 3
#### 4

```python
def console_run():
    args = create_parser()
    line = args.string
    calc = Calculator(line, stack=Stack())
    print(calc.calculate())
```


