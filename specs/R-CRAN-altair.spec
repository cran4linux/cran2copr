%global packname  altair
%global packver   4.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.1
Release:          2%{?dist}
Summary:          Interface to 'Altair'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.9
BuildRequires:    R-CRAN-vegawidget >= 0.3.1
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-repr 
Requires:         R-CRAN-reticulate >= 1.9
Requires:         R-CRAN-vegawidget >= 0.3.1
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-CRAN-repr 

%description
Interface to 'Altair' <https://altair-viz.github.io>, which itself is a
'Python' interface to 'Vega-Lite' <https://vega.github.io/vega-lite>. This
package uses the 'Reticulate' framework
<https://rstudio.github.io/reticulate> to manage the interface between R
and 'Python'.

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
%{rlibdir}/%{packname}/INDEX
