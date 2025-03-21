%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MHQoL
%global packver   0.14.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mental Health Quality of Life Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shinyalert >= 3.1.0
BuildRequires:    R-CRAN-writexl >= 1.5.1
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-shiny >= 1.0.0
BuildRequires:    R-CRAN-fmsb >= 0.7.6
BuildRequires:    R-CRAN-DT >= 0.33
BuildRequires:    R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-shinyalert >= 3.1.0
Requires:         R-CRAN-writexl >= 1.5.1
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-shiny >= 1.0.0
Requires:         R-CRAN-fmsb >= 0.7.6
Requires:         R-CRAN-DT >= 0.33
Requires:         R-CRAN-assertthat >= 0.2.1

%description
Transforms, calculates, and presents results from the Mental Health
Quality of Life Questionnaire (MHQoL), a measure of health-related quality
of life for individuals with mental health conditions. Provides scoring
functions, summary statistics, and visualization tools to facilitate
interpretation. For more details see van Krugten et al.(2022)
<doi:10.1007/s11136-021-02935-w>.

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
