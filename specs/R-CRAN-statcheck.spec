%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  statcheck
%global packver   1.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extract Statistics from Articles and Recompute P-Values

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tcltk 
BuildRequires:    R-utils 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-tcltk 
Requires:         R-utils 

%description
A "spellchecker" for statistics. It checks whether your p-values match
their accompanying test statistic and degrees of freedom. statcheck
searches for null-hypothesis significance tests (NHST) in APA style (e.g.,
t(28) = 2.2, p < .05), using pattern-matching ("regular expressions"). It
recalculates the p-value using the reported test statistic and degrees of
freedom. If the reported and computed p-values don't match, 'statcheck'
will flag the result as an error. If the reported p-value is statistically
significant and the computed one is not, or vice versa, the result will be
flagged as a decision error. You can use 'statcheck' directly on a string
of text, but you can also scan a PDF or HTML file, or even a folder of PDF
and/or HTML files. PDF files are converted to text using the R package
'pdftools', so no additional software installation is necessary. You can
find more information on what 'statcheck' can and cannot do and a
point-and-click web interface to scan PDF or HTML or DOCX articles on
<https://statcheck.io>.

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
