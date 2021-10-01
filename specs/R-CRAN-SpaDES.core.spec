%global __brp_check_rpaths %{nil}
%global packname  SpaDES.core
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Core Utilities for Developing and Running Spatially Explicit Discrete Event Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.5.8
BuildRequires:    R-CRAN-reproducible >= 1.2.7
BuildRequires:    R-CRAN-data.table >= 1.11.0
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-qs >= 0.21.1
BuildRequires:    R-CRAN-quickPlot >= 0.1.4
BuildRequires:    R-CRAN-Require >= 0.0.7
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-fastdigest 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whisker 
Requires:         R-CRAN-raster >= 2.5.8
Requires:         R-CRAN-reproducible >= 1.2.7
Requires:         R-CRAN-data.table >= 1.11.0
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-qs >= 0.21.1
Requires:         R-CRAN-quickPlot >= 0.1.4
Requires:         R-CRAN-Require >= 0.0.7
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-fastdigest 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-whisker 

%description
Provides the core framework for a discrete event system (DES) to implement
a complete data-to-decisions, reproducible workflow. The core DES
components facilitate modularity, and easily enable the user to include
additional functionality by running user-built modules. Includes
conditional scheduling, restart after interruption, packaging of reusable
modules, tools for developing arbitrary automated workflows, automated
interweaving of modules of different temporal resolution, and tools for
visualizing and understanding the DES project.

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
