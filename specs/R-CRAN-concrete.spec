%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  concrete
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Continuous-Time Competing Risks Estimation using Targeted Minimum Loss-Based Estimation (TMLE)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-origami 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.11
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-origami 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-MASS 

%description
One-step continuous-time Targeted Minimum Loss-Based Estimation (TMLE) for
outcome-specific absolute risk estimands in right-censored survival
settings with or without competing risks, implementing the methodology
described in Rytgaard et al. (2023) <doi:10.1111/biom.13856> and Rytgaard
and van der Laan (2023) <doi:10.1007/s10985-022-09576-2>. Currently
'concrete' can be used to estimate the effects of static or dynamic
interventions on binary treatments given at baseline, cross-validated
initial estimation of treatment propensity is done using the
'SuperLearner' package, and initial estimation of conditional hazards is
done using ensembles of Cox regressions from the 'survival' package or
Coxnet from the 'glmnet' package.

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
