%global packname  RDocumentation
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          3%{?dist}
Summary:          Integrate R with 'RDocumentation'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-proto >= 0.3.10
BuildRequires:    R-CRAN-rjson >= 0.2.15
BuildRequires:    R-utils 
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-proto >= 0.3.10
Requires:         R-CRAN-rjson >= 0.2.15
Requires:         R-utils 

%description
Wraps around the default help functionality in R. Instead of plain
documentation files, documentation will show up as it does on
<https://www.rdocumentation.org>, a platform that shows R documentation
from 'CRAN', 'GitHub' and 'Bioconductor', together with informative stats
to assess the package quality.

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
%{rlibdir}/%{packname}/INDEX
