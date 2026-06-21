%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fda.vi
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Data Analysis using Variational Inference

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-scales 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-scales 

%description
Implements a variational Expectation-Maximization (VEM) algorithm for
smoothing one or multiple functional observations via basis function
selection. The algorithm estimates all model parameters simultaneously and
automatically, while accounting for within-curve correlation. The approach
provides a flexible and computationally efficient framework for smoothing
correlated functional data. The algorithm is described in da Cruz, A. C.,
de Souza, C. P., and Sousa, P. H. (2024). 'Fast Bayesian basis selection
for functional data representation with correlated errors.'
<doi:10.48550/arXiv.2405.20758>.

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
