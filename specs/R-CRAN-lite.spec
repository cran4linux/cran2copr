%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lite
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Likelihood-Based Inference for Time Series Extremes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-chandwich 
BuildRequires:    R-CRAN-exdex 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-revdbayes 
BuildRequires:    R-CRAN-rust 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
Requires:         R-CRAN-chandwich 
Requires:         R-CRAN-exdex 
Requires:         R-graphics 
Requires:         R-CRAN-revdbayes 
Requires:         R-CRAN-rust 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 

%description
Performs likelihood-based inference for stationary time series extremes.
The general approach follows Fawcett and Walshaw (2012)
<doi:10.1002/env.2133>.  Marginal extreme value inferences are adjusted
for cluster dependence in the data using the methodology in Chandler and
Bate (2007) <doi:10.1093/biomet/asm015>, producing an adjusted
log-likelihood for the model parameters.  A log-likelihood for the
extremal index is produced using the K-gaps model of Suveges and Davison
(2010) <doi:10.1214/09-AOAS292>. These log-likelihoods are combined to
make inferences about extreme values. Both maximum likelihood and Bayesian
approaches are available.

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
