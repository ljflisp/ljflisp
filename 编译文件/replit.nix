{ pkgs }: {
  deps = [
   # pkgs.replit害群之马  
   # pkgs.rust-edit
   # pkgs.run
       pkgs.lolcode                            # pkgs.csound
        pkgs.vimHugeX
                                                                                                                          pkgs.dune_2
                                                                                                                          pkgs.yacc
                                                                                                                          pkgs.hol
                                                                                                                          pkgs.mercury
                                                                                                                          pkgs.wget
                                                                                                                          pkgs.wasmer
                                                                                                                          pkgs.apacheHttpd
                                                                                                                          pkgs.vlang
                                                                                                                          pkgs.zig
                                                                                                                          pkgs.run
                                                                                                                          pkgs.gfortran10
                                                                                                                          pkgs.rename
                                                                                                                          pkgs.cln
                                                                                                                          pkgs.hpx
                                                                                                                          pkgs.emacs
      pkgs.cask
    pkgs.sqlite
    pkgs.gotools  
                                    pkgs.R
         pkgs.scala
                                                 pkgs.rWrapper
                                                 pkgs.gnustep-make
                                  
                                                 pkgs.clojure
                                                 pkgs.clisp
                                                 pkgs.ts
                                                 pkgs.haxe
                                                 pkgs.bs-platform
                                                 pkgs.gdc
                                                 pkgs.dart_stable
                                                 pkgs.llvmPackages_9.clang-unwrapped
                                                 pkgs.erlang
                                                 pkgs.swift
                                                 pkgs.gh
                                                 pkgs.haskellPackages.ghc
                                                 pkgs.mono
                                                 pkgs.fsharp
                                                 pkgs.kotlin
                                                 pkgs.bc                              
                                                                                                                                                pkgs.php74
                                                                                                                                                                                                                                pkgs.cargo
                                                                                                                                                                                                                                pkgs.rustc
      pkgs.rust-analyzer
    pkgs.rustfmt
                                                                                                                                                                                                                                pkgs.rakudo
                                                                                                                                                  pkgs.nodejs-16_x
                                                                                                                                                               pkgs.lua
                                                                               pkgs.gnumake
    pkgs.dotnet-sdk  
    pkgs.haskellPackages.yabi           
    pkgs.tcl
    #pkgs.julia-bin
    pkgs.ruby
    pkgs.bat
    pkgs.python3
    pkgs.crystal
    pkgs.elixir
    pkgs.go
    pkgs.replitPackages.replbox
    pkgs.graalvm17-ce
    pkgs.haskellPackages.yabi
    pkgs.fpc
    pkgs.gcc
		pkgs.nim-unwrapped
		pkgs.nimble-unwrapped
    pkgs.gforth
    pkgs.guile_3_0
    pkgs.gnuapl
    pkgs.replitPackages.basil
    pkgs.tcl
    pkgs.gnu-cobol
   # pkgs.gdc
    pkgs.haxe
    pkgs.go
    pkgs.gopls
    #pkgs.java
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      # Needed for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
      # Needed for matplotlib
      pkgs.xorg.libX11
    ];
    PYTHONBIN = "${pkgs.python310}/bin/python3.10";
    LANG = "en_US.UTF-8";
  };
}

