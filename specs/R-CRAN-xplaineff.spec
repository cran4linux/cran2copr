%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xplaineff
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Decomposing Global Feature Effects Based on Feature Interactions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-R6 >= 2.6.1
BuildRequires:    R-CRAN-checkmate >= 2.3.2
BuildRequires:    R-CRAN-ggraph >= 2.2.1
BuildRequires:    R-CRAN-igraph >= 2.1.4
BuildRequires:    R-CRAN-patchwork >= 1.3.0
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-mlr3misc >= 0.14.0
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-R6 >= 2.6.1
Requires:         R-CRAN-checkmate >= 2.3.2
Requires:         R-CRAN-ggraph >= 2.2.1
Requires:         R-CRAN-igraph >= 2.1.4
Requires:         R-CRAN-patchwork >= 1.3.0
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-mlr3misc >= 0.14.0

%description
Implements the GADGET (Generalized Additive Decomposition of Global
EffecTs) algorithm for interpretable machine learning. The package
recursively partitions the feature space to minimize heterogeneity of
feature effects (e.g., Accumulated Local Effects or Partial Dependence),
producing a tree of regions where effects are more stable. It supports
both ALE and PD strategies, works with 'mlr3' learners and provides
visualization of the interaction tree and regional effect plots. The
method is described in Herbinger, J., Wright, M. N., Nagler, T., Bischl,
B., and Casalicchio, G. (2024), "Decomposing Global Feature Effects Based
on Feature Interactions"
<https://jmlr.org/papers/volume25/23-0699/23-0699.pdf>.

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
