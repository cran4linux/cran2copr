%global __brp_check_rpaths %{nil}
%global packname  HACSim
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Iterative Extrapolation of Species' Haplotype Accumulation Curves for Genetic Diversity Assessment

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ape >= 5.3
BuildRequires:    R-graphics >= 3.6.1
BuildRequires:    R-stats >= 3.6.1
BuildRequires:    R-utils >= 3.6.1
BuildRequires:    R-CRAN-shiny >= 1.6.0
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-matrixStats >= 0.56.0
BuildRequires:    R-CRAN-pegas >= 0.13
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ape >= 5.3
Requires:         R-graphics >= 3.6.1
Requires:         R-stats >= 3.6.1
Requires:         R-utils >= 3.6.1
Requires:         R-CRAN-shiny >= 1.6.0
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-matrixStats >= 0.56.0
Requires:         R-CRAN-pegas >= 0.13

%description
Performs iterative extrapolation of species' haplotype accumulation curves
using a nonparametric stochastic (Monte Carlo) optimization method for
assessment of specimen sampling completeness based on the approach of
Phillips et al. (2015) <doi:10.1515/dna-2015-0008>, Phillips et al. (2019)
<doi:10.1002/ece3.4757> and Phillips et al. (2020) <doi:
10.7717/peerj-cs.243>. 'HACSim' outputs a number of useful summary
statistics of sampling coverage ("Measures of Sampling Closeness"),
including an estimate of the likely required sample size (along with
desired level confidence intervals) necessary to recover a given
number/proportion of observed unique species' haplotypes. Any genomic
marker can be targeted to assess likely required specimen sample sizes for
genetic diversity assessment. The method is particularly well-suited to
assess sampling sufficiency for DNA barcoding initiatives. Users can also
simulate their own DNA sequences according to various models of nucleotide
substitution. A Shiny app is also available.

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
