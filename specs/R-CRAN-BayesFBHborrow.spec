%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesFBHborrow
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Dynamic Borrowing with Flexible Baseline Hazard Function

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-invgamma 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-invgamma 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 

%description
Allows Bayesian borrowing from a historical dataset for time-to- event
data. A flexible baseline hazard function is achieved via a piecewise
exponential likelihood with time varying split points and smoothing prior
on the historic baseline hazards.

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
