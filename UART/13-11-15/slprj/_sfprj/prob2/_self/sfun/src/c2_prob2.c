/* Include files */

#include <stddef.h>
#include "blas.h"
#include "prob2_sfun.h"
#include "c2_prob2.h"
#define CHARTINSTANCE_CHARTNUMBER      (chartInstance->chartNumber)
#define CHARTINSTANCE_INSTANCENUMBER   (chartInstance->instanceNumber)
#include "prob2_sfun_debug_macros.h"
#define _SF_MEX_LISTEN_FOR_CTRL_C(S)   sf_mex_listen_for_ctrl_c_with_debugger(S, sfGlobalDebugInstanceStruct);

static void chart_debug_initialization(SimStruct *S, unsigned int
  fullDebuggerInitialization);
static void chart_debug_initialize_data_addresses(SimStruct *S);

/* Type Definitions */

/* Named Constants */
#define CALL_EVENT                     (-1)

/* Variable Declarations */

/* Variable Definitions */
static real_T _sfTime_;
static const char * c2_debug_family_names[6] = { "gpioPin", "cmd", "nargin",
  "nargout", "u", "firstTime" };

static const char * c2_b_debug_family_names[3] = { "str", "nargin", "nargout" };

static const char * c2_c_debug_family_names[3] = { "str", "nargin", "nargout" };

/* Function Declarations */
static void initialize_c2_prob2(SFc2_prob2InstanceStruct *chartInstance);
static void initialize_params_c2_prob2(SFc2_prob2InstanceStruct *chartInstance);
static void enable_c2_prob2(SFc2_prob2InstanceStruct *chartInstance);
static void disable_c2_prob2(SFc2_prob2InstanceStruct *chartInstance);
static void c2_update_debugger_state_c2_prob2(SFc2_prob2InstanceStruct
  *chartInstance);
static const mxArray *get_sim_state_c2_prob2(SFc2_prob2InstanceStruct
  *chartInstance);
static void set_sim_state_c2_prob2(SFc2_prob2InstanceStruct *chartInstance,
  const mxArray *c2_st);
static void finalize_c2_prob2(SFc2_prob2InstanceStruct *chartInstance);
static void sf_gateway_c2_prob2(SFc2_prob2InstanceStruct *chartInstance);
static void mdl_start_c2_prob2(SFc2_prob2InstanceStruct *chartInstance);
static void initSimStructsc2_prob2(SFc2_prob2InstanceStruct *chartInstance);
static void init_script_number_translation(uint32_T c2_machineNumber, uint32_T
  c2_chartNumber, uint32_T c2_instanceNumber);
static const mxArray *c2_sf_marshallOut(void *chartInstanceVoid, void *c2_inData);
static real_T c2_emlrt_marshallIn(SFc2_prob2InstanceStruct *chartInstance, const
  mxArray *c2_b_firstTime, const char_T *c2_identifier, boolean_T *c2_svPtr);
static real_T c2_b_emlrt_marshallIn(SFc2_prob2InstanceStruct *chartInstance,
  const mxArray *c2_b_u, const emlrtMsgIdentifier *c2_parentId, boolean_T
  *c2_svPtr);
static void c2_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c2_mxArrayInData, const char_T *c2_varName, void *c2_outData);
static const mxArray *c2_b_sf_marshallOut(void *chartInstanceVoid, void
  *c2_inData);
static real_T c2_c_emlrt_marshallIn(SFc2_prob2InstanceStruct *chartInstance,
  const mxArray *c2_b_u, const emlrtMsgIdentifier *c2_parentId);
static void c2_b_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c2_mxArrayInData, const char_T *c2_varName, void *c2_outData);
static const mxArray *c2_c_sf_marshallOut(void *chartInstanceVoid, void
  *c2_inData);
static void c2_d_emlrt_marshallIn(SFc2_prob2InstanceStruct *chartInstance, const
  mxArray *c2_b_u, const emlrtMsgIdentifier *c2_parentId, char_T c2_y[38]);
static void c2_c_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c2_mxArrayInData, const char_T *c2_varName, void *c2_outData);
static const mxArray *c2_d_sf_marshallOut(void *chartInstanceVoid, void
  *c2_inData);
static const mxArray *c2_e_sf_marshallOut(void *chartInstanceVoid, void
  *c2_inData);
static void c2_isequal(SFc2_prob2InstanceStruct *chartInstance);
static const mxArray *c2_f_sf_marshallOut(void *chartInstanceVoid, void
  *c2_inData);
static int32_T c2_e_emlrt_marshallIn(SFc2_prob2InstanceStruct *chartInstance,
  const mxArray *c2_b_u, const emlrtMsgIdentifier *c2_parentId);
static void c2_d_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c2_mxArrayInData, const char_T *c2_varName, void *c2_outData);
static uint8_T c2_f_emlrt_marshallIn(SFc2_prob2InstanceStruct *chartInstance,
  const mxArray *c2_b_is_active_c2_prob2, const char_T *c2_identifier);
static uint8_T c2_g_emlrt_marshallIn(SFc2_prob2InstanceStruct *chartInstance,
  const mxArray *c2_b_u, const emlrtMsgIdentifier *c2_parentId);
static void init_dsm_address_info(SFc2_prob2InstanceStruct *chartInstance);
static void init_simulink_io_address(SFc2_prob2InstanceStruct *chartInstance);

/* Function Definitions */
static void initialize_c2_prob2(SFc2_prob2InstanceStruct *chartInstance)
{
  if (sf_is_first_init_cond(chartInstance->S)) {
    initSimStructsc2_prob2(chartInstance);
    chart_debug_initialize_data_addresses(chartInstance->S);
  }

  chartInstance->c2_sfEvent = CALL_EVENT;
  _sfTime_ = sf_get_time(chartInstance->S);
  chartInstance->c2_firstTime_not_empty = false;
  chartInstance->c2_is_active_c2_prob2 = 0U;
}

static void initialize_params_c2_prob2(SFc2_prob2InstanceStruct *chartInstance)
{
  (void)chartInstance;
}

static void enable_c2_prob2(SFc2_prob2InstanceStruct *chartInstance)
{
  _sfTime_ = sf_get_time(chartInstance->S);
}

static void disable_c2_prob2(SFc2_prob2InstanceStruct *chartInstance)
{
  _sfTime_ = sf_get_time(chartInstance->S);
}

static void c2_update_debugger_state_c2_prob2(SFc2_prob2InstanceStruct
  *chartInstance)
{
  (void)chartInstance;
}

