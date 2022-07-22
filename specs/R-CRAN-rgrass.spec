%global __brp_check_rpaths %{nil}
%global packname  rgrass
%global packver   0.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interface Between 'GRASS' Geographical Information System and 'R'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-XML 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
An interface between the 'GRASS' geographical information system ('GIS')
and 'R', based on starting 'R' from within the 'GRASS' 'GIS' environment,
or running a free-standing 'R' session in a temporary 'GRASS' location;
the package provides facilities for using all 'GRASS' commands from the
'R' command line. The original interface package for 'GRASS 5' (2000-2010)
is described in Bivand (2000) <doi:10.1016/S0098-3004(00)00057-1> and
Bivand (2001)
<https://www.r-project.org/conferences/DSC-2001/Proceedings/Bivand.pdf>.
This was succeeded by 'spgrass6' for 'GRASS 6' (2006-2016) and 'rgrass7'
for 'GRASS 7' (2015-present). The 'rgrass' package modernizes the
interface for 'GRASS 8' while still permitting the use of 'GRASS 7'.

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
