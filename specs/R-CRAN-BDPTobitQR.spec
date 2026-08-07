%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BDPTobitQR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Double-Penalty Tobit Quantile Regression for Longitudinal Interval-Censored Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Implements Bayesian Double-Penalty Tobit Quantile Regression methods for
longitudinal interval-censored data as proposed by Zhao et al. (2024)
<doi:10.3390/math12121782>. Supports Bayesian Tobit quantile regression
with double adaptive Lasso penalty ('PDAL-BTQR'), double Lasso penalty
('PDL-BTQR'), and unpenalized mixed-effects ('P-BTQR'). Handles left,
right, interval, and bilateral censoring schemes in longitudinal and
clustered structures. Includes Gibbs sampling algorithms, parameter
estimation, standard error computation, posterior credible intervals,
forecast predictions, DIC, LPML, and diagnostic plotting. References:
Tobin (1958) <doi:10.2307/1907382>; Koenker and Bassett (1978)
<doi:10.2307/1913643>; Zou (2006) <doi:10.1198/016214506000000735>;
Alhamzawi and Yu (2012) <doi:10.1016/j.csda.2011.11.018>; Zhao et al.
(2024) <doi:10.3390/math12121782>.

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
