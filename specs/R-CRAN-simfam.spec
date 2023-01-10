%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simfam
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate and Model Family Pedigrees with Structured Founders

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
The focus is on simulating and modeling families with founders drawn from
a structured population (for example, with different ancestries or other
potentially non-family relatedness), in contrast to traditional pedigree
analysis that treats all founders as equally unrelated.  Main function
simulates a random pedigree for many generations, avoiding close
relatives, pairing closest individuals according to a 1D geography and
their randomly-drawn sex, and with variable children sizes to result in a
target population size per generation.  Auxiliary functions calculate
kinship matrices, admixture matrices, and draw random genotypes across
arbitrary pedigree structures starting from the corresponding founder
values.  The code is built around the plink FAM table format for
pedigrees.  Described in Yao and Ochoa (2022)
<doi:10.1101/2022.03.25.485885>.

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
