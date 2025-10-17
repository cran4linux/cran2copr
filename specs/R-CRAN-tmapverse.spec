%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tmapverse
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Meta-Package for Thematic Mapping with 'tmap'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tmap >= 4.2
BuildRequires:    R-CRAN-tmap.glyphs 
BuildRequires:    R-CRAN-tmap.networks 
BuildRequires:    R-CRAN-tmap.cartogram 
BuildRequires:    R-CRAN-tmap.mapgl 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-cols4all 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-tmap >= 4.2
Requires:         R-CRAN-tmap.glyphs 
Requires:         R-CRAN-tmap.networks 
Requires:         R-CRAN-tmap.cartogram 
Requires:         R-CRAN-tmap.mapgl 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stars 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-cols4all 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 

%description
Attaches a set of packages commonly used for spatial plotting with 'tmap'.
It includes 'tmap' and its extensions ('tmap.glyphs', 'tmap.networks',
'tmap.cartogram', 'tmap.mapgl'), as well as supporting spatial data
packages ('sf', 'stars', 'terra') and 'cols4all' for exploring color
palettes. The collection is designed for thematic mapping workflows and
does not include the full set of packages from the R-spatial ecosystem.

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
