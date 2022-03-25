%global __brp_check_rpaths %{nil}
%global packname  survivalmodels
%global packver   0.1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.13
Release:          1%{?dist}%{?buildtag}
Summary:          Models for Survival Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-Rcpp >= 1.0.5

%description
Implementations of classical and machine learning models for survival
analysis, including deep neural networks via 'keras' and 'tensorflow'.
Each model includes a separated fit and predict interface with consistent
prediction types for predicting risk, survival probabilities, or survival
distributions with 'distr6' <https://CRAN.R-project.org/package=distr6>.
Models are either implemented from 'Python' via 'reticulate'
<https://CRAN.R-project.org/package=reticulate>, from code in GitHub
packages, or novel implementations using 'Rcpp'
<https://CRAN.R-project.org/package=Rcpp>. Novel machine learning survival
models wil be included in the package in near-future updates. Neural
networks are implemented from the 'Python' package 'pycox'
<https://github.com/havakv/pycox> and are detailed by Kvamme et al. (2019)
<https://jmlr.org/papers/v20/18-424.html>. The 'Akritas' estimator is
defined in Akritas (1994) <doi:10.1214/aos/1176325630>. 'DNNSurv' is
defined in Zhao and Feng (2020) <arXiv:1908.02337>.

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
