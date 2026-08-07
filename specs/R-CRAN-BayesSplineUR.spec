%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesSplineUR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Unit Root Test for AR(1) Model with Trend Approximated by Linear Spline Function

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Performs Bayesian unit root testing for autoregressive time series models
with non-linear trend components approximated by linear spline functions,
as proposed by Kumar et al. (2020) <doi:10.19139/soic-2310-5070-786>. The
package 'BayesSplineUR' computes posterior odds ratios, Bayes factors, and
posterior probabilities for the unit root hypothesis against
trend-stationary alternatives in models with linear spline trends or
maintained polynomial trends as developed by Chaturvedi and Kumar (2005)
<doi:10.1016/j.spl.2005.04.044>. Includes automatic knot selection using
information criteria (AIC/BIC) and theoretical foundations for Bayesian
unit root testing under structural breaks and maintained trends drawing
from Schotman and van Dijk (1991) <doi:10.1016/0304-4076(91)90038-F>,
Phillips and Perron (1988) <doi:10.1093/biomet/75.2.335>, Ouliaris et al.
(1988) <doi:10.1007/978-94-009-2953-1_10>, and Perron (1989)
<doi:10.2307/1913683>.

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
