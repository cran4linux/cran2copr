%global __brp_check_rpaths %{nil}
%global packname  phangorn
%global packver   2.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetic Reconstruction and Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ape >= 5.5
BuildRequires:    R-CRAN-igraph >= 1.0
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape >= 5.5
Requires:         R-CRAN-igraph >= 1.0
Requires:         R-CRAN-fastmatch 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Allows for estimation of phylogenetic trees and networks using Maximum
Likelihood, Maximum Parsimony, distance methods and Hadamard conjugation.
Offers methods for tree comparison, model selection and visualization of
phylogenetic networks as described in Schliep et al. (2017)
<doi:10.1111/2041-210X.12760>.

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
