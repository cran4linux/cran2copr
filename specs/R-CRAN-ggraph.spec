%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggraph
%global packver   2.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          An Implementation of Grammar of Graphics for Graphs and Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-graphlayouts >= 1.1.0
BuildRequires:    R-CRAN-igraph >= 1.0.0
BuildRequires:    R-CRAN-ggforce >= 0.3.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-graphlayouts >= 1.1.0
Requires:         R-CRAN-igraph >= 1.0.0
Requires:         R-CRAN-ggforce >= 0.3.1
Requires:         R-CRAN-dplyr 
Requires:         R-grid 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggrepel 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-memoise 

%description
The grammar of graphics as implemented in ggplot2 is a poor fit for graph
and network visualizations due to its reliance on tabular data input.
ggraph is an extension of the ggplot2 API tailored to graph visualizations
and provides the same flexible approach to building up plots layer by
layer.

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
