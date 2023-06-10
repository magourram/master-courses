# Run from command line 

```
make -j8 all -C ./Debug/
```


To generate compile_commands.json

```
bear -- make -j8 all -C ./Debug/
```

and 

```
/opt/st/stm32cubeide_1.11.2/plugins/com.st.stm32cube.ide.mcu.externaltools.cubeprogrammer.linux64_2.0.500.202209151145/tools/bin/STM32_Programmer_CLI -c port=swd -w hello_led.elf -rst
```
```
STM32_Programmer_CLI Debug/hello_led.elf -rst
```
