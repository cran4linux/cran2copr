%global __brp_check_rpaths %{nil}
%global packname  QTLRel
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Mapping of Quantitative Traits of Genetically Related Individuals and Calculating Identity Coefficients from Pedigrees

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-stats 
Requires:         R-CRAN-gdata 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lattice 
Requires:         R-stats 

%description
This software provides tools for quantitative trait mapping in populations
such as advanced intercross lines where relatedness among individuals
should not be ignored. It can estimate background genetic variance
components, impute missing genotypes, simulate genotypes, perform a genome
scan for putative quantitative trait loci (QTL), and plot mapping results.
It also has functions to calculate identity coefficients from pedigrees,
especially suitable for pedigrees that consist of a large number of
generations, or estimate identity coefficients from genotypic data in
certain circumstances.

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
