%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  termr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Modern Reactive Terminal Applications with Data Workflows

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-ps 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-codetools 
Requires:         R-grDevices 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-ps 
Requires:         R-stats 
Requires:         R-utils 

%description
Build modern reactive terminal applications for data workflows in R using
reusable widgets, layouts, events, focus management and themes. A virtual
screen buffer and incremental rendering update changed cells, while a
headless driver supports deterministic application tests. Includes data
tables that render visible rows on demand, lazy table sources, data
inspection, SQL editing and background R workers with progress and
streamed output. Optional database support and static text, Markdown,
HTML, SVG and JSON exports support analytical tools and reports without
requiring an interactive terminal for static output.

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
