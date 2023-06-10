STM32

find / -name "*gdbserver*" 2>/dev/null
find / -name "*STM32_Programmer_CLI*" 2>/dev/null

/opt/st/stm32cubeide_1.11.2/plugins/com.st.stm32cube.ide.mcu.externaltools.stlink-gdb-server.linux64_2.0.400.202209281104/tools/bin/ST-LINK_gdbserver

/opt/st/stm32cubeide_1.11.2/plugins/com.st.stm32cube.ide.mcu.externaltools.cubeprogrammer.linux64_2.0.500.202209151145/tools/bin/STM32_Programmer_CLI

/opt/st/stm32cubeide_1.11.2/plugins/com.st.stm32cube.ide.mcu.externaltools.cubeprogrammer.linux64_2.0.500.202209151145/tools/bin/STM32_Programmer_CLI -c port=swd -w /home/federicobruzzoneplasma/STM32CubeIDE/workspace_1.11.2/bare_metal_led/Debug/bare_metal_led.elf -rst

Compiler: /opt/st/stm32cubeide_1.11.2/plugins/com.st.stm32cube.ide.mcu.externaltools.gnu-tools-for-stm32.10.3-2021.10.linux64_1.0.100.202210260954/tools/bin/arm-none-eabi-gcc


Using makefile

- make -j8 all -C ./Debug/

- make -j8 clean -C ./Debug/

Generate databse

- bear -- make -j8 all -C ./Debug/

To compile

gcc-arm-none-eabi -static -mcpu=(cortex_m0plus)|(m0) -I <path to HAL.h> -L <path to HAL>
