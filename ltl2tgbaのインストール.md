LTL2TGBA (by SPOT)のインストール

http://spot.lip6.fr/wiki/GetSpot

`./configure && make && make check && make install' 

./configure がBoost ライブラリがないよと言って止まったので
brew install boost
転ぶならこちら．
> http://qiita.com/dtan4/items/9d868ee277bd37b1e30f

ltl3baと違って make はgcc4.9でもapplellvmでも動くみたいだ．

make は，10分以上かかる．

make check は1時間以上かかる．

sudo make install

ltl2tgbaが使えるようになった．






-------make check-----------
Genderme:spot-1.2.4 taka$ make check
Making check in buddy
Making check in src
/Library/Developer/CommandLineTools/usr/bin/make  bddtest
g++ -DHAVE_CONFIG_H   -I.. -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -MT bddtest-bddtest.o -MD -MP -MF .deps/bddtest-bddtest.Tpo -c -o bddtest-bddtest.o `test -f 'bddtest.cxx' || echo './'`bddtest.cxx
mv -f .deps/bddtest-bddtest.Tpo .deps/bddtest-bddtest.Po
/bin/sh ../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3   -o bddtest bddtest-bddtest.o ./libbdd.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -o .libs/bddtest bddtest-bddtest.o -Wl,-bind_at_load  ./.libs/libbdd.dylib
Making check in examples
Making check in adder
/Library/Developer/CommandLineTools/usr/bin/make  adder
g++ -DHAVE_CONFIG_H   -I../../src -I. -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -MT adder.o -MD -MP -MF .deps/adder.Tpo -c -o adder.o adder.cxx
mv -f .deps/adder.Tpo .deps/adder.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3   -o adder adder.o ../../src/libbdd.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -o .libs/adder adder.o -Wl,-bind_at_load  ../../src/.libs/libbdd.dylib
Making check in bddcalc
/Library/Developer/CommandLineTools/usr/bin/make  check-am
/Library/Developer/CommandLineTools/usr/bin/make  bddcalc
g++ -DHAVE_CONFIG_H   -I../../src -I. -I. -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -MT hashtbl.o -MD -MP -MF .deps/hashtbl.Tpo -c -o hashtbl.o hashtbl.cxx
mv -f .deps/hashtbl.Tpo .deps/hashtbl.Po
g++ -DHAVE_CONFIG_H   -I../../src -I. -I. -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -MT lexer.o -MD -MP -MF .deps/lexer.Tpo -c -o lexer.o lexer.cxx
mv -f .deps/lexer.Tpo .deps/lexer.Po
g++ -DHAVE_CONFIG_H   -I../../src -I. -I. -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -MT parser_.o -MD -MP -MF .deps/parser_.Tpo -c -o parser_.o parser_.cxx
In file included from parser_.cxx:16:
In file included from parser.y:14:
./slist.h:221:3: warning: cannot delete expression with pointer-to-'void' type 'void *'
         delete next->data;
         ^      ~~~~~~~~~~
1 warning generated.
mv -f .deps/parser_.Tpo .deps/parser_.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3   -o bddcalc hashtbl.o lexer.o parser_.o ../../src/libbdd.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -o .libs/bddcalc hashtbl.o lexer.o parser_.o -Wl,-bind_at_load  ../../src/.libs/libbdd.dylib
Making check in bddtest
/Library/Developer/CommandLineTools/usr/bin/make  bddtest
g++ -DHAVE_CONFIG_H   -I../../src -I. -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -MT bddtest.o -MD -MP -MF .deps/bddtest.Tpo -c -o bddtest.o bddtest.cxx
mv -f .deps/bddtest.Tpo .deps/bddtest.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3   -o bddtest bddtest.o ../../src/libbdd.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -o .libs/bddtest bddtest.o -Wl,-bind_at_load  ../../src/.libs/libbdd.dylib
Making check in cmilner
/Library/Developer/CommandLineTools/usr/bin/make  cmilner
gcc -DHAVE_CONFIG_H   -I../../src -I. -DNDEBUG  -fvisibility=hidden -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT cmilner.o -MD -MP -MF .deps/cmilner.Tpo -c -o cmilner.o cmilner.c
mv -f .deps/cmilner.Tpo .deps/cmilner.Po
/bin/sh ../../libtool  --tag=CC   --mode=link gcc  -fvisibility=hidden -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o cmilner cmilner.o ../../src/libbdd.la -lm 
libtool: link: gcc -fvisibility=hidden -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/cmilner cmilner.o  ../../src/.libs/libbdd.dylib -lm
Making check in fdd
/Library/Developer/CommandLineTools/usr/bin/make  fdd
g++ -DHAVE_CONFIG_H   -I../../src -I. -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -MT fdd.o -MD -MP -MF .deps/fdd.Tpo -c -o fdd.o fdd.cxx
mv -f .deps/fdd.Tpo .deps/fdd.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3   -o fdd fdd.o ../../src/libbdd.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -o .libs/fdd fdd.o -Wl,-bind_at_load  ../../src/.libs/libbdd.dylib
Making check in milner
/Library/Developer/CommandLineTools/usr/bin/make  milner
g++ -DHAVE_CONFIG_H   -I../../src -I. -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -MT milner.o -MD -MP -MF .deps/milner.Tpo -c -o milner.o milner.cxx
mv -f .deps/milner.Tpo .deps/milner.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3   -o milner milner.o ../../src/libbdd.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -o .libs/milner milner.o -Wl,-bind_at_load  ../../src/.libs/libbdd.dylib
Making check in money
/Library/Developer/CommandLineTools/usr/bin/make  money
g++ -DHAVE_CONFIG_H   -I../../src -I. -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -MT money.o -MD -MP -MF .deps/money.Tpo -c -o money.o money.cxx
mv -f .deps/money.Tpo .deps/money.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3   -o money money.o ../../src/libbdd.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -o .libs/money money.o -Wl,-bind_at_load  ../../src/.libs/libbdd.dylib
Making check in queen
/Library/Developer/CommandLineTools/usr/bin/make  queen
g++ -DHAVE_CONFIG_H   -I../../src -I. -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -MT queen.o -MD -MP -MF .deps/queen.Tpo -c -o queen.o queen.cxx
mv -f .deps/queen.Tpo .deps/queen.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3   -o queen queen.o ../../src/libbdd.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -o .libs/queen queen.o -Wl,-bind_at_load  ../../src/.libs/libbdd.dylib
Making check in solitare
/Library/Developer/CommandLineTools/usr/bin/make  solitare
g++ -DHAVE_CONFIG_H   -I../../src -I. -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -MT solitare.o -MD -MP -MF .deps/solitare.Tpo -c -o solitare.o solitare.cxx
mv -f .deps/solitare.Tpo .deps/solitare.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -g -O3   -o solitare solitare.o ../../src/libbdd.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -g -O3 -o .libs/solitare solitare.o -Wl,-bind_at_load  ../../src/.libs/libbdd.dylib
make[3]: Nothing to be done for `check-am'.
Making check in doc
make[2]: Nothing to be done for `check'.
make[2]: Nothing to be done for `check-am'.
Making check in lib
/Library/Developer/CommandLineTools/usr/bin/make  check-recursive
make[3]: Nothing to be done for `check-am'.
Making check in src
Making check in misc
make[2]: Nothing to be done for `check'.
Making check in priv
make[2]: Nothing to be done for `check'.
Making check in ltlenv
make[2]: Nothing to be done for `check'.
Making check in ltlast
make[2]: Nothing to be done for `check'.
Making check in ltlvisit
make[2]: Nothing to be done for `check'.
Making check in ltlparse
/Library/Developer/CommandLineTools/usr/bin/make  check-am
make[3]: Nothing to be done for `check-am'.
Making check in eltlparse
/Library/Developer/CommandLineTools/usr/bin/make  check-am
make[3]: Nothing to be done for `check-am'.
Making check in tgba
make[2]: Nothing to be done for `check'.
Making check in tgbaalgos
Making check in gtec
make[3]: Nothing to be done for `check'.
make[3]: Nothing to be done for `check-am'.
Making check in tgbaparse
/Library/Developer/CommandLineTools/usr/bin/make  check-am
make[3]: Nothing to be done for `check-am'.
Making check in ta
make[2]: Nothing to be done for `check'.
Making check in taalgos
make[2]: Nothing to be done for `check'.
Making check in kripke
make[2]: Nothing to be done for `check'.
Making check in saba
make[2]: Nothing to be done for `check'.
Making check in sabaalgos
make[2]: Nothing to be done for `check'.
Making check in neverparse
/Library/Developer/CommandLineTools/usr/bin/make  check-am
make[3]: Nothing to be done for `check-am'.
Making check in kripkeparse
/Library/Developer/CommandLineTools/usr/bin/make  check-am
make[3]: Nothing to be done for `check-am'.
Making check in dstarparse
/Library/Developer/CommandLineTools/usr/bin/make  check-am
make[3]: Nothing to be done for `check-am'.
Making check in .
make[2]: Nothing to be done for `check-am'.
Making check in bin
Making check in .
make[3]: Nothing to be done for `check-am'.
Making check in man
make[3]: Nothing to be done for `check'.
Making check in ltltest
/Library/Developer/CommandLineTools/usr/bin/make  consterm equals kind length ltl2dot ltl2text ltlrel lunabbrev nenoform reduc reduccmp reduceu reductau reductaustr syntimpl tostring tunabbrev tunenoform unabbrevwm defs
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT consterm.o -MD -MP -MF .deps/consterm.Tpo -c -o consterm.o consterm.cc
mv -f .deps/consterm.Tpo .deps/consterm.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o consterm consterm.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/consterm consterm.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT equals.o -MD -MP -MF .deps/equals.Tpo -c -o equals.o equals.cc
mv -f .deps/equals.Tpo .deps/equals.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o equals equals.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/equals equals.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT kind.o -MD -MP -MF .deps/kind.Tpo -c -o kind.o kind.cc
mv -f .deps/kind.Tpo .deps/kind.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o kind kind.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/kind kind.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT length.o -MD -MP -MF .deps/length.Tpo -c -o length.o length.cc
mv -f .deps/length.Tpo .deps/length.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o length length.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/length length.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DDOTTY -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT ltl2dot-readltl.o -MD -MP -MF .deps/ltl2dot-readltl.Tpo -c -o ltl2dot-readltl.o `test -f 'readltl.cc' || echo './'`readltl.cc
mv -f .deps/ltl2dot-readltl.Tpo .deps/ltl2dot-readltl.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o ltl2dot ltl2dot-readltl.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/ltl2dot ltl2dot-readltl.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT readltl.o -MD -MP -MF .deps/readltl.Tpo -c -o readltl.o readltl.cc
mv -f .deps/readltl.Tpo .deps/readltl.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o ltl2text readltl.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/ltl2text readltl.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT ltlrel.o -MD -MP -MF .deps/ltlrel.Tpo -c -o ltlrel.o ltlrel.cc
mv -f .deps/ltlrel.Tpo .deps/ltlrel.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o ltlrel ltlrel.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/ltlrel ltlrel.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DLUNABBREV -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT lunabbrev-equals.o -MD -MP -MF .deps/lunabbrev-equals.Tpo -c -o lunabbrev-equals.o `test -f 'equals.cc' || echo './'`equals.cc
mv -f .deps/lunabbrev-equals.Tpo .deps/lunabbrev-equals.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o lunabbrev lunabbrev-equals.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/lunabbrev lunabbrev-equals.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNENOFORM -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT nenoform-equals.o -MD -MP -MF .deps/nenoform-equals.Tpo -c -o nenoform-equals.o `test -f 'equals.cc' || echo './'`equals.cc
mv -f .deps/nenoform-equals.Tpo .deps/nenoform-equals.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o nenoform nenoform-equals.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/nenoform nenoform-equals.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT reduc.o -MD -MP -MF .deps/reduc.Tpo -c -o reduc.o reduc.cc
mv -f .deps/reduc.Tpo .deps/reduc.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o reduc reduc.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/reduc reduc.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DREDUC -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT reduccmp-equals.o -MD -MP -MF .deps/reduccmp-equals.Tpo -c -o reduccmp-equals.o `test -f 'equals.cc' || echo './'`equals.cc
mv -f .deps/reduccmp-equals.Tpo .deps/reduccmp-equals.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o reduccmp reduccmp-equals.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/reduccmp reduccmp-equals.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DREDUC -DEVENT_UNIV -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT reduceu-equals.o -MD -MP -MF .deps/reduceu-equals.Tpo -c -o reduceu-equals.o `test -f 'equals.cc' || echo './'`equals.cc
mv -f .deps/reduceu-equals.Tpo .deps/reduceu-equals.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o reduceu reduceu-equals.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/reduceu reduceu-equals.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DREDUC_TAU -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT reductau-equals.o -MD -MP -MF .deps/reductau-equals.Tpo -c -o reductau-equals.o `test -f 'equals.cc' || echo './'`equals.cc
mv -f .deps/reductau-equals.Tpo .deps/reductau-equals.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o reductau reductau-equals.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/reductau reductau-equals.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DREDUC_TAUSTR -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT reductaustr-equals.o -MD -MP -MF .deps/reductaustr-equals.Tpo -c -o reductaustr-equals.o `test -f 'equals.cc' || echo './'`equals.cc
mv -f .deps/reductaustr-equals.Tpo .deps/reductaustr-equals.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o reductaustr reductaustr-equals.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/reductaustr reductaustr-equals.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT syntimpl.o -MD -MP -MF .deps/syntimpl.Tpo -c -o syntimpl.o syntimpl.cc
mv -f .deps/syntimpl.Tpo .deps/syntimpl.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o syntimpl syntimpl.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/syntimpl syntimpl.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT tostring.o -MD -MP -MF .deps/tostring.Tpo -c -o tostring.o tostring.cc
mv -f .deps/tostring.Tpo .deps/tostring.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o tostring tostring.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/tostring tostring.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DTUNABBREV -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT tunabbrev-equals.o -MD -MP -MF .deps/tunabbrev-equals.Tpo -c -o tunabbrev-equals.o `test -f 'equals.cc' || echo './'`equals.cc
mv -f .deps/tunabbrev-equals.Tpo .deps/tunabbrev-equals.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o tunabbrev tunabbrev-equals.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/tunabbrev tunabbrev-equals.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNENOFORM -DTUNABBREV -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT tunenoform-equals.o -MD -MP -MF .deps/tunenoform-equals.Tpo -c -o tunenoform-equals.o `test -f 'equals.cc' || echo './'`equals.cc
mv -f .deps/tunenoform-equals.Tpo .deps/tunenoform-equals.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o tunenoform tunenoform-equals.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/tunenoform tunenoform-equals.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DWM -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT unabbrevwm-equals.o -MD -MP -MF .deps/unabbrevwm-equals.Tpo -c -o unabbrevwm-equals.o `test -f 'equals.cc' || echo './'`equals.cc
mv -f .deps/unabbrevwm-equals.Tpo .deps/unabbrevwm-equals.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o unabbrevwm unabbrevwm-equals.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/unabbrevwm unabbrevwm-equals.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
make[3]: `defs' is up to date.
/Library/Developer/CommandLineTools/usr/bin/make  check-TESTS
PASS: bare.test
PASS: parse.test
PASS: parseerr.test
PASS: utf8.test
PASS: length.test
PASS: equals.test
PASS: tostring.test
PASS: lunabbrev.test
PASS: tunabbrev.test
PASS: nenoform.test
PASS: tunenoform.test
PASS: unabbrevwm.test
PASS: consterm.test
PASS: kind.test
PASS: remove_x.test
PASS: ltlrel.test
PASS: ltlfilt.test
PASS: latex.test
PASS: lbt.test
PASS: lenient.test
PASS: rand.test
PASS: isop.test
PASS: syntimpl.test
PASS: reduc.test
PASS: reduc0.test
PASS: reducpsl.test
PASS: reduccmp.test
PASS: uwrm.test
PASS: eventuniv.test
make[5]: Nothing to be done for `all'.
============================================================================
Testsuite summary for spot 1.2.4
============================================================================
# TOTAL: 29
# PASS:  29
# SKIP:  0
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
Making check in eltltest
/Library/Developer/CommandLineTools/usr/bin/make  acc nfa defs
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT acc.o -MD -MP -MF .deps/acc.Tpo -c -o acc.o acc.cc
mv -f .deps/acc.Tpo .deps/acc.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o acc acc.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/acc acc.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT nfa.o -MD -MP -MF .deps/nfa.Tpo -c -o nfa.o nfa.cc
mv -f .deps/nfa.Tpo .deps/nfa.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o nfa nfa.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/nfa nfa.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
make[3]: `defs' is up to date.
/Library/Developer/CommandLineTools/usr/bin/make  check-TESTS
PASS: acc.test
PASS: nfa.test
make[5]: Nothing to be done for `all'.
============================================================================
Testsuite summary for spot 1.2.4
============================================================================
# TOTAL: 2
# PASS:  2
# SKIP:  0
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
Making check in tgbatest
/Library/Developer/CommandLineTools/usr/bin/make  bddprod bitvect complement explicit explicit2 explicit3 expldot explprod intvcomp intvcmp2 ltlprod mixprod powerset readsat taatgba tgbaread tripprod defs
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG -DBDD_CONCRETE_PRODUCT -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT bddprod-ltlprod.o -MD -MP -MF .deps/bddprod-ltlprod.Tpo -c -o bddprod-ltlprod.o `test -f 'ltlprod.cc' || echo './'`ltlprod.cc
mv -f .deps/bddprod-ltlprod.Tpo .deps/bddprod-ltlprod.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++ -DBDD_CONCRETE_PRODUCT -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o bddprod bddprod-ltlprod.o ../libspot.la 
libtool: link: g++ -DBDD_CONCRETE_PRODUCT -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/bddprod bddprod-ltlprod.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT bitvect.o -MD -MP -MF .deps/bitvect.Tpo -c -o bitvect.o bitvect.cc
mv -f .deps/bitvect.Tpo .deps/bitvect.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o bitvect bitvect.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/bitvect bitvect.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT complementation.o -MD -MP -MF .deps/complementation.Tpo -c -o complementation.o complementation.cc
mv -f .deps/complementation.Tpo .deps/complementation.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o complement complementation.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/complement complementation.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT explicit.o -MD -MP -MF .deps/explicit.Tpo -c -o explicit.o explicit.cc
mv -f .deps/explicit.Tpo .deps/explicit.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o explicit explicit.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/explicit explicit.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT explicit2.o -MD -MP -MF .deps/explicit2.Tpo -c -o explicit2.o explicit2.cc
mv -f .deps/explicit2.Tpo .deps/explicit2.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o explicit2 explicit2.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/explicit2 explicit2.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT explicit3.o -MD -MP -MF .deps/explicit3.Tpo -c -o explicit3.o explicit3.cc
mv -f .deps/explicit3.Tpo .deps/explicit3.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o explicit3 explicit3.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/explicit3 explicit3.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG -DDOTTY -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT expldot-powerset.o -MD -MP -MF .deps/expldot-powerset.Tpo -c -o expldot-powerset.o `test -f 'powerset.cc' || echo './'`powerset.cc
mv -f .deps/expldot-powerset.Tpo .deps/expldot-powerset.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++ -DDOTTY -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o expldot expldot-powerset.o ../libspot.la 
libtool: link: g++ -DDOTTY -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/expldot expldot-powerset.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT explprod.o -MD -MP -MF .deps/explprod.Tpo -c -o explprod.o explprod.cc
mv -f .deps/explprod.Tpo .deps/explprod.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o explprod explprod.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/explprod explprod.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT intvcomp.o -MD -MP -MF .deps/intvcomp.Tpo -c -o intvcomp.o intvcomp.cc
mv -f .deps/intvcomp.Tpo .deps/intvcomp.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o intvcomp intvcomp.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/intvcomp intvcomp.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT intvcmp2.o -MD -MP -MF .deps/intvcmp2.Tpo -c -o intvcmp2.o intvcmp2.cc
mv -f .deps/intvcmp2.Tpo .deps/intvcmp2.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o intvcmp2 intvcmp2.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/intvcmp2 intvcmp2.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT ltlprod.o -MD -MP -MF .deps/ltlprod.Tpo -c -o ltlprod.o ltlprod.cc
mv -f .deps/ltlprod.Tpo .deps/ltlprod.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o ltlprod ltlprod.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/ltlprod ltlprod.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT mixprod.o -MD -MP -MF .deps/mixprod.Tpo -c -o mixprod.o mixprod.cc
mv -f .deps/mixprod.Tpo .deps/mixprod.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o mixprod mixprod.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/mixprod mixprod.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT powerset.o -MD -MP -MF .deps/powerset.Tpo -c -o powerset.o powerset.cc
mv -f .deps/powerset.Tpo .deps/powerset.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o powerset powerset.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/powerset powerset.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT readsat.o -MD -MP -MF .deps/readsat.Tpo -c -o readsat.o readsat.cc
mv -f .deps/readsat.Tpo .deps/readsat.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o readsat readsat.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/readsat readsat.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT taatgba.o -MD -MP -MF .deps/taatgba.Tpo -c -o taatgba.o taatgba.cc
mv -f .deps/taatgba.Tpo .deps/taatgba.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o taatgba taatgba.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/taatgba taatgba.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT tgbaread.o -MD -MP -MF .deps/tgbaread.Tpo -c -o tgbaread.o tgbaread.cc
mv -f .deps/tgbaread.Tpo .deps/tgbaread.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o tgbaread tgbaread.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/tgbaread tgbaread.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT tripprod.o -MD -MP -MF .deps/tripprod.Tpo -c -o tripprod.o tripprod.cc
mv -f .deps/tripprod.Tpo .deps/tripprod.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o tripprod tripprod.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/tripprod tripprod.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
make[3]: `defs' is up to date.
/Library/Developer/CommandLineTools/usr/bin/make  check-TESTS
PASS: intvcomp.test
PASS: bitvect.test
PASS: eltl2tgba.test
PASS: explicit.test
PASS: explicit2.test
PASS: ltlcross3.test
PASS: taatgba.test
PASS: tgbaread.test
PASS: renault.test
PASS: nondet.test
PASS: det.test
PASS: neverclaimread.test
PASS: dstar.test
PASS: readsave.test
PASS: simdet.test
PASS: sim.test
PASS: sim2.test
PASS: ltl2tgba.test
PASS: ltl2neverclaim.test
SKIP: ltl2neverclaim-lbtt.test
PASS: ltl2ta.test
PASS: ltl2ta2.test
PASS: ltlprod.test
PASS: bddprod.test
PASS: explprod.test
PASS: explpro2.test
PASS: explpro3.test
PASS: explpro4.test
PASS: tripprod.test
PASS: mixprod.test
PASS: dupexp.test
PASS: degendet.test
PASS: degenid.test
PASS: degenlskip.test
PASS: kv.test
PASS: lbttparse.test
PASS: scc.test
PASS: sccsimpl.test
PASS: dbacomp.test
PASS: obligation.test
PASS: wdba.test
PASS: wdba2.test
PASS: babiak.test
SKIP: ltlcross4.test
SKIP: ltl2dstar.test
SKIP: ltl2dstar2.test
PASS: randtgba.test
PASS: emptchk.test
PASS: emptchke.test
PASS: dfs.test
PASS: ltlcrossce.test
PASS: emptchkr.test
PASS: ltlcounter.test
PASS: basimul.test
SKIP: satmin.test
SKIP: satmin2.test
SKIP: spotlbtt.test
PASS: ltlcross.test
PASS: spotlbtt2.test
PASS: ltlcross2.test
PASS: complementation.test
PASS: randpsl.test
PASS: cycles.test
make[5]: Nothing to be done for `all'.
============================================================================
Testsuite summary for spot 1.2.4
============================================================================
# TOTAL: 63
# PASS:  56
# SKIP:  7
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
Making check in sabatest
/Library/Developer/CommandLineTools/usr/bin/make  sabacomplementtgba defs
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT sabacomplementtgba.o -MD -MP -MF .deps/sabacomplementtgba.Tpo -c -o sabacomplementtgba.o sabacomplementtgba.cc
mv -f .deps/sabacomplementtgba.Tpo .deps/sabacomplementtgba.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o sabacomplementtgba sabacomplementtgba.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/sabacomplementtgba sabacomplementtgba.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
make[3]: `defs' is up to date.
Making check in kripketest
/Library/Developer/CommandLineTools/usr/bin/make  parse_print defs
g++ -DHAVE_CONFIG_H -I. -I../..  -I./.. -I.. -I../../buddy/src -DNDEBUG  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -MT parse_print_test.o -MD -MP -MF .deps/parse_print_test.Tpo -c -o parse_print_test.o parse_print_test.cc
mv -f .deps/parse_print_test.Tpo .deps/parse_print_test.Po
/bin/sh ../../libtool  --tag=CXX   --mode=link g++  -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer   -o parse_print parse_print_test.o ../libspot.la 
libtool: link: g++ -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer -o .libs/parse_print parse_print_test.o -Wl,-bind_at_load  ../.libs/libspot.dylib /Users/taka/Downloads/spot-1.2.4/buddy/src/.libs/libbdd.dylib
make[3]: `defs' is up to date.
/Library/Developer/CommandLineTools/usr/bin/make  check-TESTS
PASS: kripke.test
PASS: bad_parsing.test
make[5]: Nothing to be done for `all'.
============================================================================
Testsuite summary for spot 1.2.4
============================================================================
# TOTAL: 2
# PASS:  2
# SKIP:  0
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
Making check in sanity
/Library/Developer/CommandLineTools/usr/bin/make  check-local
INCDIR='../../src' \
    /bin/sh ./80columns.test 
