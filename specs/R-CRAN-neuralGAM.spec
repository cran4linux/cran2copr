%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  neuralGAM
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interpretable Neural Network Based on Generalized Additive Models

License:          MPL-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-gridExtra 

%description
Neural network framework based on Generalized Additive Models from Hastie
& Tibshirani (1990, ISBN:9780412343902), which trains a different neural
network to estimate the contribution of each feature to the response
variable. The networks are trained independently leveraging the local
scoring and backfitting algorithms to ensure that the Generalized Additive
Model converges and it is additive. The resultant Neural Network is a
highly accurate and interpretable deep learning model, which can be used
for high-risk AI practices where decision-making should be based on
accountable and interpretable algorithms.

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
