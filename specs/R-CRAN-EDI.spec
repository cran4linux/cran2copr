%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EDI
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Experimental Design and Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-missRanger 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RhpcBLASctl 
BuildRequires:    R-CRAN-randomizr 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppNumerical 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-missRanger 
Requires:         R-CRAN-missForest 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-digest 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-RhpcBLASctl 
Requires:         R-CRAN-randomizr 

%description
Implements a comprehensive suite of experimental designs, both fixed
(e.g., block, stratified, matched-pair, cluster, factorial, and
mixed-integer-programming-based optimal designs) and sequential (including
matching-on-the-fly designs, biased coin designs, and covariate-adaptive
urn designs that assign treatment one subject at a time while maintaining
covariate balance), for continuous, incidence, count, proportion,
survival, and ordinal response types. For each design and response type
combination, provides the corresponding inference procedures, including
exact, asymptotic, distribution-free, and resampling-based (bootstrap,
jackknife, and randomization) methods, so that estimation and testing are
always matched to how the data were generated. An 'InferenceSuite'
facility runs all applicable inference procedures for a given design and
response type at once and reports a single Cauchy-combined p-value
summarizing their evidence. A built-in simulation framework supports power
analysis and operating-characteristic studies across designs, response
types, and inference procedures, with optional parallelization via
'mirai'. Missing covariate data is handled automatically via built-in
imputation. Core numerical routines are implemented in C++ via 'Rcpp' for
speed on large designs and simulation studies. Machine-specific tuning for
optimization is included.

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
