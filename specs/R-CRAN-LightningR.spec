%global packname  LightningR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Communication with Lightning-Viz Server

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-httr 

%description
The purpose of this package is to enable usage of lightningviz server to
be accessible from R. The server itself can be found at
http://lightning-viz.org/ and is required to work with this package.
Package by itself cannot and will not create any visualizations.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
