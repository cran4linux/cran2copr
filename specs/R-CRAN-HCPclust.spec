%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HCPclust
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Conformal Prediction for Clustered Data with Missing Responses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-grf 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-quantregForest 
Requires:         R-stats 
Requires:         R-CRAN-grf 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-quantregForest 

%description
Implements hierarchical conformal prediction for clustered data with
missing responses. The method uses repeated cluster-level splitting and
within-cluster subsampling to accommodate dependence, and
inverse-probability weighting to correct distribution shift induced by
missingness. Conditional densities are estimated by inverting fitted
conditional quantiles (linear quantile regression or quantile regression
forests), and p-values are aggregated across resampling and splitting
steps using the Cauchy combination test.

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
