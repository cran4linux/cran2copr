%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scTenifoldKnk
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          In-Silico Knockout Experiments from Single-Cell Gene Regulatory Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-scTenifoldNet 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-enrichR 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-scTenifoldNet 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-enrichR 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-reshape2 

%description
A workflow based on 'scTenifoldNet' to perform in-silico knockout
experiments using single-cell RNA sequencing (scRNA-seq) data from
wild-type (WT) control samples as input.  First, the package constructs a
single-cell gene regulatory network (scGRN) and knocks out a target gene
from the adjacency matrix of the WT scGRN by setting the gene’s outdegree
edges to zero. Then, it compares the knocked out scGRN with the WT scGRN
to identify differentially regulated genes, called virtual-knockout
perturbed genes, which are used to assess the impact of the gene knockout
and reveal the gene’s function in the analyzed cells.

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
