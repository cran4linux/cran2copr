%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sparsenet
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Sparse Linear Regression Models via Nonconvex Optimization

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix >= 1.0.6
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-methods 
Requires:         R-CRAN-Matrix >= 1.0.6
Requires:         R-CRAN-shape 
Requires:         R-methods 

%description
Efficient procedure for fitting regularization paths between L1 and L0,
using the MC+ penalty of Zhang, C.H. (2010)<doi:10.1214/09-AOS729>.
Implements the methodology described in Mazumder, Friedman and Hastie
(2011) <DOI: 10.1198/jasa.2011.tm09738>. Sparsenet computes the
regularization surface over both the family parameter and the tuning
parameter by coordinate descent.

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
