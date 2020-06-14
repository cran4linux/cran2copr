%global packname  eoffice
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          2%{?dist}
Summary:          Export or Graph and Tables to 'Microsoft' Office and ImportFigures and Tables

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-rvg 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-CRAN-R.devices 
BuildRequires:    R-CRAN-devEMF 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-rvg 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplotify 
Requires:         R-CRAN-R.devices 
Requires:         R-CRAN-devEMF 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-plotly 

%description
Provides wrap functions to export and import graphics and data frames in R
to 'microsoft' office. And This package also provide write out figures
with lots of different formats. Since people may work on the platform
without GUI support, the package also provide function to easily write out
figures to lots of different type of formats. Now this package provide
function to extract colors from all types of figures and pdf files.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
