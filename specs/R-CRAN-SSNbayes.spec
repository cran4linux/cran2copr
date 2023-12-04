%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SSNbayes
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Spatio-Temporal Analysis in Stream Networks

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-SSN2 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-sf 
Requires:         R-methods 
Requires:         R-CRAN-SSN2 
Requires:         R-CRAN-rstantools

%description
Fits Bayesian spatio-temporal models and makes predictions on stream
networks using the approach by Santos-Fernandez, Edgar, et al.
(2022)."Bayesian spatio-temporal models for stream networks".
<arXiv:2103.03538>. In these models, spatial dependence is captured using
stream distance and flow connectivity, while temporal autocorrelation is
modelled using vector autoregression methods.

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
