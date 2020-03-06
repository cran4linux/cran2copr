%global packname  mechkar
%global packver   1.14.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.14.6
Release:          1%{?dist}
Summary:          Useful Tools for Scientific Research

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-ROSE 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-ResourceSelection 
BuildRequires:    R-CRAN-InformationValue 
BuildRequires:    R-CRAN-gmodels 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-givitiR 
BuildRequires:    R-CRAN-coxphw 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-MASS 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-car 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-ROSE 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-ResourceSelection 
Requires:         R-CRAN-InformationValue 
Requires:         R-CRAN-gmodels 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-givitiR 
Requires:         R-CRAN-coxphw 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-writexl 
Requires:         R-MASS 

%description
Utilities that help researchers in various phases of their research work.
This package offer a function that automate the exploratory data analysis,
a function for the generation of Table 1 (required on many epidemiological
papers) which can be exported to excel. There is also a function for
generation of a forestplot with a table and relative risks or odds ratios
that can be used for publication. Additionally, there is a function that
generates train/test random partitions used for model evaluation that
checks for the balance of the partitions.

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
%{rlibdir}/%{packname}/INDEX
