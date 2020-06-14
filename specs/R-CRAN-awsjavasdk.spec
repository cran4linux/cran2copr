%global packname  awsjavasdk
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Boilerplate R Access to the Amazon Web Services ('AWS') Java SDK

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-rappdirs 
Requires:         R-utils 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-rappdirs 

%description
Provides boilerplate access to all of the classes included in the Amazon
Web Services ('AWS') Java Software Development Kit (SDK) via
package:'rJava'.  According to Amazon, the 'SDK helps take the complexity
out of coding by providing Java APIs for many AWS services including
Amazon S3, Amazon EC2, DynamoDB, and more'.  You can read more about the
included Java code on Amazon's website:
<https://aws.amazon.com/sdk-for-java/>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
