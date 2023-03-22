%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dcm2
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Calculating the M2 Model Fit Statistic for Diagnostic Classification Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-methods >= 4.1.0
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-glue >= 1.4.2
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.1.4
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.800.1.0
BuildRequires:    R-CRAN-dplyr >= 0.8.4
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-modelr >= 0.1.8
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-methods >= 4.1.0
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-glue >= 1.4.2
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.1.4
Requires:         R-CRAN-dplyr >= 0.8.4
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-modelr >= 0.1.8
Requires:         R-CRAN-Rcpp 

%description
A collection of functions for calculating the M2 model fit statistic for
diagnostic classification models as described by Liu et al. (2016)
<DOI:10.3102/1076998615621293>. These functions provide multiple sources
of information for model fit according to the M2 statistic, including the
M2 statistic, the *p* value for that M2 statistic, and the Root Mean
Square Error of Approximation based on the M2 statistic.

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
