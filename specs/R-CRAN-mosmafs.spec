%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mosmafs
%global packver   0.1.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Objective Simultaneous Model and Feature Selection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ecr >= 2.1.0
BuildRequires:    R-CRAN-checkmate >= 1.9.0
BuildRequires:    R-CRAN-mlrCPO >= 0.3.4
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-ParamHelpers 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-smoof 
BuildRequires:    R-CRAN-mlr 
BuildRequires:    R-CRAN-parallelMap 
Requires:         R-CRAN-ecr >= 2.1.0
Requires:         R-CRAN-checkmate >= 1.9.0
Requires:         R-CRAN-mlrCPO >= 0.3.4
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-ParamHelpers 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-smoof 
Requires:         R-CRAN-mlr 
Requires:         R-CRAN-parallelMap 

%description
Performs simultaneous hyperparameter tuning and feature selection through
both single-objective and multi-objective optimization as described in
Binder, Moosbauer et al. (2019) <arXiv:1912.12912>. Uses the 'ecr'-package
as basis but adds mixed integer evolutionary strategies and multi-fidelity
functionality as well as operators specific for the problem of feature
selection.

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
