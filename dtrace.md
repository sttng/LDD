sudo dtrace -n 'syscall::open*:entry { printf("%s %s",execname,copyinstr(arg0));}'
