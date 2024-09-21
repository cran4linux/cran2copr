%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Colossus
%global packver   1.1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          "Risk Model Regression and Analysis with Complex Non-Linear Models"

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-callr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-processx 

%description
Performs survival analysis using general non-linear models. Risk models
can be the sum or product of terms. Each term is the product of
exponential/linear functions of covariates. Additionally sub-terms can be
defined as a sum of exponential, linear threshold, and step functions. Cox
Proportional hazards
<https://en.wikipedia.org/wiki/Proportional_hazards_model>, Poisson
<https://en.wikipedia.org/wiki/Poisson_regression>, and Fine-Grey
competing risks
<https://www.publichealth.columbia.edu/research/population-health-methods/competing-risk-analysis>
regression are supported. This work was sponsored by NASA Grant
80NSSC19M0161 through a subcontract from the National Council on Radiation
Protection and Measurements (NCRP). The computing for this project was
performed on the Beocat Research Cluster at Kansas State University, which
is funded in part by NSF grants CNS-1006860, EPS-1006860, EPS-0919443,
ACI-1440548, CHE-1726332, and NIH P20GM113109.

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
