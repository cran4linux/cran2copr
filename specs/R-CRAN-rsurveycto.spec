%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rsurveycto
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Interact with Data on 'SurveyCTO'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 5.2.1
BuildRequires:    R-CRAN-cli >= 3.6.3
BuildRequires:    R-CRAN-withr >= 3.0.1
BuildRequires:    R-CRAN-checkmate >= 2.3.2
BuildRequires:    R-CRAN-jsonlite >= 1.8.8
BuildRequires:    R-CRAN-glue >= 1.7.0
BuildRequires:    R-CRAN-httr >= 1.4.7
BuildRequires:    R-CRAN-readxl >= 1.4.3
BuildRequires:    R-CRAN-data.table >= 1.15.4
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-lifecycle >= 1.0.4
BuildRequires:    R-CRAN-vctrs >= 0.6.5
Requires:         R-CRAN-curl >= 5.2.1
Requires:         R-CRAN-cli >= 3.6.3
Requires:         R-CRAN-withr >= 3.0.1
Requires:         R-CRAN-checkmate >= 2.3.2
Requires:         R-CRAN-jsonlite >= 1.8.8
Requires:         R-CRAN-glue >= 1.7.0
Requires:         R-CRAN-httr >= 1.4.7
Requires:         R-CRAN-readxl >= 1.4.3
Requires:         R-CRAN-data.table >= 1.15.4
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-lifecycle >= 1.0.4
Requires:         R-CRAN-vctrs >= 0.6.5

%description
'SurveyCTO' is a platform for mobile data collection in offline settings.
The 'rsurveycto' R package uses the 'SurveyCTO' REST API
<https://docs.surveycto.com/05-exporting-and-publishing-data/05-api-access/01.api-access.html>
to read datasets and forms from a 'SurveyCTO' server into R as
'data.table's and to download file attachments. The package also has
limited support to write datasets to a server.

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
