%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glasstabs
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Animated Glass-Style Tabs and Multi-Select Filter for 'Shiny'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-htmltools >= 0.5.0
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-htmltools >= 0.5.0

%description
Tools for creating animated glassmorphism-style tab navigation and select
filter widgets in 'Shiny' applications. Provides a tab navigation
component with a sliding glass halo animation, a searchable multi-select
dropdown, and a single-select dropdown - all with multiple colour themes
and server-side update helpers. Tabs support icons, numeric badges,
disable/enable toggling, runtime append/remove, reactive rendering via
'renderGlassTabs()', URL bookmarking, and compact mode for dashboard card
layouts. 'glassTabCondition()' generates 'conditionalPanel()' condition
strings without needing to recall the internal input key pattern.
'glasstabs_news()' displays the release notes from the R console. Built-in
example apps can be launched with 'runGlassExample()'.  All widgets are
compatible with standard 'Shiny' layouts and 'bs4Dash' dashboards and
'bslib' themed applications.  For full documentation and examples see
Arthur (2026) <https://prigasg.github.io/glasstabs/>.

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
