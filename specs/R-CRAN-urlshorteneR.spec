%global packname  urlshorteneR
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Wrapper for the 'Bit.ly' and 'Is.gd'/'v.gd' URL Shortening Services

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 2.0.2
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-jsonlite >= 1.7.0
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-httr >= 1.4.2
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-clipr >= 0.7.0
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-CRAN-miniUI >= 0.1.1.1
Requires:         R-CRAN-cli >= 2.0.2
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-jsonlite >= 1.7.0
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-httr >= 1.4.2
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-clipr >= 0.7.0
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-miniUI >= 0.1.1.1

%description
Allows using two URL shortening services, which also provide expanding and
analytic functions. Specifically developed for 'Bit.ly' (which requires
OAuth2) and 'is.gd' (no API key).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
