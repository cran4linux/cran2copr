%global packname  steemr
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          A Tool for Processing Steem Data

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-openair 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-RODBC 
BuildRequires:    R-CRAN-VennDiagram 
BuildRequires:    R-CRAN-beginr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-blogdown 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-mongolite 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-htmltab 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-openair 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-RODBC 
Requires:         R-CRAN-VennDiagram 
Requires:         R-CRAN-beginr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-blogdown 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-mongolite 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-htmltab 

%description
Steem is a blockchain-based social media platform (see
<https://en.wikipedia.org/wiki/Steemit>). The Steem social activity data
are saved in the Steem blockchain, the SteemDB database, the SteemSQL
database, and so on. 'steemr' is an R package that downloads the Steem
data from the SteemDB and SteemSQL servers, re-organizes the data in a
user-friendly way, and visualizes the data for further analysis.

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

%files
%{rlibdir}/%{packname}
