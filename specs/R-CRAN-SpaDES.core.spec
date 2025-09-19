%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpaDES.core
%global packver   2.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Core Utilities for Developing and Running Spatially Explicit Discrete Event Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-reproducible >= 2.1.1
BuildRequires:    R-CRAN-terra >= 1.7.46
BuildRequires:    R-CRAN-data.table >= 1.11.0
BuildRequires:    R-CRAN-quickPlot >= 1.0.2
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-Require >= 0.3.1
BuildRequires:    R-CRAN-qs >= 0.21.1
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-lobstr 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whisker 
Requires:         R-CRAN-reproducible >= 2.1.1
Requires:         R-CRAN-terra >= 1.7.46
Requires:         R-CRAN-data.table >= 1.11.0
Requires:         R-CRAN-quickPlot >= 1.0.2
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-Require >= 0.3.1
Requires:         R-CRAN-qs >= 0.21.1
Requires:         R-CRAN-cli 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-lobstr 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-whisker 

%description
Provides the core framework for a discrete event system to implement a
complete data-to-decisions, reproducible workflow. The core components
facilitate the development of modular pieces, and enable the user to
include additional functionality by running user-built modules. Includes
conditional scheduling, restart after interruption, packaging of reusable
modules, tools for developing arbitrary automated workflows, automated
interweaving of modules of different temporal resolution, and tools for
visualizing and understanding the within-project dependencies. The
suggested package 'NLMR' can be installed from the repository
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
