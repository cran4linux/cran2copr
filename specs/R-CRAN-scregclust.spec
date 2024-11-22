%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scregclust
%global packver   0.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Reconstructing the Regulatory Programs of Target Genes in scRNA-Seq Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-igraph 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-prettyunits 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 

%description
Implementation of the scregclust algorithm described in Larsson, Held, et
al. (2024) <doi:10.1038/s41467-024-53954-3> which reconstructs regulatory
programs of target genes in scRNA-seq data. Target genes are clustered
into modules and each module is associated with a linear model describing
the regulatory program.

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
