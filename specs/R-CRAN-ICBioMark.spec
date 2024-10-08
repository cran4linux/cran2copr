%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ICBioMark
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Data-Driven Design of Targeted Gene Panels for Estimating Immunotherapy Biomarkers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gglasso 
BuildRequires:    R-CRAN-PRROC 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gglasso 
Requires:         R-CRAN-PRROC 

%description
Implementation of the methodology proposed in 'Data-driven design of
targeted gene panels for estimating immunotherapy biomarkers', Bradley and
Cannings (2021) <arXiv:2102.04296>. This package allows the user to fit
generative models of mutation from an annotated mutation dataset, and then
further to produce tunable linear estimators of exome-wide biomarkers. It
also contains functions to simulate mutation annotated format (MAF) data,
as well as to analyse the output and performance of models.

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
