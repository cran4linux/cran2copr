%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  migraph
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Inferential Methods for Multimodal and Other Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-manynet >= 1.0.5
BuildRequires:    R-CRAN-autograph >= 0.4.0
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-manynet >= 1.0.5
Requires:         R-CRAN-autograph >= 0.4.0
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-purrr 

%description
A set of tools for testing networks. It includes functions for univariate
and multivariate conditional uniform graph and quadratic assignment
procedure testing, and network regression. The package is a complement to
'Multimodal Political Networks' (2021, ISBN:9781108985000), and includes
various datasets used in the book. Built on the 'manynet' package, all
functions operate with matrices, edge lists, and 'igraph', 'network', and
'tidygraph' objects, and on one-mode and two-mode (bipartite) networks.

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
