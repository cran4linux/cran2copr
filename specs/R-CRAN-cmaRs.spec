%global __brp_check_rpaths %{nil}
%global packname  cmaRs
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Implementation of the Conic Multivariate Adaptive Regression Splines in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rmosek 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-AUC 
BuildRequires:    R-CRAN-Ryacas0 
Requires:         R-CRAN-earth 
Requires:         R-graphics 
Requires:         R-CRAN-Rmosek 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-AUC 
Requires:         R-CRAN-Ryacas0 

%description
An implementation of 'Conic Multivariate Adaptive Regression Splines
(CMARS)' in R. See Weber et al. (2011) CMARS: a new contribution to
nonparametric regression with multivariate adaptive regression splines
supported by continuous optimization, <DOI:10.1080/17415977.2011.624770>.
It constructs models by using the terms obtained from the forward step of
MARS and then estimates parameters by using 'Tikhonov' regularization and
conic quadratic optimization. It is possible to construct models for
prediction and binary classification. It provides performance measures for
the model developed. The package needs the optimisation software 'MOSEK'
<https://www.mosek.com/> to construct the models. Please follow the
instructions in 'Rmosek' for the installation.

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
