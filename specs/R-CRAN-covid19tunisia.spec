%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  covid19tunisia
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cases of COVID-19 in Tunisia

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-knitr >= 1.7
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-glue >= 1.3.2
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-tidyr >= 1.0.2
BuildRequires:    R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-knitr >= 1.7
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-glue >= 1.3.2
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-tidyr >= 1.0.2
Requires:         R-CRAN-dplyr >= 0.8.5

%description
Data personally collected about the spread of COVID-19 (SARS-COV-2) in
Tunisia <https://github.com/MounaBelaid/covid19datatunisia>.

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
