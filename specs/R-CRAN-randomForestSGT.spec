%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  randomForestSGT
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Random Forest Super Greedy Trees

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-randomForestSRC >= 3.6.2
BuildRequires:    R-CRAN-varPro >= 3.1.0
Requires:         R-CRAN-randomForestSRC >= 3.6.2
Requires:         R-CRAN-varPro >= 3.1.0

%description
Implements random forest Super Greedy Trees (SGTs) for regression. SGTs
extend classification and regression tree splitting by fitting
lasso-penalized local parametric models at tree nodes, producing sparse
univariate and multivariate geometric cuts such as axis-aligned splits,
hyperplanes, ellipsoids, hyperboloids, and interaction-based cuts.  Trees
are grown best-split-first by selecting cuts that reduce empirical risk,
and ensembles provide out-of-bag error estimation, prediction on new data,
variable filtering, tuning of the hcut complexity parameter,
coordinate-descent lasso fitting, variable importance, and local
coefficient summaries. For the underlying method, see Ishwaran (2026)
<doi:10.1007/s10462-026-11541-6>.

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
