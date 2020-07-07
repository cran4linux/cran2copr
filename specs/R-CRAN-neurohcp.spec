%global packname  neurohcp
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          3%{?dist}
Summary:          Human 'Connectome' Project Interface

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 >= 1.0.1
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-xml2 >= 1.0.1
Requires:         R-CRAN-digest 
Requires:         R-CRAN-httr 
Requires:         R-utils 
Requires:         R-CRAN-base64enc 

%description
Downloads and reads data from Human 'Connectome' Project
<https://db.humanconnectome.org> using Amazon Web Services ('AWS') 'S3'
buckets.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
