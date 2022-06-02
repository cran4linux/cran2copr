%global __brp_check_rpaths %{nil}
%global packname  iCAMP
%global packver   1.5.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.12
Release:          1%{?dist}%{?buildtag}
Summary:          Infer Community Assembly Mechanisms by Phylogenetic-Bin-Based Null Model Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-DirichletReg 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-vegan 
Requires:         R-parallel 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-Hmisc 
Requires:         R-stats4 
Requires:         R-CRAN-DirichletReg 
Requires:         R-CRAN-data.table 

%description
To implement a general framework to quantitatively infer Community
Assembly Mechanisms by Phylogenetic-bin-based null model analysis,
abbreviated as 'iCAMP' (Ning et al 2020) <doi:10.1038/s41467-020-18560-z>.
It can quantitatively assess the relative importance of different
community assembly processes, such as selection, dispersal, and drift, for
both communities and each phylogenetic group ('bin'). Each bin usually
consists of different taxa from a family or an order. The package also
provides functions to implement some other published methods, including
neutral taxa percentage (Burns et al 2016) <doi:10.1038/ismej.2015.142>
based on neutral theory model and quantifying assembly processes based on
entire-community null models ('QPEN', Stegen et al 2013)
<doi:10.1038/ismej.2013.93>. It also includes some handy functions,
particularly for big datasets, such as phylogenetic and taxonomic null
model analysis at both community and bin levels, between-taxa niche
difference and phylogenetic distance calculation, phylogenetic signal test
within phylogenetic groups, midpoint root of big trees, etc. Version 1.3.x
mainly improved the function for 'QPEN' and added function 'icamp.cate()'
to summarize 'iCAMP' results for different categories of taxa (e.g. core
versus rare taxa).

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
