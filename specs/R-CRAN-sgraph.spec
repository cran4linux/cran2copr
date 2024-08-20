%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sgraph
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Network Visualization Using 'sigma.js'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-stringi 

%description
Interactive visualizations of graphs created with the 'igraph' package
using a 'htmlwidgets' wrapper for the 'sigma.js' network visualization
v2.4.0 <https://www.sigmajs.org/>, enabling to display several thousands
of nodes. While several 'R' packages have been developed to interface
'sigma.js', all were developed for v1.x.x and none have migrated to v2.4.0
nor are they planning to. This package builds upon the 'sigmaNet' package,
and users familiar with it will recognize the similar design approach. Two
extensions have been added to the classic 'sigma.js' visualizations by
overriding the underlying 'JavaScript' code, enabling to draw a frame
around node labels, and to display labels on multiple lines by parsing
line breaks. Other additional functionalities that did not require
overriding 'sigma.js' code include toggling node visibility when clicked
using a node attribute and highlighting specific edges. 'sigma.js' is
currently preparing a stable release v3.0.0, and this package plans to
update to it when it is available.

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