static const mxArray *get_sim_state_c2_prob2(SFc2_prob2InstanceStruct
  *chartInstance)
{
  const mxArray *c2_st;
  const mxArray *c2_y = NULL;
  real_T c2_hoistedGlobal;
  real_T c2_b_u;
  const mxArray *c2_b_y = NULL;
  uint8_T c2_b_hoistedGlobal;
  uint8_T c2_c_u;
  const mxArray *c2_c_y = NULL;
  c2_st = NULL;
  c2_st = NULL;
  c2_y = NULL;
  sf_mex_assign(&c2_y, sf_mex_createcellmatrix(2, 1), false);
  c2_hoistedGlobal = chartInstance->c2_firstTime;
  c2_b_u = c2_hoistedGlobal;
  c2_b_y = NULL;
  if (!chartInstance->c2_firstTime_not_empty) {
    sf_mex_assign(&c2_b_y, sf_mex_create("y", NULL, 0, 0U, 1U, 0U, 2, 0, 0),
                  false);
  } else {
    sf_mex_assign(&c2_b_y, sf_mex_create("y", &c2_b_u, 0, 0U, 0U, 0U, 0), false);
  }

  sf_mex_setcell(c2_y, 0, c2_b_y);
  c2_b_hoistedGlobal = chartInstance->c2_is_active_c2_prob2;
  c2_c_u = c2_b_hoistedGlobal;
  c2_c_y = NULL;
  sf_mex_assign(&c2_c_y, sf_mex_create("y", &c2_c_u, 3, 0U, 0U, 0U, 0), false);
  sf_mex_setcell(c2_y, 1, c2_c_y);
  sf_mex_assign(&c2_st, c2_y, false);
  return c2_st;
}

static void set_sim_state_c2_prob2(SFc2_prob2InstanceStruct *chartInstance,
  const mxArray *c2_st)
{
  const mxArray *c2_b_u;
  chartInstance->c2_doneDoubleBufferReInit = true;
  c2_b_u = sf_mex_dup(c2_st);
  chartInstance->c2_firstTime = c2_emlrt_marshallIn(chartInstance, sf_mex_dup
    (sf_mex_getcell("firstTime", c2_b_u, 0)), "firstTime",
    &chartInstance->c2_firstTime_not_empty);
  chartInstance->c2_is_active_c2_prob2 = c2_f_emlrt_marshallIn(chartInstance,
    sf_mex_dup(sf_mex_getcell("is_active_c2_prob2", c2_b_u, 1)),
    "is_active_c2_prob2");
  sf_mex_destroy(&c2_b_u);
  c2_update_debugger_state_c2_prob2(chartInstance);
  sf_mex_destroy(&c2_st);
}

static void finalize_c2_prob2(SFc2_prob2InstanceStruct *chartInstance)
{
  (void)chartInstance;
}

