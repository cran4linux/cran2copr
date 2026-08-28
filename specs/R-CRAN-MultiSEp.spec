%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultiSEp
%global packver   4.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Predict Synthetic Lethality and Other Gene Dependency Relationships from Multiomics Data

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-igraph 
Requires:         R-grid 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-scales 

%description
Predicts gene dependency relationships (GDRs) from functional genomics
data. Regularised Gaussian mixture modelling may be applied for
unsupervised clustering in addition to other data partitioning strategies.
GDR analysis tools include discovery of synthetic lethal relationships and
predicting population coverage for candidate drug targets from cancer
patient mutational profiles. Functionality for visualisation is also
available. 'MultiSEp' is applicable to data from a variety of sources
including clinical cohorts, organoids and cell lines.

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