INCDIR='../../src' \
    /bin/sh ./style.test 
top_srcdir='../..' \
    perl ./readme.test
CXX='g++' \
    CPPFLAGS='-I./.. -I.. -I../../buddy/src -DNDEBUG -DHAVE_CONFIG_H' \
    CXXFLAGS=' -fvisibility=hidden -fvisibility-inlines-hidden -DSPOT_BUILD -g -O3 -ffast-math -fstrict-aliasing -fomit-frame-pointer' \
    INCDIR='../../src' \
    TOPBUILD='../..' \
    /bin/sh ./includes.test 
PASS: bin/common_cout.hh
PASS: bin/common_finput.hh
PASS: bin/common_output.hh
PASS: bin/common_post.hh
PASS: bin/common_r.hh
PASS: bin/common_range.hh
PASS: bin/common_setup.hh
PASS: bin/common_sys.hh
PASS: dstarparse/dstarparse.hh
PASS: dstarparse/parsedecl.hh
PASS: dstarparse/public.hh
PASS: dstarparse/stack.hh
PASS: eltlparse/eltlparse.hh
PASS: eltlparse/parsedecl.hh
PASS: eltlparse/public.hh
PASS: eltlparse/stack.hh
PASS: kripke/fairkripke.hh
PASS: kripke/kripke.hh
PASS: kripke/kripkeexplicit.hh
PASS: kripke/kripkeprint.hh
PASS: kripkeparse/kripkeparse.hh
PASS: kripkeparse/parsedecl.hh
PASS: kripkeparse/public.hh
PASS: kripkeparse/stack.hh
PASS: ltlast/allnodes.hh
PASS: ltlast/atomic_prop.hh
PASS: ltlast/automatop.hh
PASS: ltlast/binop.hh
PASS: ltlast/bunop.hh
PASS: ltlast/constant.hh
PASS: ltlast/formula.hh
PASS: ltlast/formula_tree.hh
PASS: ltlast/multop.hh
PASS: ltlast/nfa.hh
PASS: ltlast/predecl.hh
PASS: ltlast/refformula.hh
PASS: ltlast/unop.hh
PASS: ltlast/visitor.hh
PASS: ltlenv/declenv.hh
PASS: ltlenv/defaultenv.hh
PASS: ltlenv/environment.hh
PASS: ltlparse/ltlfile.hh
PASS: ltlparse/ltlparse.hh
PASS: ltlparse/parsedecl.hh
PASS: ltlparse/public.hh
PASS: ltlparse/stack.hh
PASS: ltlvisit/apcollect.hh
PASS: ltlvisit/clone.hh
PASS: ltlvisit/contain.hh
PASS: ltlvisit/destroy.hh
PASS: ltlvisit/dotty.hh
PASS: ltlvisit/dump.hh
PASS: ltlvisit/lbt.hh
PASS: ltlvisit/length.hh
PASS: ltlvisit/lunabbrev.hh
PASS: ltlvisit/mark.hh
PASS: ltlvisit/nenoform.hh
PASS: ltlvisit/postfix.hh
PASS: ltlvisit/randomltl.hh
PASS: ltlvisit/reduce.hh
PASS: ltlvisit/relabel.hh
PASS: ltlvisit/remove_x.hh
PASS: ltlvisit/simpfg.hh
PASS: ltlvisit/simplify.hh
PASS: ltlvisit/snf.hh
PASS: ltlvisit/tostring.hh
PASS: ltlvisit/tunabbrev.hh
PASS: ltlvisit/wmunabbrev.hh
PASS: misc/bareword.hh
PASS: misc/bddlt.hh
PASS: misc/bddop.hh
PASS: misc/bitvect.hh
PASS: misc/casts.hh
PASS: misc/common.hh
PASS: misc/escape.hh
PASS: misc/fixpool.hh
PASS: misc/formater.hh
PASS: misc/hash.hh
PASS: misc/hashfunc.hh
PASS: misc/intvcmp2.hh
PASS: misc/intvcomp.hh
PASS: misc/location.hh
PASS: misc/ltstr.hh
PASS: misc/memusage.hh
PASS: misc/minato.hh
PASS: misc/mspool.hh
PASS: misc/optionmap.hh
PASS: misc/position.hh
PASS: misc/random.hh
PASS: misc/satsolver.hh
PASS: misc/timer.hh
PASS: misc/tmpfile.hh
PASS: misc/unique_ptr.hh
PASS: misc/version.hh
PASS: neverparse/neverclaimparse.hh
PASS: neverparse/parsedecl.hh
PASS: neverparse/public.hh
PASS: neverparse/stack.hh
PASS: priv/acccompl.hh
PASS: priv/accconv.hh
PASS: priv/bddalloc.hh
PASS: priv/countstates.hh
PASS: priv/freelist.hh
PASS: saba/explicitstateconjunction.hh
PASS: saba/saba.hh
PASS: saba/sabacomplementtgba.hh
PASS: saba/sabastate.hh
PASS: saba/sabasucciter.hh
PASS: sabaalgos/sabadotty.hh
PASS: sabaalgos/sabareachiter.hh
PASS: ta/ta.hh
PASS: ta/taexplicit.hh
PASS: ta/taproduct.hh
PASS: ta/tgta.hh
PASS: ta/tgtaexplicit.hh
PASS: ta/tgtaproduct.hh
PASS: taalgos/dotty.hh
PASS: taalgos/emptinessta.hh
PASS: taalgos/minimize.hh
PASS: taalgos/reachiter.hh
PASS: taalgos/statessetbuilder.hh
PASS: taalgos/stats.hh
PASS: taalgos/tgba2ta.hh
PASS: tgba/bdddict.hh
PASS: tgba/bddprint.hh
PASS: tgba/formula2bdd.hh
PASS: tgba/futurecondcol.hh
PASS: tgba/public.hh
PASS: tgba/sba.hh
PASS: tgba/state.hh
PASS: tgba/statebdd.hh
PASS: tgba/succiter.hh
PASS: tgba/succiterconcrete.hh
PASS: tgba/taatgba.hh
PASS: tgba/tgba.hh
PASS: tgba/tgbabddconcrete.hh
PASS: tgba/tgbabddconcretefactory.hh
PASS: tgba/tgbabddconcreteproduct.hh
PASS: tgba/tgbabddcoredata.hh
PASS: tgba/tgbabddfactory.hh
PASS: tgba/tgbaexplicit.hh
PASS: tgba/tgbakvcomplement.hh
PASS: tgba/tgbamask.hh
PASS: tgba/tgbaproduct.hh
PASS: tgba/tgbaproxy.hh
PASS: tgba/tgbasafracomplement.hh
PASS: tgba/tgbascc.hh
PASS: tgba/tgbasgba.hh
PASS: tgba/tgbatba.hh
PASS: tgba/tgbaunion.hh
PASS: tgba/wdbacomp.hh
PASS: tgbaalgos/bfssteps.hh
PASS: tgbaalgos/complete.hh
PASS: tgbaalgos/compsusp.hh
PASS: tgbaalgos/cutscc.hh
PASS: tgbaalgos/cycles.hh
PASS: tgbaalgos/degen.hh
PASS: tgbaalgos/dotty.hh
PASS: tgbaalgos/dottydec.hh
PASS: tgbaalgos/dtbasat.hh
PASS: tgbaalgos/dtgbacomp.hh
PASS: tgbaalgos/dtgbasat.hh
PASS: tgbaalgos/dupexp.hh
PASS: tgbaalgos/eltl2tgba_lacim.hh
PASS: tgbaalgos/emptiness.hh
PASS: tgbaalgos/emptiness_stats.hh
PASS: tgbaalgos/gtec/ce.hh
PASS: tgbaalgos/gtec/explscc.hh
PASS: tgbaalgos/gtec/gtec.hh
PASS: tgbaalgos/gtec/nsheap.hh
PASS: tgbaalgos/gtec/sccstack.hh
PASS: tgbaalgos/gtec/status.hh
PASS: tgbaalgos/gv04.hh
PASS: tgbaalgos/isdet.hh
PASS: tgbaalgos/isweakscc.hh
PASS: tgbaalgos/lbtt.hh
PASS: tgbaalgos/ltl2taa.hh
PASS: tgbaalgos/ltl2tgba_fm.hh
PASS: tgbaalgos/ltl2tgba_lacim.hh
PASS: tgbaalgos/magic.hh
PASS: tgbaalgos/minimize.hh
PASS: tgbaalgos/ndfs_result.hxx
PASS: tgbaalgos/neverclaim.hh
PASS: tgbaalgos/postproc.hh
PASS: tgbaalgos/powerset.hh
PASS: tgbaalgos/projrun.hh
PASS: tgbaalgos/randomgraph.hh
PASS: tgbaalgos/reachiter.hh
PASS: tgbaalgos/reducerun.hh
PASS: tgbaalgos/reductgba_sim.hh
PASS: tgbaalgos/replayrun.hh
PASS: tgbaalgos/rundotdec.hh
PASS: tgbaalgos/safety.hh
PASS: tgbaalgos/save.hh
PASS: tgbaalgos/scc.hh
PASS: tgbaalgos/sccfilter.hh
PASS: tgbaalgos/se05.hh
PASS: tgbaalgos/simulation.hh
PASS: tgbaalgos/stats.hh
PASS: tgbaalgos/stripacc.hh
PASS: tgbaalgos/tau03.hh
PASS: tgbaalgos/tau03opt.hh
PASS: tgbaalgos/translate.hh
PASS: tgbaalgos/weight.hh
PASS: tgbaalgos/word.hh
PASS: tgbaparse/parsedecl.hh
PASS: tgbaparse/public.hh
PASS: tgbaparse/stack.hh
PASS: tgbaparse/tgbaparse.hh
Making check in wrap
Making check in python
Making check in .
make[3]: Nothing to be done for `check-am'.
Making check in ajax
make[3]: Nothing to be done for `check'.
Making check in tests
/Library/Developer/CommandLineTools/usr/bin/make  run
make[4]: `run' is up to date.
/Library/Developer/CommandLineTools/usr/bin/make  check-TESTS
PASS: alarm.py
PASS: bddnqueen.py
PASS: implies.py
PASS: interdep.py
PASS: ltl2tgba.test
PASS: ltlparse.py
PASS: ltlsimple.py
PASS: minato.py
PASS: optionmap.py
PASS: parsetgba.py
PASS: setxor.py
make[6]: Nothing to be done for `all'.
============================================================================
Testsuite summary for spot 1.2.4
============================================================================
# TOTAL: 11
# PASS:  11
# SKIP:  0
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
make[2]: Nothing to be done for `check-am'.
Making check in ltdl
/Library/Developer/CommandLineTools/usr/bin/make  check-am
make[2]: Nothing to be done for `check-am'.
Making check in iface
Making check in dve2
/Library/Developer/CommandLineTools/usr/bin/make  defs
make[3]: `defs' is up to date.
/Library/Developer/CommandLineTools/usr/bin/make  check-TESTS
SKIP: dve2check.test
SKIP: finite.test
SKIP: kripke.test
make[5]: Nothing to be done for `all'.
============================================================================
Testsuite summary for spot 1.2.4
============================================================================
# TOTAL: 3
# PASS:  0
# SKIP:  3
# XFAIL: 0
# FAIL:  0
# XPASS: 0
# ERROR: 0
============================================================================
make[2]: Nothing to be done for `check-am'.
Making check in doc
Making check in tl
make[2]: Nothing to be done for `check'.
make[2]: Nothing to be done for `check-am'.
make[1]: Nothing to be done for `check-am'.
Genderme:spot-1.2.4 taka$ 


