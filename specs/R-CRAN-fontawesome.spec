%global packname  fontawesome
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Work with 'Font Awesome' Icons

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.4
BuildRequires:    R-CRAN-pointblank >= 0.6.0
BuildRequires:    R-CRAN-htmltools >= 0.5.1.1
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-dplyr >= 1.0.4
Requires:         R-CRAN-pointblank >= 0.6.0
Requires:         R-CRAN-htmltools >= 0.5.1.1
Requires:         R-CRAN-magrittr 

%description
Easily and flexibly insert 'Font Awesome' icons into 'R Markdown'
documents and 'Shiny' apps. These icons can be inserted into HTML content
through inline 'SVG' tags or 'i' tags. There is also a utility function
for exporting 'Font Awesome' icons as 'PNG' images for those situations
where raster graphics are needed.

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
