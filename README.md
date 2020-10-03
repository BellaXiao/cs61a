# cs61a
2018fall

First round basi completion on 2020/10/3.
Could go back to review those project and concepts.

Learning Memo During the first-round learning process:
    CS 61A(https://inst.eecs.berkeley.edu/~cs61a/fa18/)
    project需要回看，学结构
    * lab04_extra 回看
    * maps project 回看并且自己下数据做一个纽约的
    * lab06 回看结构
    * ants project problem(extra Credit) and the whole structure
    *lab07: Q8: remember yield is diff from return; use of yield from
    * lab07 extra: Q11 has_cycle_constant(linked list, use fast and slow pointers)
    * lab08 Q4 not quite understand
    * lab08 Q6 nonlocal(remember to define nonlocal variable in the most inner function)
    *lab10 mini interpreter 自己复制了一次，框架需要复习
    * project scheme problem20/21
    (scheme project advance version可以后续尝试，整体框架没有浏览)
    * video 11/26 Natural Language
    * lab13 scheme extra part not finish

    order: 
    L12 (done)-> map project (done)-> video9/24(done) -> lab05 (done)->video9/26（done)->HW05(done)->video9/28(done) -> video 10/1 (done)->video 10/3 (done)->lab06 (done)->ants proj(done) -> video10/5(done)->  hw06(done)   -> video10/8(done)  ->  video10/10(done)   ->    lab07(done)   -> video 10/12 （done）  > video 10/15 (done)  -> lab08(done) -> video 10/19（skip guest） -> video10/22(done) ->lab09(done) -> HW07(done) ->video 10/24(done) -> HW08 (done)->video 10/26(done) -> video 10/29 (done)-> lab10(done) -> lab10:other parts review （done）->scheme proj （done）-> video 10/31 （done） -> video 11/2 （done）-> HW 09(done)-> lab11(done)->video 11/5(done) -> HW10(done)->video11/7(done)->video 11/9(done) -> lab12(done) -> video 11/14(done) -> video 11/19(done) ->HW11(done) -> video 11/26(done) ->video 11/28(done) -> lab13(done)

    git:
    git init (at certain path) (cd to cs61a)
    git clone url(clone the project in github to local)
    git status
    git add .
    git commit -m “string”
    git push origin master
    ——————————————
    terminal command:
    cd ~/   ./    ../
    ls  (list all files under the path)
    unzip
    mv file1 file2
    python3
    python3 path/file.py
    python3 -i path/file.py (ctrl D exit)
    显示doctest具体结果
    python3 -m doctest ~/Desktop/temp.py -v
    source activate envTF113
    (activate a certain environment)



    ——————————————
    python expressions:
    list comprehension with if else
    [f(x) if condition else g(x) for x in sequence]

    >>> sum([[1],[2],[3,4]],[])
    [1,2,3,4]    #[] is the start value

    mutable functions
    1) nonlocal variable
    python would pre-computes which frame with which variable before executing the function.
    2) use mutable objects like lists

    zip()  && zip(*) to unzip
    zip return len with the minimum len of the two component

    ————————————————
    finance usage

    datetime.timedelta objects only have days and seconds attributes, can use them to get hour and minutes dat.

    pd.isna()  && pd.notna()

    按日期求和，并以DataFrame显示每天的最后五个数据
    pd.DataFrame(bars.groupby( [ bars.index.date ]).tail(5))
    分组后求组内百分比（最后一项为累计和）
    bars.groupby( [ bars.index.date ] )[ 'accum_volume' ].transform( lambda x: x / x.iloc[ -1 ] )








