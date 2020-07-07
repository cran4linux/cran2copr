%global packname  clifro
%global packver   3.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.2
Release:          3%{?dist}
Summary:          Easily Download and Visualise Climate Data from CliFlo

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-methods 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RCurl 
Requires:         R-utils 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reshape2 

%description
CliFlo is a web portal to the New Zealand National Climate Database and
provides public access (via subscription) to around 6,500 various climate
stations (see <https://cliflo.niwa.co.nz/> for more information).
Collating and manipulating data from CliFlo (hence clifro) and importing
into R for further analysis, exploration and visualisation is now
straightforward and coherent. The user is required to have an internet
connection, and a current CliFlo subscription (free) if data from
stations, other than the public Reefton electronic weather station, is
sought.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
