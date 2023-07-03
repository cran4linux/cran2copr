%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  quickPlot
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          A System of Plotting Optimized for Speed and Modularity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-fpCompare 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-fpCompare 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-utils 

%description
A high-level plotting system, compatible with `ggplot2` objects, maps from
`sf`, `terra`, `raster`, `sp`. It is built primarily on the 'grid'
package. The objective of the package is to provide a plotting system that
is built for speed and modularity. This is useful for quick visualizations
when testing code and for plotting multiple figures to the same device
from independent sources that may be independent of one another (i.e.,
different function or modules the create the visualizations).  The
suggested package 'fastshp' can be installed from the repository
(<https://PredictiveEcology.r-universe.dev>).

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
