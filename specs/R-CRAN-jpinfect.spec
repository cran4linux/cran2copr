%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jpinfect
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Acquiring and Processing Data from Japan Institute for Health Security

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.4.3
BuildRequires:    R-CRAN-readr >= 2.1.5
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-stringi >= 1.8.7
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-readxl >= 1.4.5
BuildRequires:    R-CRAN-future >= 1.34.0
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-tidyselect >= 1.2.1
BuildRequires:    R-CRAN-future.apply >= 1.11.3
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-ISOweek >= 0.6.2
BuildRequires:    R-utils 
Requires:         R-stats >= 4.4.3
Requires:         R-CRAN-readr >= 2.1.5
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-stringi >= 1.8.7
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-readxl >= 1.4.5
Requires:         R-CRAN-future >= 1.34.0
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-tidyselect >= 1.2.1
Requires:         R-CRAN-future.apply >= 1.11.3
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-ISOweek >= 0.6.2
Requires:         R-utils 

%description
Download and post process the infectious disease case data from Japan
Institute for Health Security. Also the package included ready-to-analyse
datasets. See the data source website for further details
<https://id-info.jihs.go.jp/>.

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