static void sf_gateway_c2_prob2(SFc2_prob2InstanceStruct *chartInstance)
{
  real_T c2_hoistedGlobal;
  real_T c2_b_u;
  uint32_T c2_debug_family_var_map[6];
  char_T c2_gpioPin[2];
  char_T c2_cmd[38];
  real_T c2_nargin = 1.0;
  real_T c2_nargout = 0.0;
  int32_T c2_i0;
  static char_T c2_cv0[2] = { '1', '5' };

  const mxArray *c2_y = NULL;
  static char_T c2_c_u[29] = { 'I', 'n', 'i', 't', 'i', 'a', 'l', 'i', 'z', 'e',
    ' ', 'G', 'P', 'I', 'O', ' ', 'p', 'i', 'n', ' ', 'a', 's', ' ', 'o', 'u',
    't', 'p', 'u', 't' };

  uint32_T c2_b_debug_family_var_map[3];
  char_T c2_str[38];
  char_T c2_b_str[37];
  char_T c2_c_str[37];
  real_T c2_b_nargin = 1.0;
  real_T c2_b_nargout = 1.0;
  int32_T c2_i1;
  static char_T c2_cv1[37] = { 'e', 'c', 'h', 'o', ' ', '1', ' ', '>', ' ', '/',
    's', 'y', 's', '/', 'c', 'l', 'a', 's', 's', '/', 'g', 'p', 'i', 'o', '/',
    'g', 'p', 'i', 'o', '1', '5', '/', 'v', 'a', 'l', 'u', 'e' };

  int32_T c2_i2;
  int32_T c2_i3;
  static char_T c2_cv2[38] = { 'e', 'c', 'h', 'o', ' ', '1', ' ', '>', ' ', '/',
    's', 'y', 's', '/', 'c', 'l', 'a', 's', 's', '/', 'g', 'p', 'i', 'o', '/',
    'g', 'p', 'i', 'o', '1', '5', '/', 'v', 'a', 'l', 'u', 'e', '\x00' };

  int32_T c2_i4;
  char_T c2_d_str[38];
  char_T c2_e_str[37];
  char_T c2_f_str[37];
  real_T c2_c_nargin = 1.0;
  real_T c2_c_nargout = 1.0;
  int32_T c2_i5;
  static char_T c2_cv3[37] = { 'e', 'c', 'h', 'o', ' ', '0', ' ', '>', ' ', '/',
    's', 'y', 's', '/', 'c', 'l', 'a', 's', 's', '/', 'g', 'p', 'i', 'o', '/',
    'g', 'p', 'i', 'o', '1', '5', '/', 'v', 'a', 'l', 'u', 'e' };

  int32_T c2_i6;
  int32_T c2_i7;
  static char_T c2_cv4[38] = { 'e', 'c', 'h', 'o', ' ', '0', ' ', '>', ' ', '/',
    's', 'y', 's', '/', 'c', 'l', 'a', 's', 's', '/', 'g', 'p', 'i', 'o', '/',
    'g', 'p', 'i', 'o', '1', '5', '/', 'v', 'a', 'l', 'u', 'e', '\x00' };

  int32_T c2_i8;
  int32_T c2_i9;
  char_T c2_d_u[38];
  const mxArray *c2_b_y = NULL;
  _SFD_SYMBOL_SCOPE_PUSH(0U, 0U);
  _sfTime_ = sf_get_time(chartInstance->S);
  _SFD_CC_CALL(CHART_ENTER_SFUNCTION_TAG, 1U, chartInstance->c2_sfEvent);
  _SFD_DATA_RANGE_CHECK(*chartInstance->c2_u, 0U, 1U, 0U,
                        chartInstance->c2_sfEvent, false);
  chartInstance->c2_sfEvent = CALL_EVENT;
  _SFD_CC_CALL(CHART_ENTER_DURING_FUNCTION_TAG, 1U, chartInstance->c2_sfEvent);
  c2_hoistedGlobal = *chartInstance->c2_u;
  c2_b_u = c2_hoistedGlobal;
  _SFD_SYMBOL_SCOPE_PUSH_EML(0U, 6U, 6U, c2_debug_family_names,
    c2_debug_family_var_map);
  _SFD_SYMBOL_SCOPE_ADD_EML(c2_gpioPin, 0U, c2_d_sf_marshallOut);
  _SFD_SYMBOL_SCOPE_ADD_EML_IMPORTABLE(c2_cmd, 1U, c2_c_sf_marshallOut,
    c2_c_sf_marshallIn);
  _SFD_SYMBOL_SCOPE_ADD_EML_IMPORTABLE(&c2_nargin, 2U, c2_b_sf_marshallOut,
    c2_b_sf_marshallIn);
  _SFD_SYMBOL_SCOPE_ADD_EML_IMPORTABLE(&c2_nargout, 3U, c2_b_sf_marshallOut,
    c2_b_sf_marshallIn);
  _SFD_SYMBOL_SCOPE_ADD_EML(&c2_b_u, 4U, c2_b_sf_marshallOut);
  _SFD_SYMBOL_SCOPE_ADD_EML_IMPORTABLE(&chartInstance->c2_firstTime, 5U,
    c2_sf_marshallOut, c2_sf_marshallIn);
  CV_EML_FCN(0, 0);
  _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, 2);
  _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, 13);
  _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, 14);
  for (c2_i0 = 0; c2_i0 < 2; c2_i0++) {
    c2_gpioPin[c2_i0] = c2_cv0[c2_i0];
  }

  _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, 15);
  _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, 16);
  if (CV_EML_IF(0, 1, 0, !chartInstance->c2_firstTime_not_empty)) {
    _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, 17);
    chartInstance->c2_firstTime = 0.0;
    chartInstance->c2_firstTime_not_empty = true;
    _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, 18);
    c2_isequal(chartInstance);
    CV_EML_IF(0, 1, 1, false);
    _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, 26);
    c2_y = NULL;
    sf_mex_assign(&c2_y, sf_mex_create("y", c2_c_u, 10, 0U, 1U, 0U, 2, 1, 29),
                  false);
    sf_mex_call_debug(sfGlobalDebugInstanceStruct, "disp", 0U, 1U, 14, c2_y);
  }

  _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, 31);
  if (CV_EML_IF(0, 1, 2, CV_RELATIONAL_EVAL(4U, 0U, 0, c2_b_u, 0.0, -1, 4U,
        c2_b_u > 0.0))) {
    _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, 32);
    _SFD_SYMBOL_SCOPE_PUSH_EML(0U, 3U, 5U, c2_b_debug_family_names,
      c2_b_debug_family_var_map);
    _SFD_SYMBOL_SCOPE_ADD_EML_IMPORTABLE(c2_str, MAX_uint32_T,
      c2_c_sf_marshallOut, c2_c_sf_marshallIn);
    _SFD_SYMBOL_SCOPE_ADD_EML(c2_b_str, MAX_uint32_T, c2_e_sf_marshallOut);
    _SFD_SYMBOL_SCOPE_ADD_EML(c2_c_str, MAX_uint32_T, c2_e_sf_marshallOut);
    _SFD_SYMBOL_SCOPE_ADD_EML_IMPORTABLE(&c2_b_nargin, 1U, c2_b_sf_marshallOut,
      c2_b_sf_marshallIn);
    _SFD_SYMBOL_SCOPE_ADD_EML_IMPORTABLE(&c2_b_nargout, 2U, c2_b_sf_marshallOut,
      c2_b_sf_marshallIn);
    for (c2_i1 = 0; c2_i1 < 37; c2_i1++) {
      c2_c_str[c2_i1] = c2_cv1[c2_i1];
    }

    _SFD_SYMBOL_SWITCH(0U, 2U);
    for (c2_i2 = 0; c2_i2 < 37; c2_i2++) {
      c2_b_str[c2_i2] = c2_cv1[c2_i2];
    }

    _SFD_SYMBOL_SWITCH(0U, 1U);
    CV_EML_FCN(0, 1);
    _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, 47);
    for (c2_i3 = 0; c2_i3 < 38; c2_i3++) {
      c2_str[c2_i3] = c2_cv2[c2_i3];
    }

    _SFD_SYMBOL_SWITCH(0U, 0U);
    _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, -47);
    _SFD_SYMBOL_SCOPE_POP();
    for (c2_i4 = 0; c2_i4 < 38; c2_i4++) {
      c2_cmd[c2_i4] = c2_cv2[c2_i4];
    }
  } else {
    _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, 34);
    _SFD_SYMBOL_SCOPE_PUSH_EML(0U, 3U, 5U, c2_c_debug_family_names,
      c2_b_debug_family_var_map);
    _SFD_SYMBOL_SCOPE_ADD_EML_IMPORTABLE(c2_d_str, MAX_uint32_T,
      c2_c_sf_marshallOut, c2_c_sf_marshallIn);
    _SFD_SYMBOL_SCOPE_ADD_EML(c2_e_str, MAX_uint32_T, c2_e_sf_marshallOut);
    _SFD_SYMBOL_SCOPE_ADD_EML(c2_f_str, MAX_uint32_T, c2_e_sf_marshallOut);
    _SFD_SYMBOL_SCOPE_ADD_EML_IMPORTABLE(&c2_c_nargin, 1U, c2_b_sf_marshallOut,
      c2_b_sf_marshallIn);
    _SFD_SYMBOL_SCOPE_ADD_EML_IMPORTABLE(&c2_c_nargout, 2U, c2_b_sf_marshallOut,
      c2_b_sf_marshallIn);
    for (c2_i5 = 0; c2_i5 < 37; c2_i5++) {
      c2_f_str[c2_i5] = c2_cv3[c2_i5];
    }

    _SFD_SYMBOL_SWITCH(0U, 2U);
    for (c2_i6 = 0; c2_i6 < 37; c2_i6++) {
      c2_e_str[c2_i6] = c2_cv3[c2_i6];
    }

    _SFD_SYMBOL_SWITCH(0U, 1U);
    CV_EML_FCN(0, 1);
    _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, 47);
    for (c2_i7 = 0; c2_i7 < 38; c2_i7++) {
      c2_d_str[c2_i7] = c2_cv4[c2_i7];
    }

    _SFD_SYMBOL_SWITCH(0U, 0U);
    _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, -47);
    _SFD_SYMBOL_SCOPE_POP();
    for (c2_i8 = 0; c2_i8 < 38; c2_i8++) {
      c2_cmd[c2_i8] = c2_cv4[c2_i8];
    }
  }

  _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, 36);
  c2_isequal(chartInstance);
  CV_EML_IF(0, 1, 3, false);
  _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, 39);
  for (c2_i9 = 0; c2_i9 < 38; c2_i9++) {
    c2_d_u[c2_i9] = c2_cmd[c2_i9];
  }

  c2_b_y = NULL;
  sf_mex_assign(&c2_b_y, sf_mex_create("y", c2_d_u, 10, 0U, 1U, 0U, 2, 1, 38),
                false);
  sf_mex_call_debug(sfGlobalDebugInstanceStruct, "disp", 0U, 1U, 14, c2_b_y);
  _SFD_EML_CALL(0U, chartInstance->c2_sfEvent, -39);
  _SFD_SYMBOL_SCOPE_POP();
  _SFD_CC_CALL(EXIT_OUT_OF_FUNCTION_TAG, 1U, chartInstance->c2_sfEvent);
  _SFD_SYMBOL_SCOPE_POP();
  _SFD_CHECK_FOR_STATE_INCONSISTENCY(_prob2MachineNumber_,
    chartInstance->chartNumber, chartInstance->instanceNumber);
}

static void mdl_start_c2_prob2(SFc2_prob2InstanceStruct *chartInstance)
{
  (void)chartInstance;
}

static void initSimStructsc2_prob2(SFc2_prob2InstanceStruct *chartInstance)
{
  (void)chartInstance;
}

static void init_script_number_translation(uint32_T c2_machineNumber, uint32_T
  c2_chartNumber, uint32_T c2_instanceNumber)
{
  (void)c2_machineNumber;
  (void)c2_chartNumber;
  (void)c2_instanceNumber;
}

