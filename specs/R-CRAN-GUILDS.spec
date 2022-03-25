%global __brp_check_rpaths %{nil}
%global packname  GUILDS
%global packver   1.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Implementation of Sampling Formulas for the Unified Neutral Model of Biodiversity and Biogeography, with or without Guild Structure

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-nloptr 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-nloptr 

%description
A collection of sampling formulas for the unified neutral model of
biogeography and biodiversity. Alongside the sampling formulas, it
includes methods to perform maximum likelihood optimization of the
sampling formulas, methods to generate data given the neutral model, and
methods to estimate the expected species abundance distribution. Sampling
formulas included in the GUILDS package are the Etienne Sampling Formula
(Etienne 2005), the guild sampling formula, where guilds are assumed to
differ in dispersal ability (Janzen et al. 2015), and the guilds sampling
formula conditioned on guild size (Janzen et al. 2015).

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
