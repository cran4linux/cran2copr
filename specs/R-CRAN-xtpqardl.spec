%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xtpqardl
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Panel Quantile Autoregressive Distributed Lag Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quantreg 
Requires:         R-stats 
Requires:         R-CRAN-quantreg 

%description
Estimation of Panel Quantile Autoregressive Distributed Lag (PQARDL)
models that combine panel ARDL methodology with quantile regression.
Supports Pooled Mean Group (PMG), Mean Group (MG), and Dynamic Fixed
Effects (DFE) estimators across multiple quantiles. Computes long-run
cointegrating parameters, error correction term speed of adjustment,
half-life of adjustment, and performs Wald tests for parameter equality
across quantiles. Based on the econometric frameworks of Pesaran, Shin,
and Smith (1999) <doi:10.1080/01621459.1999.10474156>, Cho, Kim, and Shin
(2015) <doi:10.1016/j.jeconom.2015.02.030>, and Bildirici and Kayikci
(2022) <doi:10.1016/j.energy.2022.124303>.

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
