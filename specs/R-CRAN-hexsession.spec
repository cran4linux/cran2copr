%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hexsession
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create a Tile of Logos for Loaded Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-chromote 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-chromote 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-htmltools 

%description
Creates a responsive HTML file with tiled hexagonal logos for packages in
an R session. Tiles can be also be generated for a custom set of packages
specified with a character vector. Output can be saved as a static
screenshot in PNG format using a headless browser.

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
