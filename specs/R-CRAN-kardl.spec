%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kardl
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Make Symmetric and Asymmetric ARDL Estimations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-nlWaldTest 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-nlWaldTest 
Requires:         R-CRAN-car 
Requires:         R-utils 

%description
Implements estimation procedures for Autoregressive Distributed Lag (ARDL)
and Nonlinear ARDL (NARDL) models, which allow researchers to investigate
both short- and long-run relationships in time series data under mixed
orders of integration. The package supports simultaneous modeling of
symmetric and asymmetric regressors, flexible treatment of short-run and
long-run asymmetries, and automated equation handling. It includes several
cointegration testing approaches such as the Pesaran-Shin-Smith F and t
bounds tests, the Banerjee error correction test, and the restricted ECM
test, together with diagnostic tools including Wald tests for asymmetry,
ARCH tests, and stability procedures (CUSUM and CUSUMQ). Methodological
foundations are provided in Pesaran, Shin, and Smith (2001)
<doi:10.1016/S0304-4076(01)00049-5> and Shin, Yu, and Greenwood-Nimmo
(2014, ISBN:9780123855079).

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
