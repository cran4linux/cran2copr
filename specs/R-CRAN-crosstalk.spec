%global packname  crosstalk
%global packver   1.1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0.1
Release:          3%{?dist}
Summary:          Inter-Widget Interactivity for HTML Widgets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools >= 0.3.6
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-R6 

%description
Provides building blocks for allowing HTML widgets to communicate with
each other, with Shiny or without (i.e. static .html files). Currently
supports linked brushing and filtering.

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
%doc %{rlibdir}/%{packname}/lib
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
