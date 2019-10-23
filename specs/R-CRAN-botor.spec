%global packname  botor
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          'AWS Python SDK' ('boto3') for R

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-logger 
Requires:         R-utils 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-logger 

%description
Fork-safe, raw access to the 'Amazon Web Services' ('AWS') 'SDK' via the
'boto3' 'Python' module, and convenient helper functions to query the
'Simple Storage Service' ('S3') and 'Key Management Service' ('KMS'),
partial support for 'IAM', the 'Systems Manager Parameter Store' and
'Secrets Manager'.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
