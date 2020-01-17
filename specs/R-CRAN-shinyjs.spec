%global packname  shinyjs
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Easily Improve the User Experience of Your Shiny Apps in Seconds

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.0.0
BuildRequires:    R-CRAN-digest >= 0.6.8
BuildRequires:    R-CRAN-htmltools >= 0.2.9
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-shiny >= 1.0.0
Requires:         R-CRAN-digest >= 0.6.8
Requires:         R-CRAN-htmltools >= 0.2.9
Requires:         R-CRAN-jsonlite 

%description
Perform common useful JavaScript operations in Shiny apps that will
greatly improve your apps without having to know any JavaScript. Examples
include: hiding an element, disabling an input, resetting an input back to
its original value, delaying code execution by a few seconds, and many
more useful functions for both the end user and the developer. 'shinyjs'
can also be used to easily call your own custom JavaScript functions from
R.

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
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/srcjs
%{rlibdir}/%{packname}/INDEX
