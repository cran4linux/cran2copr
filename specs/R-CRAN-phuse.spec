%global packname  phuse
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          2%{?dist}
Summary:          Web Application Framework for 'PhUSE' Scripts

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-SASxport 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-git2r 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-SASxport 

%description
Make it easy to review, download and execute scripts stored in Github
'phuse-scripts' repository <https://github.com/phuse-org/phuse-scripts>.
Some examples included show the web application framework using the script
metadata. The 'PhUSE' is Pharmaceutical Users Software Exchange
<http://www.phuse.eu>.

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
%doc %{rlibdir}/%{packname}/docs
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
