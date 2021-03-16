%global packname  DUBStepR
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Correlation-Based Feature Selection for Single-Cell RNA Sequencing Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-BiocManager 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-flashClust 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-HiClimR 
BuildRequires:    R-CRAN-qlcMatrix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-Seurat 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-BiocManager 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-flashClust 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-HiClimR 
Requires:         R-CRAN-qlcMatrix 
Requires:         R-parallel 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-Seurat 
Requires:         R-methods 
Requires:         R-graphics 

%description
Determining the optimal set of feature genes to characterise cell types in
single-cell RNA sequencing data using stepwise regression on gene-gene
correlations. <doi:10.1101/2020.10.07.330563>.

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
