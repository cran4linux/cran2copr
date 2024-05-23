%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CompMix
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Comprehensive Toolkit for Environmental Mixtures Analysis ('CompMix')

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-gglasso 
BuildRequires:    R-CRAN-higlasso 
BuildRequires:    R-CRAN-hierNet 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-bkmr 
BuildRequires:    R-CRAN-qgcomp 
BuildRequires:    R-CRAN-gWQS 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-devtools 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-gglasso 
Requires:         R-CRAN-higlasso 
Requires:         R-CRAN-hierNet 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-bkmr 
Requires:         R-CRAN-qgcomp 
Requires:         R-CRAN-gWQS 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-devtools 

%description
Quantitative characterization of the health impacts associated with
exposure to chemical mixtures has received considerable attention in
current environmental and epidemiological studies. 'CompMix' package
allows practitioners to estimate the health impacts from exposure to
chemical mixtures data through various statistical approaches, including
Lasso, Elastic net, Bayeisan kernel machine regression (BKMR), hierNet,
Quantile g-computation, Weighted quantile sum (WQS) and Random forest. Hao
W, Cathey A, Aung M, Boss J, Meeker J, Mukherjee B. (2024) "Statistical
methods for chemical mixtures: a practitioners guide".
<DOI:10.1101/2024.03.03.24303677>.

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
