%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dryingkineticmodels
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Drying Kinetic Models Comparison and Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-flextable 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-flextable 

%description
Fits multiple thin-layer drying kinetic models to experimental moisture
ratio data, compares model performance using statistical criteria,
performs residual diagnostics, identifies the best-fitting model, and
exports results to Word documents. Twenty models from Ertekin and Firat
(2017) <doi:10.1016/j.jfoodeng.2016.09.030> are fitted using the
Levenberg-Marquardt algorithm described in Marquardt (1963)
<doi:10.1137/0111030>.

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
