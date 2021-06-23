%global __brp_check_rpaths %{nil}
%global packname  sstModel
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Swiss Solvency Test (SST) Standard Models

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.0.17
BuildRequires:    R-CRAN-data.table >= 1.10.4.3
BuildRequires:    R-CRAN-shiny >= 1.0.5
BuildRequires:    R-CRAN-readxl >= 1.0.0
BuildRequires:    R-CRAN-shinydashboard >= 0.6.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-MASS 
Requires:         R-CRAN-openxlsx >= 4.0.17
Requires:         R-CRAN-data.table >= 1.10.4.3
Requires:         R-CRAN-shiny >= 1.0.5
Requires:         R-CRAN-readxl >= 1.0.0
Requires:         R-CRAN-shinydashboard >= 0.6.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-MASS 

%description
Framework for the implementation of solvency related computations based on
standard models for the Swiss Solvency Test (SST), a risk-based capital
standard for Swiss insurance companies. Allows Monte Carlo simulation of
market risk, some insurance risks and their aggregation. Additional
toolbox for preprocessing computations. Convenient 'shiny' GUI combined
with a parser for an input 'excel' (.xlsx) template to simplify model
configuration, data fill-in and results visualization.

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
%doc %{rlibdir}/%{packname}/COPYRIGHT
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
