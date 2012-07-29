source $VIMRUNTIME/vimrc_example.vim
source $VIMRUNTIME/mswin.vim
behave mswin

set diffexpr=MyDiff()
function MyDiff()
  let opt = '-a --binary '
  if &diffopt =~ 'icase' | let opt = opt . '-i ' | endif
  if &diffopt =~ 'iwhite' | let opt = opt . '-b ' | endif
  let arg1 = v:fname_in
  if arg1 =~ ' ' | let arg1 = '"' . arg1 . '"' | endif
  let arg2 = v:fname_new
  if arg2 =~ ' ' | let arg2 = '"' . arg2 . '"' | endif
  let arg3 = v:fname_out
  if arg3 =~ ' ' | let arg3 = '"' . arg3 . '"' | endif
  let eq = ''
  if $VIMRUNTIME =~ ' '
    if &sh =~ '\<cmd'
      let cmd = '""' . $VIMRUNTIME . '\diff"'
      let eq = '"'
    else
      let cmd = substitute($VIMRUNTIME, ' ', '" ', '') . '\diff"'
    endif
  else
    let cmd = $VIMRUNTIME . '\diff'
  endif
  silent execute '!' . cmd . ' ' . opt . arg1 . ' ' . arg2 . ' > ' . arg3 . eq
endfunction

"GUI stuff
set nu
colo wombat
highlight LineNr term=bold cterm=NONE ctermfg=White ctermbg=None gui=NONE guifg=Grey guibg=NONE
set gfn=Ubuntu_Mono:h12:cANSI
set guioptions-=T  "remove toolbar
set encoding=utf-8
set cul
set ruler
set laststatus=2
set wrap
set textwidth=79
set formatoptions=qrn1
set colorcolumn=85

"Actual setting
set nocompatible
set ts=4 sw=4 sts=4 noexpandtab
set autoindent
set smartindent
set ignorecase
set smartcase
set matchtime=2
set matchpairs+=<:>
set gdefault
nnoremap <leader><space> :noh<cr>

"remap
inoremap <F1> <ESC>
nnoremap <F1> <ESC>
vnoremap <F1> <ESC>

" Shortcut to rapidly toggle `set list`
nmap <leader>l :set list!<CR>

" Use the same symbols as TextMate for tabstops and EOLs
set listchars=tab:»\ ,eol:¬

nnoremap <leader>rc :e $MYVIMRC<cr>
inoremap jj <ESC>

" minibufexplorer
map <Leader>b :MiniBufExplorer<cr>
let g:miniBufExplUseSingleClick = 1
