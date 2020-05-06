%global packname  CSUV
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Combined Selection and Uncertainty Visualiser (CSUV)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-relaxo 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-datasets 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-HDCI 
BuildRequires:    R-CRAN-parcor 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-relaxo 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-DT 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-datasets 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-HDCI 
Requires:         R-CRAN-parcor 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 

%description
Implementation of CSUV from C. Yuen and P. Fryzlewicz (2020)
<arXiv:2003.02791> "Exploiting disagreement between high-dimensional
variable selectors for uncertainty visualization". CSUV aims to perform
variable selection and illustrate variable selection uncertainties by
combining variable selection results from various methods.

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
