def get_text_block(fname):
  # this is how to read a block of text:
  path = "..//pdac2021_res_est_course_link2//text_blocks"
  f = open(path + "//" + fname, "r")
  # and then write it to the app
  return f.read();
  
