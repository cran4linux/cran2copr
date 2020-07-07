%global packname  wdman
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          3%{?dist}
Summary:          'Webdriver'/'Selenium' Binary Manager

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-semver >= 0.2.0
BuildRequires:    R-CRAN-binman 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-utils 
Requires:         R-CRAN-semver >= 0.2.0
Requires:         R-CRAN-binman 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-yaml 
Requires:         R-utils 

%description
There are a number of binary files associated with the
'Webdriver'/'Selenium' project (see <http://www.seleniumhq.org/download/>,
<https://sites.google.com/a/chromium.org/chromedriver/>,
<https://github.com/mozilla/geckodriver>,
<http://phantomjs.org/download.html> and
<https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver> for
more information). This package provides functions to download these
binaries and to manage processes involving them.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/yaml
%{rlibdir}/%{packname}/INDEX
