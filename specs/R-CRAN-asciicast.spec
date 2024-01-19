%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  asciicast
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Create 'Ascii' Screen Casts from R Scripts

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-processx >= 3.7.0
BuildRequires:    R-CRAN-cli >= 3.3.0.9000
BuildRequires:    R-CRAN-magick >= 2.2.9002
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-processx >= 3.7.0
Requires:         R-CRAN-cli >= 3.3.0.9000
Requires:         R-CRAN-magick >= 2.2.9002
Requires:         R-CRAN-curl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-V8 
Requires:         R-CRAN-withr 

%description
Record 'asciicast' screen casts from R scripts. Convert them to animated
SVG images, to be used in 'README' files, or blog posts. Includes
'asciinema-player' as an 'HTML' widget, and an 'asciicast' 'knitr' engine,
to embed 'ascii' screen casts in 'Rmarkdown' documents.

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
