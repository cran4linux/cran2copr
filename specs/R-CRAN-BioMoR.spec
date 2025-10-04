%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BioMoR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bioinformatics Modeling with Recursion and Autoencoder-Based Ensemble

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-themis 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-pROC 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-themis 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-pROC 

%description
Tools for bioinformatics modeling using recursive transformer-inspired
architectures, autoencoders, random forests, XGBoost, and stacked ensemble
models. Includes utilities for cross-validation, calibration,
benchmarking, and threshold optimization in predictive modeling workflows.
The methodology builds on ensemble learning (Breiman 2001
<doi:10.1023/A:1010933404324>), gradient boosting (Chen and Guestrin 2016
<doi:10.1145/2939672.2939785>), autoencoders (Hinton and Salakhutdinov
2006 <doi:10.1126/science.1127647>), and recursive transformer efficiency
approaches such as Mixture-of-Recursions (Bae et al. 2025
<doi:10.48550/arXiv.2507.10524>).

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
