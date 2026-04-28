%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FrailtyCompRisk
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Competing Risks Models for Multi-Center Survival Data with Frailty

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 

%description
Implements methods for analyzing competing risks data in multi-center
survival studies using frailty models. The approach relies on a mixed
proportional hazards model for the sub-distribution, allowing for
cluster-specific random effects. The package provides tools for model
estimation with or without frailty using Maximum Likelihood (ML) and
Restricted Maximum Likelihood (REML). It supports flexible modeling of
between-center heterogeneity and is particularly suited for multi-center
clinical trials or registries. Core features include data simulation,
likelihood computation, cluster-dependent censoring options, and testing
of frailty effects. For methodological details, see Katsahian et al.
(2006) <doi:10.1002/sim.2684>.

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
