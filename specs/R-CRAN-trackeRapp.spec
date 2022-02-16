%global __brp_check_rpaths %{nil}
%global packname  trackeRapp
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interface for the Analysis of Running, Cycling and Swimming Data from GPS-Enabled Tracking Devices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly >= 4.9.2
BuildRequires:    R-CRAN-V8 >= 3.0.2
BuildRequires:    R-CRAN-changepoint >= 2.2.2
BuildRequires:    R-CRAN-zoo >= 1.8.7
BuildRequires:    R-CRAN-mgcv >= 1.8.31
BuildRequires:    R-CRAN-trackeR >= 1.5.0
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-colorspace >= 1.4.1
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-shinyjs >= 1.1
BuildRequires:    R-CRAN-sf >= 0.9.2
BuildRequires:    R-CRAN-shinydashboard >= 0.7.1
BuildRequires:    R-CRAN-shinyWidgets >= 0.5.1
BuildRequires:    R-CRAN-mapdeck >= 0.3.2
BuildRequires:    R-CRAN-DT >= 0.13
Requires:         R-CRAN-plotly >= 4.9.2
Requires:         R-CRAN-V8 >= 3.0.2
Requires:         R-CRAN-changepoint >= 2.2.2
Requires:         R-CRAN-zoo >= 1.8.7
Requires:         R-CRAN-mgcv >= 1.8.31
Requires:         R-CRAN-trackeR >= 1.5.0
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-colorspace >= 1.4.1
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-shinyjs >= 1.1
Requires:         R-CRAN-sf >= 0.9.2
Requires:         R-CRAN-shinydashboard >= 0.7.1
Requires:         R-CRAN-shinyWidgets >= 0.5.1
Requires:         R-CRAN-mapdeck >= 0.3.2
Requires:         R-CRAN-DT >= 0.13

%description
Provides an integrated user interface and workflow for the analysis of
running, cycling and swimming data from GPS-enabled tracking devices
through the 'trackeR' <https://CRAN.R-project.org/package=trackeR> R
package.

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
