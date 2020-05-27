%global packname  servr
%global packver   0.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.17
Release:          1%{?dist}
Summary:          A Simple HTTP Server to Serve Static Files or Dynamic Documents

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httpuv >= 1.4.0
BuildRequires:    R-CRAN-mime >= 0.2
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-httpuv >= 1.4.0
Requires:         R-CRAN-mime >= 0.2
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-jsonlite 

%description
Start an HTTP server in R to serve static files, or dynamic documents that
can be converted to HTML files (e.g., R Markdown) under a given directory.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/bin
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/resources
%{rlibdir}/%{packname}/INDEX
