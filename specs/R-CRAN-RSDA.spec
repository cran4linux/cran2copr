%global packname  RSDA
%global packver   3.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.1
Release:          1%{?dist}
Summary:          R to Symbolic Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpolypath 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-princurve 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-randomcoloR 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpolypath 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-princurve 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-randomcoloR 

%description
Symbolic Data Analysis (SDA) was proposed by professor Edwin Diday in
1987, the main purpose of SDA is to substitute the set of rows (cases) in
the data table for a concept (second order statistical unit). This package
implements, to the symbolic case, certain techniques of automatic
classification, as well as some linear models.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
