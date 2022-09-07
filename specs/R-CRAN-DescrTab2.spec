%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DescrTab2
%global packver   2.1.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.16
Release:          1%{?dist}%{?buildtag}
Summary:          Publication Quality Descriptive Statistics Tables

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-flextable >= 0.6.6
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-exact2x2 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-flextable >= 0.6.6
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-exact2x2 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-Hmisc 

%description
Provides functions to create descriptive statistics tables for continuous
and categorical variables. By default, summary statistics such as mean,
standard deviation, quantiles, minimum and maximum for continuous
variables and relative and absolute frequencies for categorical variables
are calculated. 'DescrTab2' features a sophisticated algorithm to choose
appropriate test statistics for your data and provides p-values. On top of
this, confidence intervals for group differences of appropriated summary
measures are automatically produces for two-group comparison. Tables
generated by 'DescrTab2' can be integrated in a variety of document
formats, including .html, .tex and .docx documents. 'DescrTab2' also
allows printing tables to console and saving table objects for later use.

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
