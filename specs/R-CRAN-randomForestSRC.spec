%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  randomForestSRC
%global packver   3.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Unified Random Forests for Survival, Regression, and Classification (RF-SRC)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-DiagrammeR 
Requires:         R-parallel 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-DiagrammeR 

%description
Fast OpenMP parallel computing of Breiman's random forests for univariate,
multivariate, unsupervised, survival, competing risks, class imbalanced
classification and quantile regression. New Mahalanobis splitting for
correlated outcomes.  Extreme random forests and randomized splitting.
Suite of imputation methods for missing data.  Fast random forests using
subsampling. Confidence regions and standard errors for variable
importance. New improved holdout importance. Case-specific importance.
Minimal depth variable importance. Visualize trees on your Safari or
Google Chrome browser. Anonymous random forests for data privacy.

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
