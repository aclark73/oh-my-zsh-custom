# Set the iTerm2 tab color based on the VIRTUAL_ENV
if [[ "$TERM_PROGRAM" == "iTerm.app" ]] && [[ -z "$INSIDE_EMACS" ]]; then
  pyscript="${0%/*}/set-tab-color.py"
  tab_name=""
  if [[ -z `functions zsh_iterm2_tab_name` ]] ; then
    function zsh_iterm2_tab_name() {
      ref=$(git rev-parse --show-toplevel 2> /dev/null) || \
      ref=$(echo "${1:-$(svn info 2> /dev/null)}" | grep '^Working\ Copy\ Root\ Path:' | sed 's#^[^/]*##') || return
      echo "$ref"
    }
  fi
  update_tab_color() {
    _tab_name="$(zsh_iterm2_tab_name)"
    if [[ "$_tab_name" != "$tab_name" ]]; then
      # echo "Updating to $_tab_name"
      tab_name="$_tab_name"
      python "$pyscript" $tab_name
    fi
  }

  autoload add-zsh-hook
  add-zsh-hook precmd update_tab_color

  # Tell the terminal about the initial directory.
  update_tab_color
fi
