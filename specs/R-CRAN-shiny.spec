%global packname  shiny
%global packver   1.4.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0.2
Release:          1%{?dist}
Summary:          Web Application Framework for R

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.0
BuildRequires:    R-CRAN-httpuv >= 1.5.2
BuildRequires:    R-CRAN-promises >= 1.1.0
BuildRequires:    R-CRAN-later >= 1.0.0
BuildRequires:    R-CRAN-fastmap >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.16
BuildRequires:    R-CRAN-htmltools >= 0.4.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-mime >= 0.3
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-sourcetools 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-R6 >= 2.0
Requires:         R-CRAN-httpuv >= 1.5.2
Requires:         R-CRAN-promises >= 1.1.0
Requires:         R-CRAN-later >= 1.0.0
Requires:         R-CRAN-fastmap >= 1.0.0
Requires:         R-CRAN-jsonlite >= 0.9.16
Requires:         R-CRAN-htmltools >= 0.4.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-mime >= 0.3
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-sourcetools 
Requires:         R-tools 
Requires:         R-CRAN-crayon 

%description
Makes it incredibly easy to build interactive web applications with R.
Automatic "reactive" binding between inputs and outputs and extensive
prebuilt widgets make it possible to build beautiful, responsive, and
powerful applications with minimal effort.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/_pkgdown.yml
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/template
%doc %{rlibdir}/%{packname}/www
%doc %{rlibdir}/%{packname}/www-dir
%{rlibdir}/%{packname}/INDEX
