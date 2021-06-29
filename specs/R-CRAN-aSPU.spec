%global __brp_check_rpaths %{nil}
%global packname  aSPU
%global packver   1.50
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.50
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Sum of Powered Score Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gee 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-gee 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-matrixStats 

%description
R codes for the (adaptive) Sum of Powered Score ('SPU' and 'aSPU') tests,
inverse variance weighted Sum of Powered score ('SPUw' and 'aSPUw') tests
and gene-based and some pathway based association tests (Pathway based Sum
of Powered Score tests ('SPUpath'), adaptive 'SPUpath' ('aSPUpath') test,
'GEEaSPU' test for multiple traits - single 'SNP' (single nucleotide
polymorphism) association in generalized estimation equations, 'MTaSPUs'
test for multiple traits - single 'SNP' association with Genome Wide
Association Studies ('GWAS') summary statistics, Gene-based Association
Test that uses an extended 'Simes' procedure ('GATES'), Hybrid Set-based
Test ('HYST') and extended version of 'GATES' test for pathway-based
association testing ('GATES-Simes'). ). The tests can be used with genetic
and other data sets with covariates. The response variable is binary or
quantitative. Summary; (1) Single trait-'SNP' set association with
individual-level data ('aSPU', 'aSPUw', 'aSPUr'), (2) Single trait-'SNP'
set association with summary statistics ('aSPUs'), (3) Single
trait-pathway association with individual-level data ('aSPUpath'), (4)
Single trait-pathway association with summary statistics ('aSPUsPath'),
(5) Multiple traits-single 'SNP' association with individual-level data
('GEEaSPU'), (6) Multiple traits- single 'SNP' association with summary
statistics ('MTaSPUs'), (7) Multiple traits-'SNP' set association with
summary statistics('MTaSPUsSet'), (8) Multiple traits-pathway association
with summary statistics('MTaSPUsSetPath').

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
