%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FRB
%global packver   2.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast and Robust Bootstrap

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-corpcor 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-corpcor 

%description
Perform robust inference based on applying Fast and Robust Bootstrap on
robust estimators (Van Aelst and Willems (2013)
<doi:10.18637/jss.v053.i03>). This method constitutes an alternative to
ordinary bootstrap or asymptotic inference. procedures when using robust
estimators such as S-, MM- or GS-estimators. The available methods are
multivariate regression, principal component analysis and one-sample and
two-sample Hotelling tests. It provides both the robust point estimates
and uncertainty measures based on the fast and robust bootstrap.

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
