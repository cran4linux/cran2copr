%global __brp_check_rpaths %{nil}
%global packname  AWR.KMS
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          A Simple Client to the 'AWS' Key Management Service

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-AWR 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-AWR 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-jsonlite 

%description
Encrypt plain text and 'decrypt' cipher text using encryption keys hosted
at Amazon Web Services ('AWS') Key Management Service ('KMS'), on which
see <https://aws.amazon.com/kms> for more information.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
