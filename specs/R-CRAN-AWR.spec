%global packname  AWR
%global packver   1.11.189
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11.189
Release:          3%{?dist}%{?buildtag}
Summary:          'AWS' Java 'SDK' for R

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-utils 
Requires:         R-CRAN-rJava 
Requires:         R-utils 

%description
Installs the compiled Java modules of the Amazon Web Services ('AWS')
'SDK' to be used in downstream R packages interacting with 'AWS'. See
<https://aws.amazon.com/sdk-for-java> for more information on the 'AWS'
'SDK' for Java.

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
