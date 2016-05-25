#!/usr/bin/env ruby

TEXFILE=ENV['MAIN_FILE']
EXECUTE_PDFLATEX="pdflatex -shell-escape -interaction=nonstopmode #{TEXFILE}.tex"
EXECUTE_BIBTEX="bibtex #{TEXFILE}.aux"

guard :shell do
  watch(/(.*).tex/) do |m|
    system(EXECUTE_PDFLATEX) and
      system(EXECUTE_BIBTEX) and
      system(EXECUTE_PDFLATEX) and
      system(EXECUTE_PDFLATEX) and
      n("Last change: #{m[0]}", 'Build success', :success) or
    n("Last change: #{m[0]}", 'Build failed', :failed)
  end
end
