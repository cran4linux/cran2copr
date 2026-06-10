%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  evoFE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Evolutionary Feature Engineering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lightgbm 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-quitefastmst 
BuildRequires:    R-CRAN-genieclust 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lightgbm 
Requires:         R-CRAN-xgboost 
Requires:         R-stats 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-quitefastmst 
Requires:         R-CRAN-genieclust 

%description
Automates feature engineering using evolutionary algorithms inspired by
genetic programming. Starting from raw input features, the package evolves
candidate transformation recipes through selection, crossover, and
mutation, evaluating fitness via cross-validation or train/validation
splits with gradient-boosted tree models ('LightGBM' or 'XGBoost').
Built-in transformers include arithmetic, logarithmic, and power
operations, interaction terms, target encoding, quantile and log-based
binning, principal component analysis, truncated singular value
decomposition, Uniform Manifold Approximation and Projection (UMAP)
dimensionality reduction, and minimum spanning tree (MST) graph-based
clustering. The evolutionary search yields an optimised feature recipe
that can be applied to new data for prediction. Methods are described in
McInnes et al. (2018) <doi:10.21105/joss.00861>, Ke et al. (2017)
<https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-framework>,
Chen and Guestrin (2016) <doi:10.1145/2939672.2939785>, Gagolewski (2021)
<doi:10.1016/j.softx.2021.100722>, Gagolewski (2026)
<doi:10.32614/CRAN.package.lumbermark>, and Gagolewski (2026)
<doi:10.32614/CRAN.package.deadwood>.

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
