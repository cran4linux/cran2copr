%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oeli
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          My Utilities for Developing Data Science Software

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-benchmarkme 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hexSticker 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-CRAN-showtext 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sysfonts 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-benchmarkme 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hexSticker 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rprojroot 
Requires:         R-CRAN-showtext 
Requires:         R-stats 
Requires:         R-CRAN-sysfonts 
Requires:         R-CRAN-usethis 
Requires:         R-utils 

%description
Some general helper functions that I and maybe others find useful when
developing data science software. Functionality includes argument
validation, density calculation, sampling, matrix printing, user
interaction, storage helpers and more. The vignettes illustrate use cases.

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
