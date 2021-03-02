%global packname  genetics
%global packver   1.3.8.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.8.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Population Genetics

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 

%description
Classes and methods for handling genetic data. Includes classes to
represent genotypes and haplotypes at single markers up to multiple
markers on multiple chromosomes. Function include allele frequencies,
flagging homo/heterozygotes, flagging carriers of certain alleles,
estimating and testing for Hardy-Weinberg disequilibrium, estimating and
testing for linkage disequilibrium, ...

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