static const mxArray *c2_sf_marshallOut(void *chartInstanceVoid, void *c2_inData)
{
  const mxArray *c2_mxArrayOutData;
  real_T c2_b_u;
  const mxArray *c2_y = NULL;
  SFc2_prob2InstanceStruct *chartInstance;
  chartInstance = (SFc2_prob2InstanceStruct *)chartInstanceVoid;
  c2_mxArrayOutData = NULL;
  c2_mxArrayOutData = NULL;
  c2_b_u = *(real_T *)c2_inData;
  c2_y = NULL;
  if (!chartInstance->c2_firstTime_not_empty) {
    sf_mex_assign(&c2_y, sf_mex_create("y", NULL, 0, 0U, 1U, 0U, 2, 0, 0), false);
  } else {
    sf_mex_assign(&c2_y, sf_mex_create("y", &c2_b_u, 0, 0U, 0U, 0U, 0), false);
  }

  sf_mex_assign(&c2_mxArrayOutData, c2_y, false);
  return c2_mxArrayOutData;
}

static real_T c2_emlrt_marshallIn(SFc2_prob2InstanceStruct *chartInstance, const
  mxArray *c2_b_firstTime, const char_T *c2_identifier, boolean_T *c2_svPtr)
{
  real_T c2_y;
  emlrtMsgIdentifier c2_thisId;
  c2_thisId.fIdentifier = c2_identifier;
  c2_thisId.fParent = NULL;
  c2_y = c2_b_emlrt_marshallIn(chartInstance, sf_mex_dup(c2_b_firstTime),
    &c2_thisId, c2_svPtr);
  sf_mex_destroy(&c2_b_firstTime);
  return c2_y;
}

static real_T c2_b_emlrt_marshallIn(SFc2_prob2InstanceStruct *chartInstance,
  const mxArray *c2_b_u, const emlrtMsgIdentifier *c2_parentId, boolean_T
  *c2_svPtr)
{
  real_T c2_y;
  real_T c2_d0;
  (void)chartInstance;
  if (mxIsEmpty(c2_b_u)) {
    *c2_svPtr = false;
  } else {
    *c2_svPtr = true;
    sf_mex_import(c2_parentId, sf_mex_dup(c2_b_u), &c2_d0, 1, 0, 0U, 0, 0U, 0);
    c2_y = c2_d0;
  }

  sf_mex_destroy(&c2_b_u);
  return c2_y;
}

static void c2_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c2_mxArrayInData, const char_T *c2_varName, void *c2_outData)
{
  const mxArray *c2_b_firstTime;
  const char_T *c2_identifier;
  boolean_T *c2_svPtr;
  emlrtMsgIdentifier c2_thisId;
  real_T c2_y;
  SFc2_prob2InstanceStruct *chartInstance;
  chartInstance = (SFc2_prob2InstanceStruct *)chartInstanceVoid;
  c2_b_firstTime = sf_mex_dup(c2_mxArrayInData);
  c2_identifier = c2_varName;
  c2_svPtr = &chartInstance->c2_firstTime_not_empty;
  c2_thisId.fIdentifier = c2_identifier;
  c2_thisId.fParent = NULL;
  c2_y = c2_b_emlrt_marshallIn(chartInstance, sf_mex_dup(c2_b_firstTime),
    &c2_thisId, c2_svPtr);
  sf_mex_destroy(&c2_b_firstTime);
  *(real_T *)c2_outData = c2_y;
  sf_mex_destroy(&c2_mxArrayInData);
}

static const mxArray *c2_b_sf_marshallOut(void *chartInstanceVoid, void
  *c2_inData)
{
  const mxArray *c2_mxArrayOutData = NULL;
  real_T c2_b_u;
  const mxArray *c2_y = NULL;
  SFc2_prob2InstanceStruct *chartInstance;
  chartInstance = (SFc2_prob2InstanceStruct *)chartInstanceVoid;
  c2_mxArrayOutData = NULL;
  c2_b_u = *(real_T *)c2_inData;
  c2_y = NULL;
  sf_mex_assign(&c2_y, sf_mex_create("y", &c2_b_u, 0, 0U, 0U, 0U, 0), false);
  sf_mex_assign(&c2_mxArrayOutData, c2_y, false);
  return c2_mxArrayOutData;
}

static real_T c2_c_emlrt_marshallIn(SFc2_prob2InstanceStruct *chartInstance,
  const mxArray *c2_b_u, const emlrtMsgIdentifier *c2_parentId)
{
  real_T c2_y;
  real_T c2_d1;
  (void)chartInstance;
  sf_mex_import(c2_parentId, sf_mex_dup(c2_b_u), &c2_d1, 1, 0, 0U, 0, 0U, 0);
  c2_y = c2_d1;
  sf_mex_destroy(&c2_b_u);
  return c2_y;
}

static void c2_b_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c2_mxArrayInData, const char_T *c2_varName, void *c2_outData)
{
  const mxArray *c2_nargout;
  const char_T *c2_identifier;
  emlrtMsgIdentifier c2_thisId;
  real_T c2_y;
  SFc2_prob2InstanceStruct *chartInstance;
  chartInstance = (SFc2_prob2InstanceStruct *)chartInstanceVoid;
  c2_nargout = sf_mex_dup(c2_mxArrayInData);
  c2_identifier = c2_varName;
  c2_thisId.fIdentifier = c2_identifier;
  c2_thisId.fParent = NULL;
  c2_y = c2_c_emlrt_marshallIn(chartInstance, sf_mex_dup(c2_nargout), &c2_thisId);
  sf_mex_destroy(&c2_nargout);
  *(real_T *)c2_outData = c2_y;
  sf_mex_destroy(&c2_mxArrayInData);
}

static const mxArray *c2_c_sf_marshallOut(void *chartInstanceVoid, void
  *c2_inData)
{
  const mxArray *c2_mxArrayOutData = NULL;
  int32_T c2_i10;
  char_T c2_b_u[38];
  const mxArray *c2_y = NULL;
  SFc2_prob2InstanceStruct *chartInstance;
  chartInstance = (SFc2_prob2InstanceStruct *)chartInstanceVoid;
  c2_mxArrayOutData = NULL;
  for (c2_i10 = 0; c2_i10 < 38; c2_i10++) {
    c2_b_u[c2_i10] = (*(char_T (*)[38])c2_inData)[c2_i10];
  }

  c2_y = NULL;
  sf_mex_assign(&c2_y, sf_mex_create("y", c2_b_u, 10, 0U, 1U, 0U, 2, 1, 38),
                false);
  sf_mex_assign(&c2_mxArrayOutData, c2_y, false);
  return c2_mxArrayOutData;
}

static void c2_d_emlrt_marshallIn(SFc2_prob2InstanceStruct *chartInstance, const
  mxArray *c2_b_u, const emlrtMsgIdentifier *c2_parentId, char_T c2_y[38])
{
  char_T c2_cv5[38];
  int32_T c2_i11;
  (void)chartInstance;
  sf_mex_import(c2_parentId, sf_mex_dup(c2_b_u), c2_cv5, 1, 10, 0U, 1, 0U, 2, 1,
                38);
  for (c2_i11 = 0; c2_i11 < 38; c2_i11++) {
    c2_y[c2_i11] = c2_cv5[c2_i11];
  }

  sf_mex_destroy(&c2_b_u);
}

