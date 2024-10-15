%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clustTMB
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatio-Temporal Finite Mixture Model using 'TMB'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-TMB >= 1.9.0
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-clustMixType 
BuildRequires:    R-CRAN-fmesher 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reformulas 
BuildRequires:    R-CRAN-MoEClust 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-TMB >= 1.9.0
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-clustMixType 
Requires:         R-CRAN-fmesher 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mclust 
Requires:         R-methods 
Requires:         R-CRAN-reformulas 
Requires:         R-CRAN-MoEClust 
Requires:         R-CRAN-sf 
Requires:         R-stats 

%description
Fits a spatio-temporal finite mixture model using 'TMB'. Covariate,
spatial and temporal random effects can be incorporated into the gating
formula using multinomial logistic regression, the expert formula using a
generalized linear mixed model framework, or both.

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
