%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggimage
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Use Image in 'ggplot2'

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yulab.utils >= 0.1.3
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-ggfun 
BuildRequires:    R-CRAN-ggiraph 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-yulab.utils >= 0.1.3
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-ggfun 
Requires:         R-CRAN-ggiraph 
Requires:         R-CRAN-ggplotify 
Requires:         R-grid 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magick 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Supports image files and graphic objects to be visualized in 'ggplot2'
graphic system.

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
