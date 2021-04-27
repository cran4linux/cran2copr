%global packname  migraph
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          Multimodal and Multilevel Network Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-network 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-network 

%description
A set of tools that extend common social network analysis packages for
analysing multimodal and multilevel networks. It includes functions for
one- and two-mode (and sometimes three-mode) centrality, centralization,
clustering, and constraint, as well as for one- and two-mode network
regression and block-modelling. All functions operate with matrices, edge
lists, and 'igraph', 'network'/'sna', and 'tidygraph' objects. The package
is released as a complement to 'Multimodal Political Networks' (2021,
ISBN:9781108985000), and includes various datasets used in the book.

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
