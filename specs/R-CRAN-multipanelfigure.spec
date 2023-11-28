%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multipanelfigure
%global packver   2.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Infrastructure to Assemble Multi-Panel Figures (from Grobs)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-magick >= 1.9
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringi >= 1.2.3
BuildRequires:    R-CRAN-gridGraphics >= 0.3.0
BuildRequires:    R-CRAN-gtable >= 0.2.0
BuildRequires:    R-CRAN-assertive.base >= 0.0.7
BuildRequires:    R-CRAN-assertive.files >= 0.0.2
BuildRequires:    R-CRAN-assertive.numbers >= 0.0.2
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-magick >= 1.9
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringi >= 1.2.3
Requires:         R-CRAN-gridGraphics >= 0.3.0
Requires:         R-CRAN-gtable >= 0.2.0
Requires:         R-CRAN-assertive.base >= 0.0.7
Requires:         R-CRAN-assertive.files >= 0.0.2
Requires:         R-CRAN-assertive.numbers >= 0.0.2
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools to create a layout for figures made of multiple panels, and to fill
the panels with base, 'lattice', 'ggplot2' and 'ComplexHeatmap' plots,
grobs, as well as content from all image formats supported by
'ImageMagick' (accessed through 'magick').

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
