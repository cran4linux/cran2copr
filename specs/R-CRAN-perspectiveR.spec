%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  perspectiveR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Pivot Tables and Visualizations with 'Perspective'

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets >= 1.6.0
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-htmlwidgets >= 1.6.0
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 

%description
An 'htmlwidgets' binding for the 'FINOS Perspective'
<https://perspective-dev.github.io/> library, a high-performance
'WebAssembly'-powered data visualization engine. Provides interactive
pivot tables, cross-tabulations, and multiple chart types (bar, line,
scatter, heatmap, and more) that run entirely in the browser. Supports
self-service analytics with drag-and-drop column selection,
group-by/split-by pivoting, filtering, sorting, aggregation, and computed
expressions. Works in 'RStudio' Viewer, 'R Markdown', 'Quarto', and
'Shiny' with streaming data updates via proxy interface.

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
