%global packname  ggvis
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}
Summary:          Interactive Grammar of Graphics

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 0.9.11
BuildRequires:    R-CRAN-dplyr >= 0.4.0
BuildRequires:    R-CRAN-htmltools >= 0.2.4
BuildRequires:    R-CRAN-shiny >= 0.11.1
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-methods 
Requires:         R-CRAN-jsonlite >= 0.9.11
Requires:         R-CRAN-dplyr >= 0.4.0
Requires:         R-CRAN-htmltools >= 0.2.4
Requires:         R-CRAN-shiny >= 0.11.1
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lazyeval 
Requires:         R-methods 

%description
An implementation of an interactive grammar of graphics, taking the best
parts of 'ggplot2', combining them with the reactive framework of 'shiny'
and drawing web graphics using 'vega'.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/update.sh
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
