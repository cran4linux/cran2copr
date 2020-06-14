%global packname  explor
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          2%{?dist}
Summary:          Interactive Interfaces for Results Exploration

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.0
BuildRequires:    R-CRAN-scatterD3 >= 0.9.1
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-highr 
BuildRequires:    R-CRAN-formatR 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-shiny >= 1.0
Requires:         R-CRAN-scatterD3 >= 0.9.1
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-DT 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-highr 
Requires:         R-CRAN-formatR 
Requires:         R-CRAN-RColorBrewer 

%description
Shiny interfaces and graphical functions for multivariate analysis results
exploration.

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
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX
