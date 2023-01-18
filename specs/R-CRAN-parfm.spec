%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  parfm
%global packver   2.7.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.7
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Frailty Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-sn 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-msm 
Requires:         R-graphics 
Requires:         R-CRAN-sn 

%description
Fits Parametric Frailty Models by maximum marginal likelihood. Possible
baseline hazards: exponential, Weibull, inverse Weibull (Fréchet),
Gompertz, lognormal, log-skew-normal, and loglogistic. Possible Frailty
distributions: gamma, positive stable, inverse Gaussian and lognormal.

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
