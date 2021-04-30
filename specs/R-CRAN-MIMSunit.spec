%global packname  MIMSunit
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          1%{?dist}%{?buildtag}
Summary:          Algorithm to Compute Monitor Independent Movement Summary Unit (MIMS-Unit)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-utils >= 3.6.1
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-tibble >= 3.0.4
BuildRequires:    R-CRAN-R.utils >= 2.7.0
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-shiny >= 1.4.0.2
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-caTools >= 1.17.1.1
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-dygraphs >= 1.1.1.6
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-matlab >= 1.0.2
BuildRequires:    R-CRAN-dplyr >= 0.7.7
BuildRequires:    R-CRAN-signal >= 0.7.6
BuildRequires:    R-CRAN-xts >= 0.11.2
Requires:         R-utils >= 3.6.1
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-tibble >= 3.0.4
Requires:         R-CRAN-R.utils >= 2.7.0
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-shiny >= 1.4.0.2
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-caTools >= 1.17.1.1
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-dygraphs >= 1.1.1.6
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-matlab >= 1.0.2
Requires:         R-CRAN-dplyr >= 0.7.7
Requires:         R-CRAN-signal >= 0.7.6
Requires:         R-CRAN-xts >= 0.11.2

%description
The MIMS-unit algorithm is developed to compute Monitor Independent
Movement Summary Unit, a measurement to summarize raw accelerometer data
while ensuring harmonized results across different devices. It also
includes scripts to reproduce results in the related publication (John,
D., Tang. Q., Albinali, F. and Intille, S. (2019)
<doi:10.1123/jmpb.2018-0068>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
