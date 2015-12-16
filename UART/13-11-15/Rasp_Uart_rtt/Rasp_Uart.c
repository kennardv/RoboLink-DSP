/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: Rasp_Uart.c
 *
 * Code generated for Simulink model 'Rasp_Uart'.
 *
 * Model version                  : 1.3
 * Simulink Coder version         : 8.8 (R2015a) 09-Feb-2015
 * TLC version                    : 8.8 (Jan 19 2015)
 * C/C++ source code generated on : Wed Nov 18 15:12:29 2015
 *
 * Target selection: realtime.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "Rasp_Uart.h"
#include "Rasp_Uart_private.h"
#include "Rasp_Uart_dt.h"

/* Block signals (auto storage) */
B_Rasp_Uart_T Rasp_Uart_B;

/* Real-time model */
RT_MODEL_Rasp_Uart_T Rasp_Uart_M_;
RT_MODEL_Rasp_Uart_T *const Rasp_Uart_M = &Rasp_Uart_M_;

/* Model output function */
void Rasp_Uart_output(void)
{
  /* S-Function (Uart_Rasp_13_11_15): '<Root>/S-Function Builder' */
  Uart_Rasp_13_11_15_Outputs_wrapper(&Rasp_Uart_P.Constant_Value,
    &Rasp_Uart_B.SFunctionBuilder );
}

/* Model update function */
void Rasp_Uart_update(void)
{
  /* signal main to stop simulation */
  {                                    /* Sample time: [0.2s, 0.0s] */
    if ((rtmGetTFinal(Rasp_Uart_M)!=-1) &&
        !((rtmGetTFinal(Rasp_Uart_M)-Rasp_Uart_M->Timing.taskTime0) >
          Rasp_Uart_M->Timing.taskTime0 * (DBL_EPSILON))) {
      rtmSetErrorStatus(Rasp_Uart_M, "Simulation finished");
    }

    if (rtmGetStopRequested(Rasp_Uart_M)) {
      rtmSetErrorStatus(Rasp_Uart_M, "Simulation finished");
    }
  }

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   */
  Rasp_Uart_M->Timing.taskTime0 =
    (++Rasp_Uart_M->Timing.clockTick0) * Rasp_Uart_M->Timing.stepSize0;
}

/* Model initialize function */
void Rasp_Uart_initialize(void)
{
  /* Registration code */

  /* initialize real-time model */
  (void) memset((void *)Rasp_Uart_M, 0,
                sizeof(RT_MODEL_Rasp_Uart_T));
  rtmSetTFinal(Rasp_Uart_M, -1);
  Rasp_Uart_M->Timing.stepSize0 = 0.2;

  /* External mode info */
  Rasp_Uart_M->Sizes.checksums[0] = (3274007383U);
  Rasp_Uart_M->Sizes.checksums[1] = (3385641398U);
  Rasp_Uart_M->Sizes.checksums[2] = (1867125087U);
  Rasp_Uart_M->Sizes.checksums[3] = (4257514776U);

  {
    static const sysRanDType rtAlwaysEnabled = SUBSYS_RAN_BC_ENABLE;
    static RTWExtModeInfo rt_ExtModeInfo;
    static const sysRanDType *systemRan[1];
    Rasp_Uart_M->extModeInfo = (&rt_ExtModeInfo);
    rteiSetSubSystemActiveVectorAddresses(&rt_ExtModeInfo, systemRan);
    systemRan[0] = &rtAlwaysEnabled;
    rteiSetModelMappingInfoPtr(Rasp_Uart_M->extModeInfo,
      &Rasp_Uart_M->SpecialInfo.mappingInfo);
    rteiSetChecksumsPtr(Rasp_Uart_M->extModeInfo, Rasp_Uart_M->Sizes.checksums);
    rteiSetTPtr(Rasp_Uart_M->extModeInfo, rtmGetTPtr(Rasp_Uart_M));
  }

  /* block I/O */
  (void) memset(((void *) &Rasp_Uart_B), 0,
                sizeof(B_Rasp_Uart_T));

  /* data type transition information */
  {
    static DataTypeTransInfo dtInfo;
    (void) memset((char_T *) &dtInfo, 0,
                  sizeof(dtInfo));
    Rasp_Uart_M->SpecialInfo.mappingInfo = (&dtInfo);
    dtInfo.numDataTypes = 14;
    dtInfo.dataTypeSizes = &rtDataTypeSizes[0];
    dtInfo.dataTypeNames = &rtDataTypeNames[0];

    /* Block I/O transition table */
    dtInfo.B = &rtBTransTable;

    /* Parameters transition table */
    dtInfo.P = &rtPTransTable;
  }
}

/* Model terminate function */
void Rasp_Uart_terminate(void)
{
  /* (no terminate code required) */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
