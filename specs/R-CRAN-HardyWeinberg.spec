%global packname  HardyWeinberg
%global packver   1.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Tests and Graphics for Hardy-Weinberg Equilibrium

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-Rcpp 

%description
Contains tools for exploring Hardy-Weinberg equilibrium (Hardy, 1908;
Weinberg, 1908) <doi:10.1126/science.28.706.49> for bi and multi-allelic
genetic marker data. All classical tests (chi-square, exact,
likelihood-ratio and permutation tests) with bi-allelic variants are
included in the package, as well as functions for power computation and
for the simulation of marker data under equilibrium and disequilibrium.
Routines for dealing with markers on the X-chromosome are included
(Graffelman & Weir, 2016) <doi: 10.1038/hdy.2016.20>, including Bayesian
procedures. Some exact and permutation procedures also work with
multi-allelic variants. Special test procedures that jointly address
Hardy-Weinberg equilibrium and equality of allele frequencies in both
sexes are supplied, for the bi and multi-allelic case. Functions for
testing equilibrium in the presence of missing data by using multiple
imputation are also provided. Implements several graphics for exploring
the equilibrium status of a large set of bi-allelic markers: ternary plots
with acceptance regions, log-ratio plots and Q-Q plots.

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
