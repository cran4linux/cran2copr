%global packname  vegawidget
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}
Summary:          'Htmlwidget' for 'Vega' and 'Vega-Lite'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-htmltools 

%description
'Vega' and 'Vega-Lite' parse text in 'JSON' notation to render
chart-specifications into 'HTML'. This package is used to facilitate the
rendering. It also provides a means to interact with signals, events, and
datasets in a 'Vega' chart using 'JavaScript' or 'Shiny'.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/bin
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/example-data
%doc %{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/schema
%doc %{rlibdir}/%{packname}/shiny-demo
%doc %{rlibdir}/%{packname}/templates
%doc %{rlibdir}/%{packname}/test-apps
%doc %{rlibdir}/%{packname}/tutorials
%{rlibdir}/%{packname}/INDEX
