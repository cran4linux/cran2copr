%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ForeComp
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Size-Power Tradeoff Visualization for Equal Predictive Ability of Two Forecasts

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-astsa 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-astsa 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 

%description
Offers tools for visualizing and analyzing size and power properties of
tests for equal predictive accuracy, including Diebold-Mariano and related
procedures. Provides multiple Diebold-Mariano test implementations based
on fixed-smoothing approaches, including fixed-b methods such as Kiefer
and Vogelsang (2005) <doi:10.1017/S0266466605050565>, and applications to
tests for equal predictive accuracy as in Coroneo and Iacone (2020)
<doi:10.1002/jae.2756>, alongside conventional large-sample
approximations. HAR inference involves nonparametric estimation of the
long-run variance, and a key tuning parameter (the truncation parameter)
trades off size and power. Lazarus, Lewis, and Stock (2021)
<doi:10.3982/ECTA15404> theoretically characterize the size-power frontier
for the Gaussian multivariate location model. 'ForeComp' computes and
visualizes the finite-sample size-power frontier of the Diebold-Mariano
test based on fixed-b asymptotics together with the Bartlett kernel. To
compute finite-sample size and power, it fits a best approximating ARMA
process to the input data and reports how the truncation parameter
performs and how robust testing outcomes are to its choice.

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
