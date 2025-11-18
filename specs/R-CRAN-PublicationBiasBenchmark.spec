%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PublicationBiasBenchmark
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Benchmark for Publication Bias Correction Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-osfr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-clubSandwich 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-puniform 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-osfr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-pwr 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-clubSandwich 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-puniform 
Requires:         R-CRAN-Rdpack 

%description
Implements a unified interface for benchmarking meta-analytic publication
bias correction methods through simulation studies (see Bartoš et al.,
2025, <doi:10.48550/arXiv.2510.19489>). It provides 1) predefined
data-generating mechanisms from the literature, 2) functions for running
meta-analytic methods on simulated data, 3) pre-simulated datasets and
pre-computed results for reproducible benchmarks, 4) tools for visualizing
and comparing method performance.

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
