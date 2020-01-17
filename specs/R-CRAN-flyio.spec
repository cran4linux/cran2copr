%global packname  flyio
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Read or Write any Format from Anywhere

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-googleCloudStorageR 
BuildRequires:    R-CRAN-aws.s3 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-googleCloudStorageR 
Requires:         R-CRAN-aws.s3 
Requires:         R-utils 
Requires:         R-tools 

%description
Perform input, output of files in R from data sources like Google Cloud
Storage ('GCS') <https://cloud.google.com/storage/>, Amazon Web Services
('AWS S3') <https://aws.amazon.com/s3> or local drive.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
