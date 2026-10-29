%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hairline
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clean, Predictable Figures for Medical and Data Science

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-grid 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-ragg 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-systemfonts 
BuildRequires:    R-CRAN-textshaping 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-S7 
Requires:         R-grid 
Requires:         R-grDevices 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-ragg 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-systemfonts 
Requires:         R-CRAN-textshaping 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-yaml 

%description
A design system for 'ggplot2' figures: one frame for titles, legends,
panels and captions, a fixed spacing and type scale, colour-vision checked
palettes, brand files in the 'brand.yml' format, and print-ready export.
Produces output matching the 'hairline' Python package.

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
