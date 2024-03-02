%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pvda
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Disproportionality Functions for Pharmacovigilance

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats >= 4.1.3
BuildRequires:    R-utils >= 4.1.3
BuildRequires:    R-CRAN-cli >= 3.4.1
BuildRequires:    R-CRAN-tibble >= 3.1.8
BuildRequires:    R-CRAN-Rdpack >= 2.4
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dtplyr >= 1.2.2
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.14.6
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-purrr >= 0.3.5
Requires:         R-stats >= 4.1.3
Requires:         R-utils >= 4.1.3
Requires:         R-CRAN-cli >= 3.4.1
Requires:         R-CRAN-tibble >= 3.1.8
Requires:         R-CRAN-Rdpack >= 2.4
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dtplyr >= 1.2.2
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-data.table >= 1.14.6
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-purrr >= 0.3.5

%description
Tools for performing disproportionality analysis using the information
component, proportional reporting rate and the reporting odds ratio. The
anticipated use is passing data to the da() function, which executes the
disproportionality analysis. See Norén et al (2011)
<doi:10.1177/0962280211403604> and Montastruc et al (2011)
<doi:10.1111/j.1365-2125.2011.04037.x> for further details.

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
