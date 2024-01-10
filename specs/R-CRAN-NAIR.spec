%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NAIR
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Network Analysis of Immune Repertoire

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-RcppArmadillo >= 0.10.8.0.0
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 

%description
Pipelines for studying the adaptive immune repertoire of T cells and B
cells via network analysis based on receptor sequence similarity. Relate
clinical outcomes to immune repertoires based on their network properties,
or to particular clusters and clones within a repertoire. Yang et al.
(2023) <doi:10.3389/fimmu.2023.1181825>.

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
