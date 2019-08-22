%global packname  algorithmia
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Allows you to Easily Interact with the Algorithmia Platform

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-methods >= 2.5.0
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rjson 
Requires:         R-methods >= 2.5.0
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rjson 

%description
The company, Algorithmia, houses the largest marketplace of online
algorithms. This package essentially holds a bunch of REST wrappers that
make it very easy to call algorithms in the Algorithmia platform and
access files and directories in the Algorithmia data API. To learn more
about the services they offer and the algorithms in the platform visit
<http://algorithmia.com>. More information for developers can be found at
<http://developers.algorithmia.com>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
