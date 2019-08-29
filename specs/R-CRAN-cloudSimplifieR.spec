%global packname  cloudSimplifieR
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}
Summary:          Fetch Data from Amazon AWS

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-aws.s3 
BuildRequires:    R-CRAN-aws.signature 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-aws.s3 
Requires:         R-CRAN-aws.signature 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-readr 

%description
Simple helper functions to fetch and read data from various formats stored
on Amazon AWS S3 Buckets <https://aws.amazon.com/s3/> . Most functions are
essentially wrapping over cloudyR <https://cloudyr.github.io/> which is a
project and group of packages which provide easier cloud computing
solutions for R.

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
%{rlibdir}/%{packname}/INDEX
