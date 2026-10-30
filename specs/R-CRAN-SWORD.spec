%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SWORD
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Support Vector Machine Weighted Oblique Random Decision Forests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-Rcpp >= 1.0.0

%description
Implements SWORD (Support vector machine Weighted Oblique Random Decision
forests), a random forest method for regression based on TORS (Tree
Oblique for Regression with weighted SVM) oblique regression trees. At
each internal node a Weighted-SVM classifier with a linear kernel defines
the oblique splitting hyperplane as a sparse linear combination of
predictors. The C++ coordinate-descent solver provides fast training.
Variable importance is computed via OIW-VI (Oblique Impurity-Weighted
Variable Importance). Provides tree fitting (TORS), forest fitting
(SWORD), prediction, and variable importance (VI_SWORD). Parallel tree
fitting is supported via the 'future'/'furrr' framework. The SWORD method
is described in Carta and Frigau (accepted, in press) 'Oblique Random
Forests for Regression via Weighted Support Vector Machine', Advances in
Data Analysis and Classification. The TORS algorithm is described in Carta
and Frigau (2025) <doi:10.1007/s00180-025-01647-w>. The weighted SVM is
based on Yang, Song and Cao (2005) <doi:10.1109/IJCNN.2005.1555965> and
the 'WeightSVM' package by Xu et al. (2024)
<doi:10.32614/CRAN.package.WeightSVM>.

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
