%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crmPack
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Object-Oriented Implementation of CRM Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-CRAN-rjags 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-MASS 

%description
Implements a wide range of model-based dose escalation designs, ranging
from classical and modern continual reassessment methods (CRMs) based on
dose-limiting toxicity endpoints to dual-endpoint designs taking into
account a biomarker/efficacy outcome. The focus is on Bayesian inference,
making it very easy to setup a new design with its own JAGS code. However,
it is also possible to implement 3+3 designs for comparison or models with
non-Bayesian estimation. The whole package is written in a modular form in
the S4 class system, making it very flexible for adaptation to new models,
escalation or stopping rules.

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
