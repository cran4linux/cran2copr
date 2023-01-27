%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adegenet
%global packver   2.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Analysis of Genetic and Genomic Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildRequires:    R-CRAN-dplyr >= 0.4.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-dplyr >= 0.4.1
Requires:         R-methods 
Requires:         R-CRAN-ade4 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-seqinr 
Requires:         R-parallel 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-vegan 

%description
Toolset for the exploration of genetic and genomic data. Adegenet provides
formal (S4) classes for storing and handling various genetic data,
including genetic markers with varying ploidy and hierarchical population
structure ('genind' class), alleles counts by populations ('genpop'), and
genome-wide SNP data ('genlight'). It also implements original
multivariate methods (DAPC, sPCA), graphics, statistical tests, simulation
tools, distance and similarity measures, and several spatial methods. A
range of both empirical and simulated datasets is also provided to
illustrate various methods.

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
