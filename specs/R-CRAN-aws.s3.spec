%global packname  aws.s3
%global packver   0.3.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.21
Release:          3%{?dist}
Summary:          'AWS S3' Client Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-aws.signature >= 0.3.7
BuildRequires:    R-CRAN-xml2 > 1.0.0
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-aws.signature >= 0.3.7
Requires:         R-CRAN-xml2 > 1.0.0
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-digest 

%description
A simple client package for the Amazon Web Services ('AWS') Simple Storage
Service ('S3') 'REST' 'API' <https://aws.amazon.com/s3/>.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/experiments
%{rlibdir}/%{packname}/INDEX
