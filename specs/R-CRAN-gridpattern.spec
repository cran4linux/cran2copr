%global __brp_check_rpaths %{nil}
%global packname  gridpattern
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          'grid' Pattern Grobs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-utils 
Requires:         R-CRAN-glue 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-png 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-utils 

%description
Provides 'grid' grobs that fill in a user-defined area with various
patterns.  Includes enhanced versions of the geometric and image-based
patterns originally contained in the 'ggpattern' package as well as
original 'pch', 'polygon_tiling', 'regular_polygon', 'rose', 'text',
'wave', and 'weave' patterns plus support for custom user-defined
patterns.

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
