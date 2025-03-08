%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  visae
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization of Adverse Events

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-shiny >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-shinyjs >= 1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-ggrepel >= 0.8.2
BuildRequires:    R-CRAN-ca >= 0.71
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-DT >= 0.13
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-shiny >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-shinyjs >= 1.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-ggrepel >= 0.8.2
Requires:         R-CRAN-ca >= 0.71
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-DT >= 0.13

%description
Implementation of 'shiny' app to visualize adverse events based on the
Common Terminology Criteria for Adverse Events (CTCAE) using stacked
correspondence analysis as described in Diniz et. al
(2021)<doi:10.1186/s12874-021-01368-w>.

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
