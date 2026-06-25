%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gaQSAR
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          QSAR Modelling Using Genetic Algorithm Based Variable Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-prospectr 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-stats 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-prospectr 
Requires:         R-CRAN-reshape2 

%description
Implements genetic algorithm-based variable selection for building
quantitative structure-activity relationship (QSAR) models. The package
provides a workflow for selecting optimal predictor subsets from large
descriptor spaces using leave-one-out cross-validation (LOOCV) with Q2 as
the fitness criterion. Features include automatic handling of
multicollinearity via variance inflation factor (VIF) thresholding,
customizable genetic algorithm operators, and diagnostic tools for model
evaluation. Supports both training set optimization and external
validation, plus nested (double) cross-validation for unbiased performance
estimation and predictor stability diagnostics. Built-in visualization
functions include Q2 curves and Williams plots to assess model
applicability domain. The method is demonstrated in papers predicting
antibacterial activity by Araya-Cloutier et al. (2018)
<doi:10.1038/s41598-018-27545-4> and Kalli et al. (2021)
<doi:10.1038/s41598-021-92964-9>.

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
