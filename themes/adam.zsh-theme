if [[ -z `functions screen_prompt_info` ]] ; then
    function screen_prompt_info() {
        return
    }
fi

if [[ -z `functions git_repo_name` ]] ; then
    function git_repo_name() {
      ref=$(git rev-parse --show-toplevel 2> /dev/null) || return
      echo "$ref"
    }
fi

if [[ -z `functions machine_color` ]] ; then
    function machine_color() {
      return
    }
fi

PROMPT='%(?,✅,🚫) %% '
# RPS1='%{$fg[blue]%}%~%{$reset_color%} '
# base_color="$(machine_color)"
base_color="blue"
prompt_prefix="%{%F{$base_color}%}"
RPS1='$prompt_prefix%m:%2~$(screen_prompt_info)$(git_prompt_info)$(conda_env_prompt_info)$(virtualenv_prompt_info)%{$reset_color%} %T⏰ '

ZSH_THEME_SCREEN_PREFIX=" %{$fg[grey]%}"
ZSH_THEME_SCREEN_SUFFIX="💻"

ZSH_THEME_VIRTUALENV_PREFIX=" %{$fg[blue]%}"
ZSH_THEME_VIRTUALENV_SUFFIX="🌎"

ZSH_THEME_CONDA_ENV_PREFIX=" %{$fg[blue]%}"
ZSH_THEME_CONDA_ENV_SUFFIX="🌎"

ZSH_THEME_GIT_PROMPT_PREFIX=" %{$fg[yellow]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX=""
ZSH_THEME_GIT_PROMPT_CLEAN="🌷"
ZSH_THEME_GIT_PROMPT_DIRTY="💩"
ZSH_THEME_GIT_PROMPT_AHEAD="🔥"
