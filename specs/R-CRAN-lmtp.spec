%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lmtp
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Parametric Causal Effects of Feasible Interventions Based on Modified Treatment Policies

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-future >= 1.17.0
BuildRequires:    R-CRAN-data.table >= 1.13.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-origami 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-isotone 
BuildRequires:    R-CRAN-ife 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-future >= 1.17.0
Requires:         R-CRAN-data.table >= 1.13.0
Requires:         R-stats 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-origami 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-isotone 
Requires:         R-CRAN-ife 
Requires:         R-CRAN-lifecycle 

%description
Non-parametric estimators for casual effects based on longitudinal
modified treatment policies as described in Diaz, Williams, Hoffman, and
Schenck <doi:10.1080/01621459.2021.1955691>, traditional point treatment,
and traditional longitudinal effects. Continuous, binary, categorical
treatments, and multivariate treatments are allowed as well are censored
outcomes. The treatment mechanism is estimated via a density ratio
classification procedure irrespective of treatment variable type. For both
continuous and binary outcomes, additive treatment effects can be
calculated and relative risks and odds ratios may be calculated for binary
outcomes. Supports survival outcomes with competing risks (Diaz, Hoffman,
and Hejazi; <doi:10.1007/s10985-023-09606-7>).

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
