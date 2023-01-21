%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phylter
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          1%{?dist}%{?buildtag}
Summary:          Detect and Remove Outliers in Phylogenomics Datasets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mrfDepth 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mrfDepth 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-RSpectra 
Requires:         R-stats 
Requires:         R-utils 

%description
Analyzis and filtering of phylogenomics datasets. It takes an input either
a collection of gene trees (then transformed to matrices) or directly a
collection of gene matrices and performs an iterative process to identify
what species in what genes are outliers, and whose elimination
significantly improves the concordance between the input matrices. The
methods builds upon the Distatis approach (Abdi et al. (2005)
<doi:10.1101/2021.09.08.459421>), a generalization of classical
multidimensional scaling to multiple distance matrices.

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
