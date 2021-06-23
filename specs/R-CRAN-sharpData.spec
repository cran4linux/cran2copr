%global __brp_check_rpaths %{nil}
%global packname  sharpData
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Data Sharpening

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-CRAN-KernSmooth 
Requires:         R-stats 
Requires:         R-CRAN-quadprog 

%description
Functions and data sets inspired by data sharpening - data perturbation to
achieve improved performance in nonparametric estimation, as described in
Choi, E., Hall, P. and Rousson, V. (2000). Capabilities for enhanced local
linear regression function and derivative estimation are included, as well
as an asymptotically correct iterated data sharpening estimator for any
degree of local polynomial regression estimation. A cross-validation-based
bandwidth selector is included which, in concert with the iterated
sharpener, will often provide superior performance, according to a median
integrated squared error criterion.  Sample data sets are provided to
illustrate function usage.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
