/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2023 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
//void SystemClock_Config(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
#define GPIO_REGISTER 0x50000000

// In setNthBit indexing starts from 0.
void setNthBit(uint32_t* current, int index, int zeroOrOne) {
	if (zeroOrOne == 1) { *current |= 1 << index; }
	if (zeroOrOne == 0) { *current &= ~(1 << index); }
}

int getNthBits(int number, int from, int to) {
    return (((1 << to) - 1) & (number >> (from)));
}

uint32_t* addOffset(uint32_t current, uint32_t offset) {
	return (uint32_t*)(current + offset);
}


void loop() {
	for (int i = 0; i < 100000; i++);
}

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  //HAL_Init();

  /* USER CODE BEGIN Init */
	uint32_t* RCC_IOPENR = addOffset(0x40021000, 0x2c);
	setNthBit(RCC_IOPENR, 0, 0);

	uint32_t* portMode = GPIO_REGISTER;
	uint32_t* portInputData = addOffset(GPIO_REGISTER, 0x10);
	uint32_t* portOutputData = addOffset(GPIO_REGISTER, 0x14);
	uint32_t* portPullUpPullDown = addOffset(GPIO_REGISTER, 0x0C);


	// Set PA5 pin in `01: General purpose output mode`
	setNthBit(portMode, 10, 1);
	setNthBit(portMode, 11, 0);

	// Set PA0 pin in `00: Input mode`
	setNthBit(portMode, 0, 0);
	setNthBit(portMode, 1, 0);

	// Set PA0 pin in Floating
//	setNthBit(portPullUpPullDown, 0, 0);
//	setNthBit(portPullUpPullDown, 1, 0);
	// Set PA0 pin in Pull Up
	setNthBit(portPullUpPullDown, 0, 1);
	setNthBit(portPullUpPullDown, 1, 0);
	// Set PA0 pin in Pull Down
//	setNthBit(portPullUpPullDown, 0, 0);
//	setNthBit(portPullUpPullDown, 1, 1);


  /* USER CODE END Init */

  /* Configure the system clock */
  //SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  /* USER CODE BEGIN 2 */

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {

	  // Es. 1
//	  setNthBit(portOutputData, 5, 1);
//	  loop();
//	  setNthBit(portOutputData, 5, 0);
//	  loop();

	  // Es. 2
	  uint32_t valueInputData = *portInputData;
	  int PA0Data = getNthBits(valueInputData, 0, 1);

	  if (PA0Data == 1) {
		  setNthBit(portOutputData, 5, 1);
	  } else {
		  setNthBit(portOutputData, 5, 0);
	  }


    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
//void SystemClock_Config(void)
//{
//  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
//  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};
//
//  /** Configure the main internal regulator output voltage
//  */
//  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);
//
//  /** Initializes the RCC Oscillators according to the specified parameters
//  * in the RCC_OscInitTypeDef structure.
//  */
//  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_MSI;
//  RCC_OscInitStruct.MSIState = RCC_MSI_ON;
//  RCC_OscInitStruct.MSICalibrationValue = 0;
//  RCC_OscInitStruct.MSIClockRange = RCC_MSIRANGE_5;
//  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_NONE;
//  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
//  {
//    Error_Handler();
//  }
//
//  /** Initializes the CPU, AHB and APB buses clocks
//  */
//  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
//                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
//  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_MSI;
//  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
//  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
//  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;
//
//  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_0) != HAL_OK)
//  {
//    Error_Handler();
//  }
//}
//
///* USER CODE BEGIN 4 */
//
///* USER CODE END 4 */
//
///**
//  * @brief  This function is executed in case of error occurrence.
//  * @retval None
//  */
//void Error_Handler(void)
//{
//  /* USER CODE BEGIN Error_Handler_Debug */
//  /* User can add his own implementation to report the HAL error return state */
//  __disable_irq();
//  while (1)
//  {
//  }
//  /* USER CODE END Error_Handler_Debug */
//}
//
//#ifdef  USE_FULL_ASSERT
///**
//  * @brief  Reports the name of the source file and the source line number
//  *         where the assert_param error has occurred.
//  * @param  file: pointer to the source file name
//  * @param  line: assert_param error line source number
//  * @retval None
//  */
//void assert_failed(uint8_t *file, uint32_t line)
//{
//  /* USER CODE BEGIN 6 */
//  /* User can add his own implementation to report the file name and line number,
//     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
//  /* USER CODE END 6 */
//}
//#endif /* USE_FULL_ASSERT */
