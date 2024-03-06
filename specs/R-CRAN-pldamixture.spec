%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pldamixture
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Post-Linkage Data Analysis Based on Mixture Modelling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
Requires:         R-stats 
Requires:         R-CRAN-survival 

%description
Perform inference in the secondary analysis setting with linked data
potentially containing mismatch errors. Only the linked data file may be
accessible and information about the record linkage process may be limited
or unavailable. Implements the 'General Framework for Regression with
Mismatched Data' developed by Slawski et al. (2023) <arXiv:2306.00909>.
The framework uses a mixture model for pairs of linked records whose two
components reflect distributions conditional on match status, i.e.,
correct match or mismatch. Inference is based on composite likelihood and
the Expectation-Maximization (EM) algorithm. The package currently
supports Cox Proportional Hazards Regression (right-censored data only)
and Generalized Linear Regression Models (Gaussian, Gamma, Poisson, and
Logistic (binary models only)). Information about the underlying record
linkage process can be incorporated into the method if available (e.g.,
assumed overall mismatch rate, safe matches, predictors of match status,
or predicted probabilities of correct matches).

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
