#!/usr/bin/env ruby

TEXFILE=ENV['MAIN_FILE']

guard :shell do
  watch(/(.*).tex/) do |m|
    system("pdflatex -interaction=nonstopmode #{TEXFILE}.tex") and
      system("bibtex #{TEXFILE}.aux") and
      system("pdflatex -interaction=nonstopmode #{TEXFILE}.tex") and
      system("pdflatex -interaction=nonstopmode #{TEXFILE}.tex") and
      n("Last change: #{m[0]}", 'Build success', :success) or
    n("Last change: #{m[0]}", 'Build failed', :failed)
  end
end