static void c2_c_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c2_mxArrayInData, const char_T *c2_varName, void *c2_outData)
{
  const mxArray *c2_cmd;
  const char_T *c2_identifier;
  emlrtMsgIdentifier c2_thisId;
  char_T c2_y[38];
  int32_T c2_i12;
  SFc2_prob2InstanceStruct *chartInstance;
  chartInstance = (SFc2_prob2InstanceStruct *)chartInstanceVoid;
  c2_cmd = sf_mex_dup(c2_mxArrayInData);
  c2_identifier = c2_varName;
  c2_thisId.fIdentifier = c2_identifier;
  c2_thisId.fParent = NULL;
  c2_d_emlrt_marshallIn(chartInstance, sf_mex_dup(c2_cmd), &c2_thisId, c2_y);
  sf_mex_destroy(&c2_cmd);
  for (c2_i12 = 0; c2_i12 < 38; c2_i12++) {
    (*(char_T (*)[38])c2_outData)[c2_i12] = c2_y[c2_i12];
  }

  sf_mex_destroy(&c2_mxArrayInData);
}

static const mxArray *c2_d_sf_marshallOut(void *chartInstanceVoid, void
  *c2_inData)
{
  const mxArray *c2_mxArrayOutData = NULL;
  int32_T c2_i13;
  char_T c2_b_u[2];
  const mxArray *c2_y = NULL;
  SFc2_prob2InstanceStruct *chartInstance;
  chartInstance = (SFc2_prob2InstanceStruct *)chartInstanceVoid;
  c2_mxArrayOutData = NULL;
  for (c2_i13 = 0; c2_i13 < 2; c2_i13++) {
    c2_b_u[c2_i13] = (*(char_T (*)[2])c2_inData)[c2_i13];
  }

  c2_y = NULL;
  sf_mex_assign(&c2_y, sf_mex_create("y", c2_b_u, 10, 0U, 1U, 0U, 2, 1, 2),
                false);
  sf_mex_assign(&c2_mxArrayOutData, c2_y, false);
  return c2_mxArrayOutData;
}

static const mxArray *c2_e_sf_marshallOut(void *chartInstanceVoid, void
  *c2_inData)
{
  const mxArray *c2_mxArrayOutData = NULL;
  int32_T c2_i14;
  char_T c2_b_u[37];
  const mxArray *c2_y = NULL;
  SFc2_prob2InstanceStruct *chartInstance;
  chartInstance = (SFc2_prob2InstanceStruct *)chartInstanceVoid;
  c2_mxArrayOutData = NULL;
  for (c2_i14 = 0; c2_i14 < 37; c2_i14++) {
    c2_b_u[c2_i14] = (*(char_T (*)[37])c2_inData)[c2_i14];
  }

  c2_y = NULL;
  sf_mex_assign(&c2_y, sf_mex_create("y", c2_b_u, 10, 0U, 1U, 0U, 2, 1, 37),
                false);
  sf_mex_assign(&c2_mxArrayOutData, c2_y, false);
  return c2_mxArrayOutData;
}

const mxArray *sf_c2_prob2_get_eml_resolved_functions_info(void)
{
  const mxArray *c2_nameCaptureInfo = NULL;
  c2_nameCaptureInfo = NULL;
  sf_mex_assign(&c2_nameCaptureInfo, sf_mex_create("nameCaptureInfo", NULL, 0,
    0U, 1U, 0U, 2, 0, 1), false);
  return c2_nameCaptureInfo;
}

static void c2_isequal(SFc2_prob2InstanceStruct *chartInstance)
{
  (void)chartInstance;
}

static const mxArray *c2_f_sf_marshallOut(void *chartInstanceVoid, void
  *c2_inData)
{
  const mxArray *c2_mxArrayOutData = NULL;
  int32_T c2_b_u;
  const mxArray *c2_y = NULL;
  SFc2_prob2InstanceStruct *chartInstance;
  chartInstance = (SFc2_prob2InstanceStruct *)chartInstanceVoid;
  c2_mxArrayOutData = NULL;
  c2_b_u = *(int32_T *)c2_inData;
  c2_y = NULL;
  sf_mex_assign(&c2_y, sf_mex_create("y", &c2_b_u, 6, 0U, 0U, 0U, 0), false);
  sf_mex_assign(&c2_mxArrayOutData, c2_y, false);
  return c2_mxArrayOutData;
}

static int32_T c2_e_emlrt_marshallIn(SFc2_prob2InstanceStruct *chartInstance,
  const mxArray *c2_b_u, const emlrtMsgIdentifier *c2_parentId)
{
  int32_T c2_y;
  int32_T c2_i15;
  (void)chartInstance;
  sf_mex_import(c2_parentId, sf_mex_dup(c2_b_u), &c2_i15, 1, 6, 0U, 0, 0U, 0);
  c2_y = c2_i15;
  sf_mex_destroy(&c2_b_u);
  return c2_y;
}

static void c2_d_sf_marshallIn(void *chartInstanceVoid, const mxArray
  *c2_mxArrayInData, const char_T *c2_varName, void *c2_outData)
{
  const mxArray *c2_b_sfEvent;
  const char_T *c2_identifier;
  emlrtMsgIdentifier c2_thisId;
  int32_T c2_y;
  SFc2_prob2InstanceStruct *chartInstance;
  chartInstance = (SFc2_prob2InstanceStruct *)chartInstanceVoid;
  c2_b_sfEvent = sf_mex_dup(c2_mxArrayInData);
  c2_identifier = c2_varName;
  c2_thisId.fIdentifier = c2_identifier;
  c2_thisId.fParent = NULL;
  c2_y = c2_e_emlrt_marshallIn(chartInstance, sf_mex_dup(c2_b_sfEvent),
    &c2_thisId);
  sf_mex_destroy(&c2_b_sfEvent);
  *(int32_T *)c2_outData = c2_y;
  sf_mex_destroy(&c2_mxArrayInData);
}

static uint8_T c2_f_emlrt_marshallIn(SFc2_prob2InstanceStruct *chartInstance,
  const mxArray *c2_b_is_active_c2_prob2, const char_T *c2_identifier)
{
  uint8_T c2_y;
  emlrtMsgIdentifier c2_thisId;
  c2_thisId.fIdentifier = c2_identifier;
  c2_thisId.fParent = NULL;
  c2_y = c2_g_emlrt_marshallIn(chartInstance, sf_mex_dup(c2_b_is_active_c2_prob2),
    &c2_thisId);
  sf_mex_destroy(&c2_b_is_active_c2_prob2);
  return c2_y;
}

static uint8_T c2_g_emlrt_marshallIn(SFc2_prob2InstanceStruct *chartInstance,
  const mxArray *c2_b_u, const emlrtMsgIdentifier *c2_parentId)
{
  uint8_T c2_y;
  uint8_T c2_u0;
  (void)chartInstance;
  sf_mex_import(c2_parentId, sf_mex_dup(c2_b_u), &c2_u0, 1, 3, 0U, 0, 0U, 0);
  c2_y = c2_u0;
  sf_mex_destroy(&c2_b_u);
  return c2_y;
}

static void init_dsm_address_info(SFc2_prob2InstanceStruct *chartInstance)
{
  (void)chartInstance;
}

