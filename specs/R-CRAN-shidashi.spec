%global __brp_check_rpaths %{nil}
%global packname  shidashi
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Shiny Dashboard Template System

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml >= 2.2.1
BuildRequires:    R-CRAN-jsonlite >= 1.7.2
BuildRequires:    R-CRAN-shiny >= 1.7.0
BuildRequires:    R-CRAN-httr >= 1.4.2
BuildRequires:    R-CRAN-formatR >= 1.11
BuildRequires:    R-CRAN-fastmap >= 1.1.0
BuildRequires:    R-CRAN-digest >= 0.6.27
Requires:         R-CRAN-yaml >= 2.2.1
Requires:         R-CRAN-jsonlite >= 1.7.2
Requires:         R-CRAN-shiny >= 1.7.0
Requires:         R-CRAN-httr >= 1.4.2
Requires:         R-CRAN-formatR >= 1.11
Requires:         R-CRAN-fastmap >= 1.1.0
Requires:         R-CRAN-digest >= 0.6.27

%description
A template system based on 'AdminLTE3' (<https://adminlte.io/themes/v3/>)
theme. Comes with default theme that can be easily customized. Developers
can upload modified templates on 'Github', and users can easily download
templates with 'RStudio' project wizard. The key features of the default
template include light and dark theme switcher, resizing graphs,
synchronizing inputs across sessions, new notification system, fancy
progress bars, and card-like flip panels with back sides, as well as
various of 'HTML' tool widgets.

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
