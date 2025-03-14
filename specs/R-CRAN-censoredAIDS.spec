%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  censoredAIDS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Censored AI/QUAI Demand System via Maximum Likelihood Estimation (MLE)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 

%description
Tools for estimating censored Almost Ideal (AI) and Quadratic Almost Ideal
(QUAI) demand systems using Maximum Likelihood Estimation (MLE). It
includes functions for calculating demand share equations and the
truncated log-likelihood function for a system of equations, incorporating
demographic variables. The package is designed to handle censored data,
where some observations may be zero due to non-purchase of certain goods.
It is particularly useful for applied researchers analyzing household
consumption data.

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
