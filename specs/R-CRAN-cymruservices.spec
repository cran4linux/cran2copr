%global __brp_check_rpaths %{nil}
%global packname  cymruservices
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}%{?buildtag}
Summary:          Query 'Team Cymru' 'IP' Address, Autonomous System Number('ASN'), Border Gateway Protocol ('BGP'), Bogon and 'Malware'Hash Data Services

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-pingr 
Requires:         R-utils 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-pingr 

%description
A toolkit for querying 'Team Cymru' <http://team-cymru.org> 'IP' address,
Autonomous System Number ('ASN'), Border Gateway Protocol ('BGP'), Bogon
and 'Malware' Hash Data Services.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
