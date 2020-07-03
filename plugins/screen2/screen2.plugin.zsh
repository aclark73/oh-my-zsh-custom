function screen_prompt_info() {
  [[ -n "$STY" ]] || return
  name="${${(s:.:)STY}[2]}"
  echo "${ZSH_THEME_SCREEN_PREFIX:=\{}${name}${ZSH_THEME_SCREEN_SUFFIX:=\}}"
}
