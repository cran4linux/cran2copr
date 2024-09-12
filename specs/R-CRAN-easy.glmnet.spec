%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easy.glmnet
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Simplify the Use of 'glmnet' for Machine Learning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-glmnet 
Requires:         R-parallel 
Requires:         R-CRAN-survival 

%description
Provides several functions to simplify using the 'glmnet' package:
converting data frames into matrices ready for 'glmnet'; b) imputing
missing variables multiple times; c) fitting and applying prediction
models straightforwardly; d) assigning observations to folds in a balanced
way; e) cross-validate the models; f) selecting the most representative
model across imputations and folds; and g) getting the relevance of the
model regressors; as described in several publications: Solanes et al.
(2022) <doi:10.1038/s41537-022-00309-w>, Palau et al. (2023)
<doi:10.1016/j.rpsm.2023.01.001>, Sobregrau et al. (2024)
<doi:10.1016/j.jpsychores.2024.111656>.

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
