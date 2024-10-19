%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mrgsolve
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate from ODE-Based Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.2
Requires:         R-core >= 3.6.2
BuildRequires:    R-CRAN-tibble >= 3.1.6
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-BH >= 1.75.0.0
BuildRequires:    R-CRAN-tidyselect >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.8
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-rlang >= 1.0.1
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10.7.3.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-tibble >= 3.1.6
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-tidyselect >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.8
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-rlang >= 1.0.1
Requires:         R-methods 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-glue 

%description
Fast simulation from ordinary differential equation (ODE) based models
typically employed in quantitative pharmacology and systems biology.

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
