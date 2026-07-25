%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IRTC
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Marginal Maximum Likelihood Estimation for Item Response Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-tools 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-tools 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Self-contained marginal maximum likelihood (MML) estimation for
unidimensional and multidimensional item response models, including the
Rasch / one-parameter logistic, partial credit, rating scale,
two-parameter logistic and generalised partial credit models, with latent
regression, multiple groups and case weights. A parallelised,
dimension-factorised streaming estimation engine supports large
between-item (simple-structure) multidimensional models with bounded
memory and an opt-in controlled-accuracy quadrature mode that reports a
measured approximation error. A usability layer serves non-specialists and
automated pipelines: one-stop estimation from common file formats
('Excel', delimited text, 'SPSS', 'Stata', 'SAS') with automatic cleaning
and answer-key scoring, pre-estimation data checks, classical item
statistics and item fit, plain-language quality ratings, bilingual
(English/Chinese) output, spreadsheet exports for item banking and
cross-year linking, audience-specific 'Word'/'HTML' reports, and
machine-readable results with structured error conditions. Methods follow
Adams, Wilson and Wang (1997) <doi:10.1177/0146621697211001>.

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
