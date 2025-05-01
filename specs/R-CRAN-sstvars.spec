%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sstvars
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Toolkit for Reduced Form and Structural Smooth Transition Vector Autoregressive Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-parallel >= 4.0.0
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-graphics >= 4.0.0
BuildRequires:    R-utils >= 4.0.0
BuildRequires:    R-CRAN-pbapply >= 1.7.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.12.0.0.0
Requires:         R-parallel >= 4.0.0
Requires:         R-stats >= 4.0.0
Requires:         R-graphics >= 4.0.0
Requires:         R-utils >= 4.0.0
Requires:         R-CRAN-pbapply >= 1.7.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-RcppArmadillo >= 0.12.0.0.0

%description
Penalized and non-penalized maximum likelihood estimation of smooth
transition vector autoregressive models with various types of transition
weight functions, conditional distributions, and identification methods.
Constrained estimation with various types of constraints is available.
Residual based model diagnostics, forecasting, simulations, counterfactual
analysis, and computation of impulse response functions, generalized
impulse response functions, generalized forecast error variance
decompositions, as well as historical decompositions. See Heather
Anderson, Farshid Vahid (1998) <doi:10.1016/S0304-4076(97)00076-6>, Helmut
Lütkepohl, Aleksei Netšunajev (2017) <doi:10.1016/j.jedc.2017.09.001>,
Markku Lanne, Savi Virolainen (2025) <doi:10.48550/arXiv.2403.14216>, Savi
Virolainen (2025) <doi:10.48550/arXiv.2404.19707>.

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
