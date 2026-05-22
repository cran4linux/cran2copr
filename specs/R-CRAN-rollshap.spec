%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rollshap
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Rolling Shapley Values

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-roll >= 1.1.7
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 

%description
Analytical computation of rolling and expanding Shapley values for
time-series data. The 'rollshap' package decomposes the coefficient of
determination (R-squared) of a linear regression into nonnegative
contributions from each explanatory variable using the Shapley value from
cooperative game theory (Shapley, 1953, <doi:10.1515/9781400881970-018>).
For each window, the exact Shapley value is computed by fitting all
subsets of the explanatory variables and averaging the marginal
contribution to R-squared across all orderings, which returns an
order-invariant attribution that sums to the full-model R-squared. Use
cases include variable importance, factor attribution, and feature
selection in time-series regression. The package supports rolling and
expanding windows, weights, and handling of missing values via 'min_obs',
'complete_obs', and 'na_restore' arguments. The implementation uses the
online and offline algorithms from the 'roll' package to compute rolling
and expanding cross-products efficiently with parallelism across columns
and windows provided by 'RcppParallel'.

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
