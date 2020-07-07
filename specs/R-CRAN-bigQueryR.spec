%global packname  bigQueryR
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}
Summary:          Interface with Google BigQuery with Shiny Compatibility

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-googleAuthR >= 1.1.1
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-CRAN-googleCloudStorageR >= 0.2.0
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-googleAuthR >= 1.1.1
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-CRAN-googleCloudStorageR >= 0.2.0
Requires:         R-CRAN-assertthat 

%description
Interface with 'Google BigQuery', see <https://cloud.google.com/bigquery/>
for more information. This package uses 'googleAuthR' so is compatible
with similar packages, including 'Google Cloud Storage'
(<https://cloud.google.com/storage/>) for result extracts.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/client.json
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
