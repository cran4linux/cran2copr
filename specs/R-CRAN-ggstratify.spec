%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggstratify
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Stratified Descriptive Figures with a Point-and-Click GUI

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-survey >= 4.5
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-survival >= 3.2.0
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-patchwork >= 1.1.0
BuildRequires:    R-CRAN-bslib >= 0.5.0
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ragg 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-survey >= 4.5
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-survival >= 3.2.0
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-patchwork >= 1.1.0
Requires:         R-CRAN-bslib >= 0.5.0
Requires:         R-grDevices 
Requires:         R-CRAN-ragg 
Requires:         R-stats 
Requires:         R-utils 

%description
A point-and-click 'shiny' interface for the descriptive analysis that
comes before any model is chosen. Pass a data frame, pick the variable to
describe, and add the layers you want to see it within: a second variable
becomes the panels of a 'ggplot2' facet_wrap(), and further variables
become separate figures, one file each, taken either one variable at a
time or crossed. Every stratum is reported with the number of observations
behind it, on the figure and on each of its panels; strata that contain
none are listed rather than dropped, and rows with a missing value in a
layer variable are excluded and counted. A continuous variable can be
categorized into quantile groups, equal-width bins or user-supplied cut
points, a variable of any type can be turned into whether it is missing or
observed, so that the rows a layer would exclude become a stratum of their
own, and a date or date-time variable can be read at a chosen resolution,
either as a calendar period or as a position in the yearly cycle such as
the month or the season; any of them can then be used as a layer. The
figure types follow those offered by the 'ggplotgui' package and add the
line plot for change over time, an optional LOWESS smoother, and the
Kaplan-Meier curve estimated by 'survival', with an optional
number-at-risk table. An error bar can show a standard error or a
confidence interval, the latter from the t distribution for a mean and
from the Clopper-Pearson or Wilson method for a proportion, and the points
can be joined by a line computed from the same summary, which is how a
trend over time is read. A survey weight can be set: the figure is then
drawn from the weighted data, every count is reported both as rows and as
the sum of the weights, and error bars and confidence bands are
design-based estimates from the 'survey' package. Columns are described as
they are typed, so convert each to the type you mean first. Figures are
written as PNG or SVG, and the application prints the 'ggplot2' code
behind the figure on screen, so that a description can be repeated, shared
or accounted for later. Everything runs locally, with no network access
and no AI involved.

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
