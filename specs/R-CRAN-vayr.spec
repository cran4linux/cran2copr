%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vayr
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extensions for 'ggplot2' to Visualize as You Randomize

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-withr >= 2.1.1
BuildRequires:    R-CRAN-packcircles >= 0.3.7
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-withr >= 2.1.1
Requires:         R-CRAN-packcircles >= 0.3.7

%description
Extensions for 'ggplot2' that implement the "visualize as you randomize"
principles of Coppock (2021) <doi:10.1017/9781108777919.022>, which can be
especially useful when plotting experimental data. Provides position
adjustments that arrange over-plotted points so that a statistical model
can be shown in data-space, and a helper for graphing extreme value bounds
when an experiment encounters attrition.

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
