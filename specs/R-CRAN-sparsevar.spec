%global packname  sparsevar
%global packver   0.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.11
Release:          3%{?dist}
Summary:          Sparse VAR/VECM Models Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-picasso 
BuildRequires:    R-CRAN-corpcor 
Requires:         R-Matrix 
Requires:         R-CRAN-ncvreg 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-grid 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-picasso 
Requires:         R-CRAN-corpcor 

%description
A wrapper for sparse VAR/VECM time series models estimation using
penalties like ENET (Elastic Net), SCAD (Smoothly Clipped Absolute
Deviation) and MCP (Minimax Concave Penalty). Based on the work of Sumanta
Basu and George Michailidis <doi:10.1214/15-AOS1315>.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
