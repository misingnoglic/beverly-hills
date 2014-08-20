for /d %A in ("I:\EmerMgmt\*") DO (
  Echo "%A" >>dir.txt
  Echo "" >> dir.txt
  dir "%A" /B /O:GN >> dir.txt
  Echo "" >> dir.txt
  )
