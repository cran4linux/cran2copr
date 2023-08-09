%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  defm
%global packver   0.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Simulation of Multi-Binary Response Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-stats4 
Requires:         R-CRAN-Rcpp 

%description
Multi-binary response models are a class of models that allow for the
estimation of multiple binary outcomes simultaneously. This package
provides functions to estimate and simulate these models using the
Discrete Exponential-Family Models [DEFM] framework. In it, we implement
the models described in Vega Yon, Valente, and Pugh (2023)
<doi:10.48550/arXiv.2211.00627>. DEFMs include Exponential-Family Random
Graph Models [ERGMs], which characterize graphs using sufficient
statistics, which is also the core of DEFMs. Using sufficient statistics,
we can describe the data through meaningful motifs, for example,
transitions between different states, joint distribution of the outcomes,
etc.

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
