%global packname  webdriver
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          2%{?dist}
Summary:          'WebDriver' Client for 'PhantomJS'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 2.0.0
BuildRequires:    R-CRAN-curl >= 2.0
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-debugme 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-showimage 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-callr >= 2.0.0
Requires:         R-CRAN-curl >= 2.0
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-debugme 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-showimage 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
A client for the 'WebDriver' 'API'. It allows driving a (probably
headless) web browser, and can be used to test web applications, including
'Shiny' apps. In theory it works with any 'WebDriver' implementation, but
it was only tested with 'PhantomJS'.

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
%doc %{rlibdir}/%{packname}/js
%doc %{rlibdir}/%{packname}/README.markdown
%doc %{rlibdir}/%{packname}/README.Rmd
%doc %{rlibdir}/%{packname}/screenshot-1-1.png
%doc %{rlibdir}/%{packname}/screenshot-2-1.png
%{rlibdir}/%{packname}/INDEX
