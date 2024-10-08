%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  heckmanGE
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Inference for Heckman Selection Models with Cluster-Robust Variance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-glm2 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-miscTools 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-glm2 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-miscTools 
Requires:         R-CRAN-vctrs 

%description
Tools for the estimation of Heckman selection models with robust
variance-covariance matrices. It includes functions for computing the
bread and meat matrices, as well as clustered standard errors for
generalized Heckman models, see Fernando de Souza Bastos and Wagner
Barreto-Souza and Marc G. Genton (2022, ISSN:
<https://www.jstor.org/stable/27164235>). The package also offers
cluster-robust inference with sandwich estimators, and tools for handling
issues related to eigenvalues in covariance matrices.

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
