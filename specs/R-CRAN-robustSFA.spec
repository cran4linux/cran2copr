%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robustSFA
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Estimation of Stochastic Frontier Models with MDPDE

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-frontier 
BuildRequires:    R-CRAN-BH 
Requires:         R-stats 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-frontier 

%description
This provides a robust estimator for stochastic frontier models, employing
the Minimum Density Power Divergence Estimator (MDPDE) for enhanced
robustness against outliers. Additionally, it includes a function to
recommend the optimal tuning parameter, alpha, which controls the
robustness of the MDPDE. The methods implemented in this package are based
on Song et al. (2017) <doi:10.1016/j.csda.2016.08.005>.

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
