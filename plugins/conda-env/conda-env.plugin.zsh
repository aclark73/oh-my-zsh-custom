function conda_env_prompt_info(){
  [[ -n ${CONDA_DEFAULT_ENV} ]] || return
  echo "${ZSH_THEME_CONDA_ENV_PREFIX:=[}${CONDA_DEFAULT_ENV:t}${ZSH_THEME_CONDA_ENV_SUFFIX:=]}"
}
