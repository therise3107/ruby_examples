#!/usr/bin/ruby1.9.1
require "webrick/cgi"

class HelloCGI < WEBrick::CGI
  def do_GET(req, res)
    res["content-type"] = "text/plain"
    res.body = "Hello, world.\n"
  end
end

HelloCGI.new.start
