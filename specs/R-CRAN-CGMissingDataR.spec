%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CGMissingDataR
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Missingness Benchmark for Continuous Glucose Monitoring Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-ranger 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-ranger 

%description
Evaluates predictive performance under feature-level missingness in
repeated-measures continuous glucose monitoring-like data. The benchmark
injects missing values at user-specified rates, imputes incomplete feature
matrices using an iterative chained-equations approach inspired by
multivariate imputation by chained equations (MICE; Azur et al. (2011)
<doi:10.1002/mpr.329>), fits Random Forest regression models (Breiman
(2001) <doi:10.1023/A:1010933404324>) and k-nearest-neighbor regression
models (Zhang (2016) <doi:10.21037/atm.2016.03.37>), and reports mean
absolute percentage error and R-squared across missingness rates.

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
