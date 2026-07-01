%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DSGEr
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Transcriptional Disruption Score for Gene Sets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-POT 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-evd 
Requires:         R-methods 
Requires:         R-CRAN-POT 
Requires:         R-CRAN-Rcpp 

%description
Computes pathway-level transcriptional disruption scores from differential
expression p-values using permutation tests with Generalized Pareto
Distribution (GPD) tail extrapolation and false discovery rate (FDR)
correction. Reference: Guo P, Li H (2026) DSGE: Disruption Score of Gene
Expression for Gene-Set Enrichment Analysis.
<https://github.com/LHJLab/DSGE>.

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
