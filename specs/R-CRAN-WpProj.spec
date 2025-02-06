%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WpProj
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Linear p-Wasserstein Projections

License:          GPL (== 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-approxOT >= 1.2
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-oem 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ROI 
BuildRequires:    R-CRAN-ROI.plugin.ecos 
BuildRequires:    R-CRAN-ROI.plugin.lpsolve 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-rqPen 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-RcppCGAL 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-RSpectra 
Requires:         R-CRAN-approxOT >= 1.2
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-oem 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ROI 
Requires:         R-CRAN-ROI.plugin.ecos 
Requires:         R-CRAN-ROI.plugin.lpsolve 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-rqPen 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-lifecycle 

%description
Performs Wasserstein projections from the predictive distributions of any
model into the space of predictive distributions of linear models. We
utilize L1 penalties to also reduce the complexity of the model space.
This package employs the methods as described in Dunipace, Eric and
Lorenzo Trippa (2020) <doi:10.48550/arXiv.2012.09999>.

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
