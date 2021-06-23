%global __brp_check_rpaths %{nil}
%global packname  MinBAR
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Determining the Minimal Background Area for Species Distribution Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ecospat >= 2.2
BuildRequires:    R-CRAN-geosphere >= 1.5.5
BuildRequires:    R-CRAN-dismo >= 1.1.4
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-maxnet 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-latticeExtra 
Requires:         R-CRAN-ecospat >= 2.2
Requires:         R-CRAN-geosphere >= 1.5.5
Requires:         R-CRAN-dismo >= 1.1.4
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-maxnet 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-latticeExtra 

%description
A versatile tool that aims at (1) defining the minimum background extent
necessary to fit Species Distribution Models reliable enough to extract
ecologically relevant conclusions from them and (2) optimizing the
modelling process in terms of computation demands. See Rotllan-Puig, X. &
Traveset, A. (2021)
<https://www.sciencedirect.com/science/article/pii/S0304380020304191>.

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
