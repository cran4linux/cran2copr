%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  varPro
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Model-Independent Variable Selection via the Rule-Based Variable Priority

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-randomForestSRC >= 3.4.5
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-BART 
BuildRequires:    R-CRAN-umap 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-randomForestSRC >= 3.4.5
Requires:         R-CRAN-glmnet 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-BART 
Requires:         R-CRAN-umap 
Requires:         R-CRAN-survival 

%description
A new framework of variable selection, which instead of generating
artificial covariates such as permutation importance and knockoffs,
creates release rules to examine the affect on the response for each
covariate where the conditional distribution of the response variable can
be arbitrary and unknown.

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
