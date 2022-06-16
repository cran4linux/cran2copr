%global __brp_check_rpaths %{nil}
%global packname  huxtable
%global packver   5.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Create and Style Tables for LaTeX, HTML and Other Formats

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-fansi 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-fansi 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tidyselect 
Requires:         R-utils 
Requires:         R-CRAN-xml2 

%description
Creates styled tables for data presentation. Export to HTML, LaTeX, RTF,
'Word', 'Excel', and 'PowerPoint'. Simple, modern interface to manipulate
borders, size, position, captions, colours, text styles and number
formatting. Table cells can span multiple rows and/or columns. Includes a
'huxreg' function for creation of regression tables, and 'quick_*'
one-liners to print data to a new document.

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