static void init_simulink_io_address(SFc2_prob2InstanceStruct *chartInstance)
{
  chartInstance->c2_u = (real_T *)ssGetInputPortSignal_wrapper(chartInstance->S,
    0);
}

/* SFunction Glue Code */
#ifdef utFree
#undef utFree
#endif

#ifdef utMalloc
#undef utMalloc
#endif

#ifdef __cplusplus

extern "C" void *utMalloc(size_t size);
extern "C" void utFree(void*);

#else

extern void *utMalloc(size_t size);
extern void utFree(void*);

#endif

void sf_c2_prob2_get_check_sum(mxArray *plhs[])
{
  ((real_T *)mxGetPr((plhs[0])))[0] = (real_T)(4247062917U);
  ((real_T *)mxGetPr((plhs[0])))[1] = (real_T)(3205674318U);
  ((real_T *)mxGetPr((plhs[0])))[2] = (real_T)(1225921500U);
  ((real_T *)mxGetPr((plhs[0])))[3] = (real_T)(3963774338U);
}

mxArray* sf_c2_prob2_get_post_codegen_info(void);
mxArray *sf_c2_prob2_get_autoinheritance_info(void)
{
  const char *autoinheritanceFields[] = { "checksum", "inputs", "parameters",
    "outputs", "locals", "postCodegenInfo" };

  mxArray *mxAutoinheritanceInfo = mxCreateStructMatrix(1, 1, sizeof
    (autoinheritanceFields)/sizeof(autoinheritanceFields[0]),
    autoinheritanceFields);

  {
    mxArray *mxChecksum = mxCreateString("lpdECFXoKXwjUFc9UApiZD");
    mxSetField(mxAutoinheritanceInfo,0,"checksum",mxChecksum);
  }

  {
    const char *dataFields[] = { "size", "type", "complexity" };

    mxArray *mxData = mxCreateStructMatrix(1,1,3,dataFields);

    {
      mxArray *mxSize = mxCreateDoubleMatrix(1,2,mxREAL);
      double *pr = mxGetPr(mxSize);
      pr[0] = (double)(1);
      pr[1] = (double)(1);
      mxSetField(mxData,0,"size",mxSize);
    }

    {
      const char *typeFields[] = { "base", "fixpt", "isFixedPointType" };

      mxArray *mxType = mxCreateStructMatrix(1,1,sizeof(typeFields)/sizeof
        (typeFields[0]),typeFields);
      mxSetField(mxType,0,"base",mxCreateDoubleScalar(10));
      mxSetField(mxType,0,"fixpt",mxCreateDoubleMatrix(0,0,mxREAL));
      mxSetField(mxType,0,"isFixedPointType",mxCreateDoubleScalar(0));
      mxSetField(mxData,0,"type",mxType);
    }

    mxSetField(mxData,0,"complexity",mxCreateDoubleScalar(0));
    mxSetField(mxAutoinheritanceInfo,0,"inputs",mxData);
  }

  {
    mxSetField(mxAutoinheritanceInfo,0,"parameters",mxCreateDoubleMatrix(0,0,
                mxREAL));
  }

  {
    mxSetField(mxAutoinheritanceInfo,0,"outputs",mxCreateDoubleMatrix(0,0,mxREAL));
  }

  {
    mxSetField(mxAutoinheritanceInfo,0,"locals",mxCreateDoubleMatrix(0,0,mxREAL));
  }

  {
    mxArray* mxPostCodegenInfo = sf_c2_prob2_get_post_codegen_info();
    mxSetField(mxAutoinheritanceInfo,0,"postCodegenInfo",mxPostCodegenInfo);
  }

  return(mxAutoinheritanceInfo);
}

mxArray *sf_c2_prob2_third_party_uses_info(void)
{
  mxArray * mxcell3p = mxCreateCellMatrix(1,0);
  return(mxcell3p);
}

mxArray *sf_c2_prob2_jit_fallback_info(void)
{
  const char *infoFields[] = { "fallbackType", "fallbackReason",
    "hiddenFallbackType", "hiddenFallbackReason", "incompatibleSymbol" };

  mxArray *mxInfo = mxCreateStructMatrix(1, 1, 5, infoFields);
  mxArray *fallbackType = mxCreateString("late");
  mxArray *fallbackReason = mxCreateString("third_party_libs");
  mxArray *hiddenFallbackType = mxCreateString("");
  mxArray *hiddenFallbackReason = mxCreateString("");
  mxArray *incompatibleSymbol = mxCreateString("auxInfo:includeFiles");
  mxSetField(mxInfo, 0, infoFields[0], fallbackType);
  mxSetField(mxInfo, 0, infoFields[1], fallbackReason);
  mxSetField(mxInfo, 0, infoFields[2], hiddenFallbackType);
  mxSetField(mxInfo, 0, infoFields[3], hiddenFallbackReason);
  mxSetField(mxInfo, 0, infoFields[4], incompatibleSymbol);
  return mxInfo;
}

mxArray *sf_c2_prob2_updateBuildInfo_args_info(void)
{
  mxArray *mxBIArgs = mxCreateCellMatrix(1,0);
  return mxBIArgs;
}

mxArray* sf_c2_prob2_get_post_codegen_info(void)
{
  const char* fieldNames[] = { "exportedFunctionsUsedByThisChart",
    "exportedFunctionsChecksum" };

  mwSize dims[2] = { 1, 1 };

  mxArray* mxPostCodegenInfo = mxCreateStructArray(2, dims, sizeof(fieldNames)/
    sizeof(fieldNames[0]), fieldNames);

  {
    mxArray* mxExportedFunctionsChecksum = mxCreateString("");
    mwSize exp_dims[2] = { 0, 1 };

    mxArray* mxExportedFunctionsUsedByThisChart = mxCreateCellArray(2, exp_dims);
    mxSetField(mxPostCodegenInfo, 0, "exportedFunctionsUsedByThisChart",
               mxExportedFunctionsUsedByThisChart);
    mxSetField(mxPostCodegenInfo, 0, "exportedFunctionsChecksum",
               mxExportedFunctionsChecksum);
  }

  return mxPostCodegenInfo;
}

static const mxArray *sf_get_sim_state_info_c2_prob2(void)
{
  const char *infoFields[] = { "chartChecksum", "varInfo" };

  mxArray *mxInfo = mxCreateStructMatrix(1, 1, 2, infoFields);
  const char *infoEncStr[] = {
    "100 S1x2'type','srcId','name','auxInfo'{{M[4],M[0],T\"firstTime\",S'l','i','p'{{M1x2[477 486],M[0],}}},{M[8],M[0],T\"is_active_c2_prob2\",}}"
  };

  mxArray *mxVarInfo = sf_mex_decode_encoded_mx_struct_array(infoEncStr, 2, 10);
  mxArray *mxChecksum = mxCreateDoubleMatrix(1, 4, mxREAL);
  sf_c2_prob2_get_check_sum(&mxChecksum);
  mxSetField(mxInfo, 0, infoFields[0], mxChecksum);
  mxSetField(mxInfo, 0, infoFields[1], mxVarInfo);
  return mxInfo;
}

