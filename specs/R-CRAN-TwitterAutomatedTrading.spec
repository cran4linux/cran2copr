%global packname  TwitterAutomatedTrading
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Automated Trading Using Tweets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-twitteR 
BuildRequires:    R-CRAN-naptime 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-twitteR 
Requires:         R-CRAN-naptime 
Requires:         R-utils 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-magrittr 

%description
Provides an integration to the 'metatrader 5'. The functionalities carry
out automated trading using sentiment indexes computed from 'twitter'
and/or 'stockwits'. The sentiment indexes are based on the ph.d.
dissertation "Essays on Economic Forecasting Models" (Godeiro,2018)
<https://repositorio.ufpb.br/jspui/handle/123456789/15198> The integration
between the 'R' and the 'metatrader 5' allows sending buy/sell orders to
the brokerage.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/EA
%{rlibdir}/%{packname}/INDEX
