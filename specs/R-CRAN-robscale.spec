%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robscale
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Faster Robustness: Accelerated Estimation of Location and Scale

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-RcppParallel >= 5.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-RcppParallel >= 5.0.0
Requires:         R-CRAN-Rcpp >= 1.0.0

%description
Robust estimation ensures statistical reliability in data contaminated by
outliers. Yet, computational bottlenecks in existing 'R' implementations
frequently obstruct both very small sample analysis and large-scale
processing. 'robscale' resolves these inefficiencies by providing
high-performance implementations of logistic M-estimators and the 'Qn' and
'Sn' scale estimators. By leveraging platform-specific Single Instruction,
Multiple Data (SIMD) vectorization and Intel Threading Building Blocks
(TBB) parallelism, the package delivers speedups of 11–39x for small
samples and up to 10x for massive datasets. These performance gains enable
the integration of robust statistics into modern, time-critical
computational workflows. Replaces 'revss' with an 'Rcpp' backend.

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
