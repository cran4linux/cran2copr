%global packname  AzureKeyVault
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Key and Secret Management in 'Azure'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-AzureAuth >= 1.0.1
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-jose 
BuildRequires:    R-CRAN-AzureRMR 
BuildRequires:    R-CRAN-AzureGraph 
Requires:         R-CRAN-AzureAuth >= 1.0.1
Requires:         R-utils 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-jose 
Requires:         R-CRAN-AzureRMR 
Requires:         R-CRAN-AzureGraph 

%description
Manage keys, certificates, secrets, and storage accounts in Microsoft's
'Key Vault' service: <https://azure.microsoft.com/services/key-vault>.
Provides facilities to store and retrieve secrets, use keys to encrypt,
decrypt, sign and verify data, and manage certificates. Integrates with
the 'AzureAuth' package to enable authentication with a certificate, and
with the 'openssl' package for importing and exporting cryptographic
objects. Part of the 'AzureR' family of packages.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
