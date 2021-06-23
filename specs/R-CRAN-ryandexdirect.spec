%global __brp_check_rpaths %{nil}
%global packname  ryandexdirect
%global packver   3.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6.0
Release:          3%{?dist}%{?buildtag}
Summary:          Load Data From 'Yandex Direct'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 

%description
Load data from 'Yandex Direct' API V5
<https://tech.yandex.ru/direct/doc/dg/concepts/about-docpage/> into R.
Provide function for load lists of campaings, ads, keywords and other
objects from 'Yandex Direct' account. Also you can load statistic from API
'Reports Service'
<https://tech.yandex.ru/direct/doc/reports/reports-docpage/>. And allows
keyword bids management.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/logo
%{rlibdir}/%{packname}/INDEX