static void chart_debug_initialization(SimStruct *S, unsigned int
  fullDebuggerInitialization)
{
  if (!sim_mode_is_rtw_gen(S)) {
    SFc2_prob2InstanceStruct *chartInstance;
    ChartRunTimeInfo * crtInfo = (ChartRunTimeInfo *)(ssGetUserData(S));
    ChartInfoStruct * chartInfo = (ChartInfoStruct *)(crtInfo->instanceInfo);
    chartInstance = (SFc2_prob2InstanceStruct *) chartInfo->chartInstance;
    if (ssIsFirstInitCond(S) && fullDebuggerInitialization==1) {
      /* do this only if simulation is starting */
      {
        unsigned int chartAlreadyPresent;
        chartAlreadyPresent = sf_debug_initialize_chart
          (sfGlobalDebugInstanceStruct,
           _prob2MachineNumber_,
           2,
           1,
           1,
           0,
           1,
           0,
           0,
           0,
           0,
           0,
           &(chartInstance->chartNumber),
           &(chartInstance->instanceNumber),
           (void *)S);

        /* Each instance must initialize its own list of scripts */
        init_script_number_translation(_prob2MachineNumber_,
          chartInstance->chartNumber,chartInstance->instanceNumber);
        if (chartAlreadyPresent==0) {
          /* this is the first instance */
          sf_debug_set_chart_disable_implicit_casting
            (sfGlobalDebugInstanceStruct,_prob2MachineNumber_,
             chartInstance->chartNumber,1);
          sf_debug_set_chart_event_thresholds(sfGlobalDebugInstanceStruct,
            _prob2MachineNumber_,
            chartInstance->chartNumber,
            0,
            0,
            0);
          _SFD_SET_DATA_PROPS(0,1,1,0,"u");
          _SFD_STATE_INFO(0,0,2);
          _SFD_CH_SUBSTATE_COUNT(0);
          _SFD_CH_SUBSTATE_DECOMP(0);
        }

        _SFD_CV_INIT_CHART(0,0,0,0);

        {
          _SFD_CV_INIT_STATE(0,0,0,0,0,0,NULL,NULL);
        }

        _SFD_CV_INIT_TRANS(0,0,NULL,NULL,0,NULL);

        /* Initialization of MATLAB Function Model Coverage */
        _SFD_CV_INIT_EML(0,1,2,0,4,0,0,0,0,0,0,0);
        _SFD_CV_INIT_EML_FCN(0,0,"eML_blk_kernel",0,-1,1318);
        _SFD_CV_INIT_EML_FCN(0,1,"c_string",1320,-1,1448);
        _SFD_CV_INIT_EML_IF(0,1,0,529,550,-1,997);
        _SFD_CV_INIT_EML_IF(0,1,1,574,605,934,993);
        _SFD_CV_INIT_EML_IF(0,1,2,1046,1056,1131,1213);
        _SFD_CV_INIT_EML_IF(0,1,3,1214,1245,1290,1313);
        _SFD_CV_INIT_EML_RELATIONAL(0,1,0,1050,1055,-1,4);
        _SFD_SET_DATA_COMPILED_PROPS(0,SF_DOUBLE,0,NULL,0,0,0,0.0,1.0,0,0,
          (MexFcnForType)c2_b_sf_marshallOut,(MexInFcnForType)NULL);
      }
    } else {
      sf_debug_reset_current_state_configuration(sfGlobalDebugInstanceStruct,
        _prob2MachineNumber_,chartInstance->chartNumber,
        chartInstance->instanceNumber);
    }
  }
}

static void chart_debug_initialize_data_addresses(SimStruct *S)
{
  if (!sim_mode_is_rtw_gen(S)) {
    SFc2_prob2InstanceStruct *chartInstance;
    ChartRunTimeInfo * crtInfo = (ChartRunTimeInfo *)(ssGetUserData(S));
    ChartInfoStruct * chartInfo = (ChartInfoStruct *)(crtInfo->instanceInfo);
    chartInstance = (SFc2_prob2InstanceStruct *) chartInfo->chartInstance;
    if (ssIsFirstInitCond(S)) {
      /* do this only if simulation is starting and after we know the addresses of all data */
      {
        _SFD_SET_DATA_VALUE_PTR(0U, chartInstance->c2_u);
      }
    }
  }
}

static const char* sf_get_instance_specialization(void)
{
  return "sSNdYVqXUk2JYMyn5KzTU2E";
}

static void sf_opaque_initialize_c2_prob2(void *chartInstanceVar)
{
  chart_debug_initialization(((SFc2_prob2InstanceStruct*) chartInstanceVar)->S,0);
  initialize_params_c2_prob2((SFc2_prob2InstanceStruct*) chartInstanceVar);
  initialize_c2_prob2((SFc2_prob2InstanceStruct*) chartInstanceVar);
}

static void sf_opaque_enable_c2_prob2(void *chartInstanceVar)
{
  enable_c2_prob2((SFc2_prob2InstanceStruct*) chartInstanceVar);
}

static void sf_opaque_disable_c2_prob2(void *chartInstanceVar)
{
  disable_c2_prob2((SFc2_prob2InstanceStruct*) chartInstanceVar);
}

static void sf_opaque_gateway_c2_prob2(void *chartInstanceVar)
{
  sf_gateway_c2_prob2((SFc2_prob2InstanceStruct*) chartInstanceVar);
}

static const mxArray* sf_opaque_get_sim_state_c2_prob2(SimStruct* S)
{
  ChartRunTimeInfo * crtInfo = (ChartRunTimeInfo *)(ssGetUserData(S));
  ChartInfoStruct * chartInfo = (ChartInfoStruct *)(crtInfo->instanceInfo);
  return get_sim_state_c2_prob2((SFc2_prob2InstanceStruct*)
    chartInfo->chartInstance);         /* raw sim ctx */
}

static void sf_opaque_set_sim_state_c2_prob2(SimStruct* S, const mxArray *st)
{
  ChartRunTimeInfo * crtInfo = (ChartRunTimeInfo *)(ssGetUserData(S));
  ChartInfoStruct * chartInfo = (ChartInfoStruct *)(crtInfo->instanceInfo);
  set_sim_state_c2_prob2((SFc2_prob2InstanceStruct*)chartInfo->chartInstance, st);
}

static void sf_opaque_terminate_c2_prob2(void *chartInstanceVar)
{
  if (chartInstanceVar!=NULL) {
    SimStruct *S = ((SFc2_prob2InstanceStruct*) chartInstanceVar)->S;
    ChartRunTimeInfo * crtInfo = (ChartRunTimeInfo *)(ssGetUserData(S));
    if (sim_mode_is_rtw_gen(S) || sim_mode_is_external(S)) {
      sf_clear_rtw_identifier(S);
      unload_prob2_optimization_info();
    }

    finalize_c2_prob2((SFc2_prob2InstanceStruct*) chartInstanceVar);
    utFree(chartInstanceVar);
    if (crtInfo != NULL) {
      utFree(crtInfo);
    }

    ssSetUserData(S,NULL);
  }
}

static void sf_opaque_init_subchart_simstructs(void *chartInstanceVar)
{
  initSimStructsc2_prob2((SFc2_prob2InstanceStruct*) chartInstanceVar);
}

