%global packname  rasterly
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          Easily and Rapidly Generate Raster Image Data with Support for'Plotly.js'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-grid 
Requires:         R-stats 

%description
It aims to easily and rapidly generate raster data in R, even for very
large datasets, with an aesthetics-based mapping syntax that should be
familiar to users of the 'ggplot2' package. While 'rasterly' does not
attempt to reproduce the full functionality of the 'Datashader' graphics
pipeline system for Python, the 'rasterly' API has several core elements
in common with that software package.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
