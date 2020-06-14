%global packname  distill
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          2%{?dist}
Summary:          'R Markdown' Format for Scientific and Technical Writing

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.3
BuildRequires:    R-CRAN-knitr >= 1.15
BuildRequires:    R-CRAN-rmarkdown >= 1.10
BuildRequires:    R-CRAN-bookdown >= 0.8
BuildRequires:    R-CRAN-xfun >= 0.2
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-downloader 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-openssl 
Requires:         R-CRAN-jsonlite >= 1.3
Requires:         R-CRAN-knitr >= 1.15
Requires:         R-CRAN-rmarkdown >= 1.10
Requires:         R-CRAN-bookdown >= 0.8
Requires:         R-CRAN-xfun >= 0.2
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-png 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-rprojroot 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-downloader 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-openssl 

%description
Scientific and technical article format for the web. 'Distill' articles
feature attractive, reader-friendly typography, flexible layout options
for visualizations, and full support for footnotes and citations.

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
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/rmarkdown
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
