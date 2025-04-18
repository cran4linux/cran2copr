%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tsdistributions
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Location Scale Standardized Distributions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-TMB >= 1.7.20
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tsmethods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-GeneralizedHyperbolic 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-SkewHyperbolic 
BuildRequires:    R-CRAN-mev 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB >= 1.7.20
Requires:         R-methods 
Requires:         R-CRAN-tsmethods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-GeneralizedHyperbolic 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-SkewHyperbolic 
Requires:         R-CRAN-mev 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-future 
Requires:         R-CRAN-progressr 

%description
Location-Scale based distributions parameterized in terms of mean,
standard deviation, skew and shape parameters and estimation using
automatic differentiation. Distributions include the Normal, Student and
GED as well as their skewed variants ('Fernandez and Steel'), the 'Johnson
SU', and the Generalized Hyperbolic. Also included is the semi-parametric
piece wise distribution ('spd') with Pareto tails and kernel interior.

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
