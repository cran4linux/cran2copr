%global __brp_check_rpaths %{nil}
%global packname  zonebuilder
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Create and Explore Geographic Zoning Systems

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Functions, documentation and example data to help divide geographic space
into discrete polygons (zones). The functions are motivated by research
into the merits of different zoning systems <doi:10.1068/a090169>. A
flexible 'ClockBoard' zoning system is provided, which breaks-up space by
concentric rings and radial lines emanating from a central point. By
default, the diameter of the rings grow according the triangular number
sequence <doi:10.1080/26375451.2019.1598687> with the first 4 'doughnuts'
(or 'annuli') measuring 1, 3, 6, and 10 km wide. These annuli are
subdivided into equal segments (12 by default), creating the visual
impression of a dartboard. Zones are labelled according to distance to the
centre and angular distance from North, creating a simple geographic
zoning and labelling system useful for visualising geographic phenomena
with a clearly demarcated central location such as cities.

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
