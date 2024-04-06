%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SpaDES
%global packver   2.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.10
Release:          1%{?dist}%{?buildtag}
Summary:          Develop and Run Spatially Explicit Discrete Event Simulation Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-SpaDES.tools >= 2.0.5
BuildRequires:    R-CRAN-SpaDES.core >= 2.0.3
BuildRequires:    R-CRAN-reproducible >= 2.0.10
BuildRequires:    R-CRAN-quickPlot >= 1.0.2
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-SpaDES.tools >= 2.0.5
Requires:         R-CRAN-SpaDES.core >= 2.0.3
Requires:         R-CRAN-reproducible >= 2.0.10
Requires:         R-CRAN-quickPlot >= 1.0.2
Requires:         R-methods 
Requires:         R-utils 

%description
Metapackage for implementing a variety of event-based models, with a focus
on spatially explicit models. These include raster-based, event-based, and
agent-based models. The core simulation components (provided by
'SpaDES.core') are built upon a discrete event simulation (DES; see
Matloff (2011) ch 7.8.3 <https://nostarch.com/artofr.htm>) framework that
facilitates modularity, and easily enables the user to include additional
functionality by running user-built simulation modules (see also
'SpaDES.tools'). Included are numerous tools to visualize rasters and
other maps (via 'quickPlot'), and caching methods for reproducible
simulations (via 'reproducible'). Tools for running simulation experiments
are provided by 'SpaDES.experiment'. Additional functionality is provided
by the 'SpaDES.addins' and 'SpaDES.shiny' packages.

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
