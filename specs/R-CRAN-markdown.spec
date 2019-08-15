%global packname  markdown
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Render Markdown with the C Library 'Sundown'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 2.11.1
Requires:         R-core >= 2.11.1
BuildRequires:    R-CRAN-mime >= 0.3
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xfun 
Requires:         R-CRAN-mime >= 0.3
Requires:         R-utils 
Requires:         R-CRAN-xfun 

%description
Provides R bindings to the 'Sundown' Markdown rendering library
(<https://github.com/vmg/sundown>). Markdown is a plain-text formatting
syntax that can be converted to 'XHTML' or other formats. See
<http://en.wikipedia.org/wiki/Markdown> for more information about
Markdown.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYING
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NOTICE
%doc %{rlibdir}/%{packname}/resources
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
