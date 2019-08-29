%global packname  gWidgets2
%global packver   1.0-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}
Summary:          Rewrite of gWidgets API for Simplified GUI Construction

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-digest 
Requires:         R-methods 
Requires:         R-CRAN-digest 

%description
Re-implementation of the 'gWidgets' API. The API is defined in this
package. A second, toolkit-specific package is required to use it. There
are three in development: 'gWidgets2RGtk2', 'gWidgets2Qt', and
'gWidgets2tcltk'.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/docsource
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/images
%doc %{rlibdir}/%{packname}/install
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
