%global packname  cyclestreets
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}
Summary:          Cycle Routing and Data for Cycling Advocacy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-stringr 

%description
An interface to the cycle routing/data services provided by
'CycleStreets', a not-for-profit social enterprise and advocacy
organisation. The application programming interfaces (APIs) provided by
'CycleStreets' are documented at (<https://www.cyclestreets.net/api/>).
The focus of this package is the journey planning API, which aims to
emulate the routes taken by a knowledgeable cyclist. An innovative feature
of the routing service of its provision of fastest, quietest and balanced
profiles. These represent routes taken to minimise time, avoid traffic and
compromise between the two, respectively.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
