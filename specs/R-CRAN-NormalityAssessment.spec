%global __brp_check_rpaths %{nil}
%global packname  NormalityAssessment
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Graphical User Interface for Testing Normality Visually

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-shinyalert >= 2.0.0
BuildRequires:    R-CRAN-stringi >= 1.7.4
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-shinyBS >= 0.61
BuildRequires:    R-CRAN-rio >= 0.5.27
BuildRequires:    R-CRAN-DT >= 0.19
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-shinyalert >= 2.0.0
Requires:         R-CRAN-stringi >= 1.7.4
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-shinyBS >= 0.61
Requires:         R-CRAN-rio >= 0.5.27
Requires:         R-CRAN-DT >= 0.19

%description
Package including an interactive Shiny application for testing normality
visually.

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
