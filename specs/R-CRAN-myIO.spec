%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  myIO
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Data Visualizations Using 'd3.js'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 

%description
Create interactive 'd3.js' visualizations from R with built-in statistical
transforms. Computes confidence intervals, regression fits, LOESS
smoothing, moving averages, error bars, and uncertainty visualizations
(quantile dot plots and fan charts) in R and renders them as composable
chart layers via 'htmlwidgets'. Supports 36 chart types including
boxplots, violin plots, Q-Q diagnostic plots, calendar heatmaps, survival
curves, and group comparisons with pairwise significance testing. Also
provides a machine-readable chart specification schema with validators so
that large language model agents can author and verify charts. Works in
'RStudio', 'Shiny', and 'R Markdown'.

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
