%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayclumpr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Analysis of Clumped Isotope Datasets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-deming 
BuildRequires:    R-CRAN-IsoplotR 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rstantools
Requires:         R-parallel 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-deming 
Requires:         R-CRAN-IsoplotR 
Requires:         R-CRAN-rstan 
Requires:         R-stats 
Requires:         R-CRAN-rstantools

%description
Simulating synthetic clumped isotope dataset, fitting linear regression
models under Bayesian and non-Bayesian frameworks, and generating
temperature reconstructions for the same two approaches. Please note that
models implemented in this package are described in Roman-Palacios et al.
(2021) <doi:10.1002/essoar.10507995.1>.

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
