%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  musicXML
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Sonification using 'musicXML'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-xml2 

%description
A set of tools to facilitate data sonification and handle the 'musicXML'
format
<https://usermanuals.musicxml.com/MusicXML/Content/XS-MusicXML.htm>.
Several classes are defined for basic musical objects such as note pitch,
note duration, note, measure and score. Moreover, sonification utilities
functions are provided, e.g. to map data into musical attributes such as
pitch, loudness or duration. A typical sonification workflow hence looks
like: get data; map them to musical attributes; create and write the
'musicXML' score, which can then be further processed using specialized
music software (e.g. 'MuseScore', 'GuitarPro', etc.). Examples can be
found in the blog <https://globxblog.github.io/>, the presentation by
Renard and Le Bescond (2022, <https://hal.science/hal-03710340v1>) or the
poster by Renard et al. (2023, <https://hal.inrae.fr/hal-04388845v1>).

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
