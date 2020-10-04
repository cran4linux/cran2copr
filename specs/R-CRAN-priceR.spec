%global packname  priceR
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Economics and Pricing Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gsubfn 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gsubfn 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-stringi 

%description
Functions to aid in micro and macro economic analysis and handling of
price and currency data. Includes extraction of relevant inflation and
exchange rate data from World Bank API, data cleaning/parsing, and
standardisation. Inflation adjustment calculations as found in Principles
of Macroeconomics by Gregory Mankiw et al (2014). Current and historical
end of day exchange rates for 171 currencies from the European Central
Bank Statistical Data Warehouse (2020)
<https://sdw.ecb.europa.eu/curConverter.do>.

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
