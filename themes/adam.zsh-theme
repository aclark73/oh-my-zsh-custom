if [[ -z `functions screen_prompt_info` ]] ; then
    function screen_prompt_info() {
        return
    }
fi


PROMPT='%(?,✅,🚫) %% '
# RPS1='%{$fg[blue]%}%~%{$reset_color%} '
machine_color=$fg[blue]
RPS1='%{$machine_color%}%m:%2~$(screen_prompt_info)$(git_prompt_info)$(conda_env_prompt_info)$(virtualenv_prompt_info)%{$reset_color%} %T⏰ '

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
