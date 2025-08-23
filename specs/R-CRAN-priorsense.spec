%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  priorsense
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Prior Diagnostics and Sensitivity Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-grDevices >= 3.6.2
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-ggdist >= 3.3.2
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-checkmate >= 2.3.1
BuildRequires:    R-CRAN-posterior >= 1.6.0
BuildRequires:    R-CRAN-matrixStats >= 1.3.0
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-ggh4x >= 0.2.5
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-grDevices >= 3.6.2
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-ggdist >= 3.3.2
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-checkmate >= 2.3.1
Requires:         R-CRAN-posterior >= 1.6.0
Requires:         R-CRAN-matrixStats >= 1.3.0
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-ggh4x >= 0.2.5
Requires:         R-stats 
Requires:         R-utils 

%description
Provides functions for prior and likelihood sensitivity analysis in
Bayesian models. Currently it implements methods to determine the
sensitivity of the posterior to power-scaling perturbations of the prior
and likelihood.

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
