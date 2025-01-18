%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  georob
%global packver   0.3-22
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.22
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Geostatistical Analysis of Spatial Data

License:          GPL (>= 2) | LGPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildArch:        noarch
BuildRequires:    R-CRAN-robustbase >= 0.90.2
BuildRequires:    R-CRAN-sp >= 0.9.60
BuildRequires:    R-CRAN-constrainedKriging >= 0.2.7
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-robustbase >= 0.90.2
Requires:         R-CRAN-sp >= 0.9.60
Requires:         R-CRAN-constrainedKriging >= 0.2.7
Requires:         R-CRAN-abind 
Requires:         R-CRAN-fields 
Requires:         R-graphics 
Requires:         R-CRAN-lmtest 
Requires:         R-methods 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-nleqslv 
Requires:         R-parallel 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-snowfall 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides functions for efficiently fitting linear models with spatially
correlated errors by robust (Kuensch et al. (2011)
<doi:10.3929/ethz-a-009900710>) and Gaussian (Harville (1977)
<doi:10.1080/01621459.1977.10480998>) (Restricted) Maximum Likelihood and
for computing robust and customary point and block external-drift Kriging
predictions (Cressie (1993) <doi:10.1002/9781119115151>), along with
utility functions for variogram modelling in ad hoc geostatistical
analyses, model building, model evaluation by cross-validation,
(conditional) simulation of Gaussian processes (Davies and Bryant (2013)
<doi:10.18637/jss.v055.i09>), unbiased back-transformation of Kriging
predictions of log-transformed data (Cressie (2006)
<doi:10.1007/s11004-005-9022-8>).

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
