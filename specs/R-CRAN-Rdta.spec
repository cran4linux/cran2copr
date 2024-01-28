%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rdta
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Transforming Augmentation for Linear Mixed Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack >= 1.4.4
BuildRequires:    R-CRAN-mvtnorm >= 1.0.11
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
Requires:         R-CRAN-MCMCpack >= 1.4.4
Requires:         R-CRAN-mvtnorm >= 1.0.11
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 

%description
We provide a toolbox to fit univariate and multivariate linear mixed
models via data transforming augmentation. Users can also fit these models
via typical data augmentation for a comparison. It returns either maximum
likelihood estimates of unknown model parameters (hyper-parameters) via an
EM algorithm or posterior samples of those parameters via MCMC. Also see
Tak et al. (2019) <doi:10.1080/10618600.2019.1704295>.

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
