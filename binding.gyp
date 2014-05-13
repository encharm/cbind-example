{
  "targets": [
    {
      "target_name": "cbind_example",
      "sources": [
        "src/addon.cc"
      ],
      "include_dirs"  : [
          "<!(node -e \"require('nan')\" 2> /dev/null)",
          "<!(node -e \"require('cbind')('example.nid')\" 2> /dev/null)"
      ],
      "cflags": ["-g", "-std=c++11"],
			"cflags_cc!": [ '-fno-exceptions' ]
    }
  ]
}