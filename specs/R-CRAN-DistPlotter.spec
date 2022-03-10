%global __brp_check_rpaths %{nil}
%global packname  DistPlotter
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Graphical User Interface for Plotting Common Univariate Distributions

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-shinyalert >= 3.0.0
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-extraDistr >= 1.9.1
BuildRequires:    R-CRAN-stringi >= 1.7.6
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-colourpicker >= 1.1.1
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.8
BuildRequires:    R-CRAN-shinyBS >= 0.61
BuildRequires:    R-CRAN-shinyWidgets >= 0.6.4
BuildRequires:    R-CRAN-rio >= 0.5.29
BuildRequires:    R-CRAN-DT >= 0.20
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-shinyalert >= 3.0.0
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-extraDistr >= 1.9.1
Requires:         R-CRAN-stringi >= 1.7.6
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-colourpicker >= 1.1.1
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.8
Requires:         R-CRAN-shinyBS >= 0.61
Requires:         R-CRAN-shinyWidgets >= 0.6.4
Requires:         R-CRAN-rio >= 0.5.29
Requires:         R-CRAN-DT >= 0.20

%description
Package including an interactive Shiny application for plotting common
univariate distributions.

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
