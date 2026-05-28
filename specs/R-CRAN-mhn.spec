%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mhn
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Modified Half-Normal Distribution

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-BH >= 1.78.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-stats 

%description
Provides density, distribution, quantile, and random generation functions
for the Modified Half-Normal (MHN) distribution, along with moments, mode,
and the Fox-Wright Psi function used as the normalizing constant. The MHN
distribution arises as a conditional posterior in Bayesian MCMC and
generalizes the half-normal, truncated normal, and square-root gamma
distributions. Implements efficient sampling via the Sun, Kong & Pal
(2023) <doi:10.1080/03610926.2021.1934700> algorithms and the Gao & Wang
(2025) <doi:10.1080/03610918.2025.2524551> RTDR method.

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
