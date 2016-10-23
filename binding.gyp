{
  "targets": [
    {
      "includes": [
        "auto.gypi"
      ],
      "sources": [
        "src/run.cpp"
      ],
      "link_settings":{
        "ldflags": [
          "-L<(module_root_dir)/src/target/release -lbinarytrees",
          "-Wl,-rpath=<(module_root_dir)/src/target/release"
        ]
      }
    }
  ],
  "includes": [
    "auto-top.gypi"
  ]
}
