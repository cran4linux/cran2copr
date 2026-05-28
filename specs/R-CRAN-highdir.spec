%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  highdir
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Backend-Agnostic Figure Builder for 'highcharter' and 'ggplot2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-jsonlite >= 1.8.0
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-htmlwidgets >= 1.6.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-highcharter >= 0.9.4
BuildRequires:    R-CRAN-viridis >= 0.6.0
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-jsonlite >= 1.8.0
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-htmlwidgets >= 1.6.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-highcharter >= 0.9.4
Requires:         R-CRAN-viridis >= 0.6.0
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-stats 

%description
Provides a backend-agnostic 'API' for creating data visualizations using
'highcharter' (interactive) or 'ggplot2' (static). Figures are defined
once via a specification object and can be rendered to either backend
without modifying the calling code. Supports both declarative and layered
workflows, flexible theming and colour palettes, optional 'JavaScript'
enhancements, and tools for exporting figures and interactive exploration
via a 'shiny' app.

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
