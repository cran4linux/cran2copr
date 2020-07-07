%global packname  webshot
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          3%{?dist}
Summary:          Take Screenshots of Web Pages

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         ImageMagick
BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-callr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-callr 

%description
Takes screenshots of web pages, including Shiny applications and R
Markdown documents.

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
%doc %{rlibdir}/%{packname}/casperjs
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/NOTICE
%doc %{rlibdir}/%{packname}/utils.js
%doc %{rlibdir}/%{packname}/webshot.js
%{rlibdir}/%{packname}/INDEX
