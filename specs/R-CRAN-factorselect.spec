%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  factorselect
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Eigenvalue-Based Estimation of the Number of Factors in Approximate Factor Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Eigenvalue-based estimation of the number of factors in approximate factor
models. Designed to work when either N or T is large, without requiring
both dimensions to grow simultaneously. Implements the eigenvalue ratio
estimator of Ahn and Horenstein (2013) <doi:10.3982/ECTA8968>, the
information criteria of Bai and Ng (2002) <doi:10.1111/1468-0262.00273>,
the tuned penalty of Alessi, Barigozzi and Capasso (2010)
<doi:10.1016/j.spl.2010.08.005>, the auto-covariance ratio estimator of
Lam and Yao (2012) <doi:10.1214/12-AOS970>, and the edge distribution
estimators of Onatski (2009) <doi:10.3982/ECTA6964> and Onatski (2010)
<doi:10.1162/REST_a_00043>.

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
