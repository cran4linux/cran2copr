%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  voigt
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Voigt Distribution

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-invgamma 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-invgamma 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-pracma 

%description
Random generation, density function and parameter estimation for the Voigt
distribution. The main objective of this package is to provide R users
with efficient estimation of Voigt parameters using classic iid data in a
Bayesian framework. The estimating function allows flexible prior
specification, specification of fixed parameters and several options for
MCMC posterior simulation. A basic version of the algorithm is described
in: Cannas M. and Piras, N. (2025) <doi:10.1007/978-3-031-96303-2_53>.

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
