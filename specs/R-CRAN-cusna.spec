%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cusna
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Native GPU-Accelerated Simulation and Estimation of Network Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-stats 
Requires:         R-utils 

%description
A self-contained native engine (a C interface over 'CUDA' kernels and C++
host logic) for stochastic actor-oriented models (the model family of
'RSiena'), exponential random graph models (cross-sectional, temporal, and
separable temporal), and models for binary actor attributes, callable from
R without a Python runtime. Modelled on the 'torch' package: the CRAN
build is CPU-only from source; the GPU path is compiled from source when a
'CUDA' toolkit is detected at configure time. The data preparation, host
statistics ('RSiena' Appendix B conventions), and moment targets are
validated bit-for-bit against the reference implementation and reproduce
'RSiena' targets on public datasets to machine precision; the estimators
match 'RSiena', 'ergm', 'btergm', and 'tergm' on public benchmark models.

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
