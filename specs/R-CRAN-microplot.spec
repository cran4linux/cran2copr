%global __brp_check_rpaths %{nil}
%global packname  microplot
%global packver   1.0-45
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.45
Release:          1%{?dist}%{?buildtag}
Summary:          Microplots (Sparklines) in 'LaTeX', 'Word', 'HTML', 'Excel'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.1.1
BuildRequires:    R-CRAN-flextable >= 0.5.11
BuildRequires:    R-CRAN-HH 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-cowplot 
Requires:         R-CRAN-Hmisc >= 4.1.1
Requires:         R-CRAN-flextable >= 0.5.11
Requires:         R-CRAN-HH 
Requires:         R-CRAN-lattice 
Requires:         R-grid 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-cowplot 

%description
The microplot function writes a set of R graphics files to be used as
microplots (sparklines) in tables in either 'LaTeX', 'HTML', 'Word', or
'Excel' files.  For 'LaTeX', we provide methods for the Hmisc::latex()
generic function to construct 'latex' tabular environments which include
the graphs.  These can be used directly with the operating system
'pdflatex' or 'latex' command, or by using one of 'Sweave', 'knitr',
'rmarkdown', or 'Emacs org-mode' as an intermediary.  For 'MS Word', the
msWord() function uses the 'flextable' package to construct 'Word' tables
which include the graphs.  There are several distinct approaches for
constructing HTML files.  The simplest is to use the msWord() function
with argument filetype="html".  Alternatively, use either 'Emacs org-mode'
or the htmlTable::htmlTable() function to construct an 'HTML' file
containing tables which include the graphs.  See the documentation for our
as.htmlimg() function.  For 'Excel' use on 'Windows', the file
examples/irisExcel.xls includes 'VBA' code which brings the individual
panels into individual cells in the spreadsheet. Examples in the examples
and demo subdirectories are shown with 'lattice' graphics, 'ggplot2'
graphics, and 'base' graphics. Examples for 'LaTeX' include 'Sweave' (both
'LaTeX'-style and 'Noweb'-style), 'knitr', 'emacs org-mode', and
'rmarkdown' input files and their 'pdf' output files.  Examples for 'HTML'
include 'org-mode' and 'Rmd' input files and their webarchive 'HTML'
output files.  In addition, the as.orgtable() function can display a
data.frame in an 'org-mode' document.  The examples for 'MS Word' (with
either filetype="docx" or filetype="html") work with all operating
systems.  The package does not require the installation of 'LaTeX' or 'MS
Word' to be able to write '.tex' or '.docx' files.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
