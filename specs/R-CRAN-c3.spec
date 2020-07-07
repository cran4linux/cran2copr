%global packname  c3
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          'C3.js' Chart Library

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-viridis 

%description
Create interactive charts with the 'C3.js' <http://c3js.org/> charting
library. All plot types in 'C3.js' are available and include line, bar,
scatter, and mixed geometry plots. Plot annotations, labels and axis are
highly adjustable. Interactive web based charts can be embedded in R
Markdown documents or Shiny web applications.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
