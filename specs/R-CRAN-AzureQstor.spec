%global packname  AzureQstor
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Interface to 'Azure Queue Storage'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-AzureStor >= 3.0.0
BuildRequires:    R-CRAN-AzureRMR >= 2.0.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-AzureStor >= 3.0.0
Requires:         R-CRAN-AzureRMR >= 2.0.0
Requires:         R-utils 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-httr 

%description
An interface to 'Azure Queue Storage'. This is a cloud service for storing
large numbers of messages, for example from automated sensors, that can be
accessed remotely via authenticated calls using HTTP or HTTPS. Queue
storage is often used to create a backlog of work to process
asynchronously. Part of the 'AzureR' family of packages.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
