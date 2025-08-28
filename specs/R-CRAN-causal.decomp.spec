%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  causal.decomp
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Decomposition Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-SuppDists 
BuildRequires:    R-CRAN-PSweight 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-DynTxRegime 
BuildRequires:    R-CRAN-distr 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-modelObj 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-knitr 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-SuppDists 
Requires:         R-CRAN-PSweight 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-DynTxRegime 
Requires:         R-CRAN-distr 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-modelObj 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-knitr 

%description
We implement causal decomposition analysis using methods proposed by Park,
Lee, and Qin (2022) and Park, Kang, and Lee (2023), which provide
researchers with multiple-mediator imputation, single-mediator imputation,
and product-of-coefficients regression approaches to estimate the initial
disparity, disparity reduction, and disparity remaining
(<doi:10.1177/00491241211067516>; <doi:10.1177/00811750231183711>). We
also implement sensitivity analysis for causal decomposition using
R-squared values as sensitivity parameters (Park, Kang, Lee, and Ma, 2023
<doi:10.1515/jci-2022-0031>). Finally, we include individualized causal
decomposition and sensitivity analyses proposed by Park, Kang, and Lee
(2025+) <doi:10.48550/arXiv.2506.19010>.

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
