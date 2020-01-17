%global packname  noctua
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          Connect to 'AWS Athena' using R 'AWS SDK' 'paws' ('DBI'Interface)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI >= 0.7
BuildRequires:    R-CRAN-paws >= 0.1.5
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-DBI >= 0.7
Requires:         R-CRAN-paws >= 0.1.5
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Designed to be compatible with the 'R' package 'DBI' (Database Interface)
when connecting to Amazon Web Service ('AWS') Athena
<https://aws.amazon.com/athena/>. To do this the 'R' 'AWS' Software
Development Kit ('SDK') 'paws' <https://github.com/paws-r/paws> is used as
a driver.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/icons
%{rlibdir}/%{packname}/INDEX
