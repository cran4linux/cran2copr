%global packname  AzureCognitive
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Interface to Azure Cognitive Services

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.3
BuildRequires:    R-CRAN-AzureAuth >= 1.2.0
BuildRequires:    R-CRAN-AzureRMR 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-httr >= 1.3
Requires:         R-CRAN-AzureAuth >= 1.2.0
Requires:         R-CRAN-AzureRMR 
Requires:         R-CRAN-jsonlite 

%description
An interface to Azure Cognitive Services
<https://docs.microsoft.com/azure/cognitive-services/welcome>. Both an
'Azure Resource Manager' interface, for deploying Cognitive Services
resources, and a client framework are supplied. While 'AzureCognitive' can
be called by the end-user, it is meant to provide a foundation for other
packages that will support specific services, like Computer Vision, Custom
Vision, language translation, and so on. Part of the 'AzureR' family of
packages.

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
