%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cytometree
%global packver   2.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Cytometry Gating and Annotation

License:          LGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-GoFKernel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mclust 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-GoFKernel 

%description
Given the hypothesis of a bi-modal distribution of cells for each marker,
the algorithm constructs a binary tree, the nodes of which are
subpopulations of cells. At each node, observed cells and markers are
modeled by both a family of normal distributions and a family of bi-modal
normal mixture distributions. Splitting is done according to a normalized
difference of AIC between the two families. Method is detailed in:
Commenges, Alkhassim, Gottardo, Hejblum & Thiebaut (2018) <doi:
10.1002/cyto.a.23601>.

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
