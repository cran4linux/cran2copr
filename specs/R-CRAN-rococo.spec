%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rococo
%global packver   1.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Rank Correlation Coefficient and Test

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-methods 
Requires:         R-stats 

%description
Provides the robust gamma rank correlation coefficient as introduced by
Bodenhofer, Krone, and Klawonn (2013) <DOI:10.1016/j.ins.2012.11.026>
along with a permutation-based rank correlation test. The rank correlation
coefficient and the test are explicitly designed for dealing with noisy
numerical data.

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
