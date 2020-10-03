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
      echo blue
    }
fi

prompt_color="%(?,$FG[028],$FG[124])"
PROMPT='${SSH_CLIENT+%m}%{$prompt_color%}%%%{$reset_color%} '
# PROMPT='%{$prompt_color%}%%%{$reset_color%} '
# PROMPT='%(?,✅,🚫) %% '
# RPS1='%{$fg[blue]%}%~%{$reset_color%} '
# base_color="$(machine_color)"
# base_color="blue"
machine_color=$fg[blue]
RPS1='%{$machine_color%}%2~$(screen_prompt_info)$(git_prompt_info)$(conda_env_prompt_info)$(virtualenv_prompt_info)%{$reset_color%} %T '

ZSH_THEME_SCREEN_PREFIX=" %{$fg[grey]%}"
ZSH_THEME_SCREEN_SUFFIX=""

ZSH_THEME_VIRTUALENV_PREFIX=" %{$fg[100]%}"
ZSH_THEME_VIRTUALENV_SUFFIX="%{$reset_color%}"

ZSH_THEME_CONDA_ENV_PREFIX=" %{$FG[100]%}"
ZSH_THEME_CONDA_ENV_SUFFIX="%{$reset_color%}"

ZSH_THEME_GIT_PROMPT_PREFIX=" %{$FG[021]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_CLEAN="."
ZSH_THEME_GIT_PROMPT_DIRTY="!"
ZSH_THEME_GIT_PROMPT_AHEAD="!!"
