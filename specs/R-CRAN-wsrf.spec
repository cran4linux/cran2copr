%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wsrf
%global packver   1.7.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.31
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted Subspace Random Forest for Classification

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.2
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.10.2
Requires:         R-parallel 
Requires:         R-stats 

%description
A parallel implementation of Weighted Subspace Random Forest.  The
Weighted Subspace Random Forest algorithm was proposed in the
International Journal of Data Warehousing and Mining by Baoxun Xu, Joshua
Zhexue Huang, Graham Williams, Qiang Wang, and Yunming Ye (2012)
<DOI:10.4018/jdwm.2012040103>.  The algorithm can classify very
high-dimensional data with random forests built using small subspaces.  A
novel variable weighting method is used for variable subspace selection in
place of the traditional random variable sampling.This new approach is
particularly useful in building models from high-dimensional data.

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
