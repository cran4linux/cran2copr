%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wrappedtools
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          1%{?dist}%{?buildtag}
Summary:          Useful Wrappers Around Commonly Used Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-nortest 
Requires:         R-stats 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-coin 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-nortest 

%description
The main functionalities of 'wrappedtools' are: adding backticks to
variable names; rounding to desired precision with special case for
p-values; selecting columns based on pattern and storing their position,
name, and backticked name; computing and formatting of descriptive
statistics (e.g. mean±SD), comparing groups and creating publication-ready
tables with descriptive statistics and p-values; creating specialized
plots for correlation matrices. Functions were mainly written for my own
daily work or teaching, but may be of use to others as well.

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
