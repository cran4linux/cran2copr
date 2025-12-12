%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stochtree
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stochastic Tree Ensembles (XBART and BART) for Supervised Learning and Causal Inference

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cpp11 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-R6 
Requires:         R-stats 

%description
Flexible stochastic tree ensemble software. Robust implementations of
Bayesian Additive Regression Trees (BART) Chipman, George, McCulloch
(2010) <doi:10.1214/09-AOAS285> for supervised learning and Bayesian
Causal Forests (BCF) Hahn, Murray, Carvalho (2020) <doi:10.1214/19-BA1195>
for causal inference. Enables model serialization and parallel sampling
and provides a low-level interface for custom stochastic forest samplers.

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
