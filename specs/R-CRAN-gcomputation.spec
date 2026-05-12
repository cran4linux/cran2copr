%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gcomputation
%global packver   0.34
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.34
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Inference by using G-Computation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-hdnom 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-hdnom 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mice 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Several functions and S3 methods for G-computation and emulation of
clinical trials. It allows for flexible estimation of the outcome model,
especially penalized regressions (Lasso, Ridge, or Elasticnet) for binary,
continuous, counting, or right-censored time-to-event outcomes. Average
treatment effect among the entire population (ATE) or among the treated
population (ATT) can be estimated. The method for time-to-events is
described by Chatton et al. (2020) <doi:10.1038/s41598-020-65917-x>.  For
a binary outcome, details are available in the paper proposed by Chatton
et al. (2022) <doi:10.1177/09622802211047345>.

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