extern unsigned int sf_machine_global_initializer_called(void);
static void mdlProcessParameters_c2_prob2(SimStruct *S)
{
  int i;
  for (i=0;i<ssGetNumRunTimeParams(S);i++) {
    if (ssGetSFcnParamTunable(S,i)) {
      ssUpdateDlgParamAsRunTimeParam(S,i);
    }
  }

  if (sf_machine_global_initializer_called()) {
    ChartRunTimeInfo * crtInfo = (ChartRunTimeInfo *)(ssGetUserData(S));
    ChartInfoStruct * chartInfo = (ChartInfoStruct *)(crtInfo->instanceInfo);
    initialize_params_c2_prob2((SFc2_prob2InstanceStruct*)
      (chartInfo->chartInstance));
  }
}

static void mdlSetWorkWidths_c2_prob2(SimStruct *S)
{
  ssMdlUpdateIsEmpty(S, 1);
  if (sim_mode_is_rtw_gen(S) || sim_mode_is_external(S)) {
    mxArray *infoStruct = load_prob2_optimization_info();
    int_T chartIsInlinable =
      (int_T)sf_is_chart_inlinable(sf_get_instance_specialization(),infoStruct,2);
    ssSetStateflowIsInlinable(S,chartIsInlinable);
    ssSetRTWCG(S,1);
    ssSetEnableFcnIsTrivial(S,1);
    ssSetDisableFcnIsTrivial(S,1);
    ssSetNotMultipleInlinable(S,sf_rtw_info_uint_prop
      (sf_get_instance_specialization(),infoStruct,2,
       "gatewayCannotBeInlinedMultipleTimes"));
    sf_update_buildInfo(sf_get_instance_specialization(),infoStruct,2);
    if (chartIsInlinable) {
      ssSetInputPortOptimOpts(S, 0, SS_REUSABLE_AND_LOCAL);
      sf_mark_chart_expressionable_inputs(S,sf_get_instance_specialization(),
        infoStruct,2,1);
    }

    {
      unsigned int outPortIdx;
      for (outPortIdx=1; outPortIdx<=0; ++outPortIdx) {
        ssSetOutputPortOptimizeInIR(S, outPortIdx, 1U);
      }
    }

    {
      unsigned int inPortIdx;
      for (inPortIdx=0; inPortIdx < 1; ++inPortIdx) {
        ssSetInputPortOptimizeInIR(S, inPortIdx, 1U);
      }
    }

    sf_set_rtw_dwork_info(S,sf_get_instance_specialization(),infoStruct,2);
    ssSetHasSubFunctions(S,!(chartIsInlinable));
  } else {
  }

  ssSetOptions(S,ssGetOptions(S)|SS_OPTION_WORKS_WITH_CODE_REUSE);
  ssSetChecksum0(S,(2414119115U));
  ssSetChecksum1(S,(2489495850U));
  ssSetChecksum2(S,(4119885834U));
  ssSetChecksum3(S,(1999319305U));
  ssSetmdlDerivatives(S, NULL);
  ssSetExplicitFCSSCtrl(S,1);
  ssSupportsMultipleExecInstances(S,1);
}

static void mdlRTW_c2_prob2(SimStruct *S)
{
  if (sim_mode_is_rtw_gen(S)) {
    ssWriteRTWStrParam(S, "StateflowChartType", "Embedded MATLAB");
  }
}

static void mdlStart_c2_prob2(SimStruct *S)
{
  SFc2_prob2InstanceStruct *chartInstance;
  ChartRunTimeInfo * crtInfo = (ChartRunTimeInfo *)utMalloc(sizeof
    (ChartRunTimeInfo));
  chartInstance = (SFc2_prob2InstanceStruct *)utMalloc(sizeof
    (SFc2_prob2InstanceStruct));
  memset(chartInstance, 0, sizeof(SFc2_prob2InstanceStruct));
  if (chartInstance==NULL) {
    sf_mex_error_message("Could not allocate memory for chart instance.");
  }

  chartInstance->chartInfo.chartInstance = chartInstance;
  chartInstance->chartInfo.isEMLChart = 1;
  chartInstance->chartInfo.chartInitialized = 0;
  chartInstance->chartInfo.sFunctionGateway = sf_opaque_gateway_c2_prob2;
  chartInstance->chartInfo.initializeChart = sf_opaque_initialize_c2_prob2;
  chartInstance->chartInfo.terminateChart = sf_opaque_terminate_c2_prob2;
  chartInstance->chartInfo.enableChart = sf_opaque_enable_c2_prob2;
  chartInstance->chartInfo.disableChart = sf_opaque_disable_c2_prob2;
  chartInstance->chartInfo.getSimState = sf_opaque_get_sim_state_c2_prob2;
  chartInstance->chartInfo.setSimState = sf_opaque_set_sim_state_c2_prob2;
  chartInstance->chartInfo.getSimStateInfo = sf_get_sim_state_info_c2_prob2;
  chartInstance->chartInfo.zeroCrossings = NULL;
  chartInstance->chartInfo.outputs = NULL;
  chartInstance->chartInfo.derivatives = NULL;
  chartInstance->chartInfo.mdlRTW = mdlRTW_c2_prob2;
  chartInstance->chartInfo.mdlStart = mdlStart_c2_prob2;
  chartInstance->chartInfo.mdlSetWorkWidths = mdlSetWorkWidths_c2_prob2;
  chartInstance->chartInfo.extModeExec = NULL;
  chartInstance->chartInfo.restoreLastMajorStepConfiguration = NULL;
  chartInstance->chartInfo.restoreBeforeLastMajorStepConfiguration = NULL;
  chartInstance->chartInfo.storeCurrentConfiguration = NULL;
  chartInstance->chartInfo.callAtomicSubchartUserFcn = NULL;
  chartInstance->chartInfo.callAtomicSubchartAutoFcn = NULL;
  chartInstance->chartInfo.debugInstance = sfGlobalDebugInstanceStruct;
  chartInstance->S = S;
  crtInfo->isEnhancedMooreMachine = 0;
  crtInfo->checksum = SF_RUNTIME_INFO_CHECKSUM;
  crtInfo->fCheckOverflow = sf_runtime_overflow_check_is_on(S);
  crtInfo->instanceInfo = (&(chartInstance->chartInfo));
  crtInfo->isJITEnabled = false;
  crtInfo->compiledInfo = NULL;
  ssSetUserData(S,(void *)(crtInfo));  /* register the chart instance with simstruct */
  init_dsm_address_info(chartInstance);
  init_simulink_io_address(chartInstance);
  if (!sim_mode_is_rtw_gen(S)) {
  }

  chart_debug_initialization(S,1);
}

void c2_prob2_method_dispatcher(SimStruct *S, int_T method, void *data)
{
  switch (method) {
   case SS_CALL_MDL_START:
    mdlStart_c2_prob2(S);
    break;

   case SS_CALL_MDL_SET_WORK_WIDTHS:
    mdlSetWorkWidths_c2_prob2(S);
    break;

   case SS_CALL_MDL_PROCESS_PARAMETERS:
    mdlProcessParameters_c2_prob2(S);
    break;

   default:
    /* Unhandled method */
    sf_mex_error_message("Stateflow Internal Error:\n"
                         "Error calling c2_prob2_method_dispatcher.\n"
                         "Can't handle method %d.\n", method);
    break;
  }
}
