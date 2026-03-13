%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  INCVCommunityDetection
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Inductive Node-Splitting Cross-Validation for Community Detection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-ClusterR 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-IMIFA 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-ClusterR 
Requires:         R-CRAN-irlba 
Requires:         R-parallel 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-IMIFA 
Requires:         R-stats 

%description
Implements Inductive Node-Splitting Cross-Validation (INCV) for selecting
the number of communities in stochastic block models. Provides f-fold and
random-split node-level cross-validation, along with competing methods
including CROISSANT, Edge Cross-Validation (ECV), and Node
Cross-Validation (NCV). Supports both SBM and Degree-Corrected Block
Models (DCBM), with multiple loss functions (L2, binomial deviance, AUC).
Includes network simulation utilities for SBM, RDPG, and latent space
models.

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
