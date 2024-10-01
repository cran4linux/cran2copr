%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MethodOpt
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced Method Optimization for Spectra-Generating Sampling and Analysis Instrumentation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats >= 4.3.2
BuildRequires:    R-CRAN-gtools >= 3.9.5
BuildRequires:    R-CRAN-ggplot2 >= 3.4.4
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-shinyalert >= 3.0.0
BuildRequires:    R-CRAN-FrF2 >= 2.3.3
BuildRequires:    R-CRAN-zip >= 2.3.0
BuildRequires:    R-CRAN-shinyjs >= 2.1.0
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-zoo >= 1.8.12
BuildRequires:    R-CRAN-shiny >= 1.7.5.1
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-dplyr >= 1.1.3
BuildRequires:    R-CRAN-rlang >= 1.1.2
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-shinyBS >= 0.61.1
BuildRequires:    R-CRAN-htmltools >= 0.5.8.1
BuildRequires:    R-CRAN-shinyFeedback >= 0.4.0
BuildRequires:    R-CRAN-DT >= 0.30
BuildRequires:    R-CRAN-DoE.wrapper >= 0.12
Requires:         R-stats >= 4.3.2
Requires:         R-CRAN-gtools >= 3.9.5
Requires:         R-CRAN-ggplot2 >= 3.4.4
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-shinyalert >= 3.0.0
Requires:         R-CRAN-FrF2 >= 2.3.3
Requires:         R-CRAN-zip >= 2.3.0
Requires:         R-CRAN-shinyjs >= 2.1.0
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-zoo >= 1.8.12
Requires:         R-CRAN-shiny >= 1.7.5.1
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-dplyr >= 1.1.3
Requires:         R-CRAN-rlang >= 1.1.2
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-shinyBS >= 0.61.1
Requires:         R-CRAN-htmltools >= 0.5.8.1
Requires:         R-CRAN-shinyFeedback >= 0.4.0
Requires:         R-CRAN-DT >= 0.30
Requires:         R-CRAN-DoE.wrapper >= 0.12

%description
A graphical user interface to apply an advanced method optimization
algorithm to various sampling and analysis instruments. This includes
generating experimental designs, uploading and viewing data, and
performing various analyses to determine the optimal method. Details of
the techniques used in this package are published in Gamble, Granger, &
Mannion (2024) <doi:10.1021/acs.analchem.3c05763>.

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
