%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CIMEHR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Clinically Informative Visiting and Observation Processes in Electronic Health Record (EHR) Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-slim 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-slim 

%description
Fits semiparametric joint models for longitudinal electronic health record
(EHR) data that addresses two-stage hierarchical missingness mechanism.
The first stage is the visiting process, and the second stage is the
observation process. The core CIMEHR method (Clinical Informative
Missingness for Electronic Health Records) uses a three-stage procedure:
partial likelihood with log-normal frailty for visit intensity, probit
regression with shared latent factor-linked random effects for
observation, and weighted least squares with risk-set centering for the
outcome. These three stages are connected through a shared latent factor
that induces dependence across all three processes. A data simulator and
implementations of common benchmark methods (linear mixed models, multiple
imputation, and others) are included for comparative studies. Detailed
methods are described in Yang, Shi, and Mukherjee (2026)
<doi:10.48550/arXiv.2602.15374>.

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
