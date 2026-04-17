%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  munch
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Rich Inline Text for 'grid' Graphics and 'flextable'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-commonmark 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-gdtools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-systemfonts 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-commonmark 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-gdtools 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-CRAN-systemfonts 
Requires:         R-CRAN-xml2 

%description
Renders rich inline text (bold, italic, code, links, images) in grid
graphics and 'ggplot2', from markdown or 'flextable' chunks. Provides
grobs, theme elements, and geometry layers for styled text rendering. Only
works with graphics devices that support 'systemfonts', such as those
provided by 'ragg', 'svglite', or 'ggiraph'. The 'cairo_pdf' device is
also supported when fonts are installed at the system level.

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
