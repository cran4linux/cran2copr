%global packname  GMSimpute
%global packver   0.0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.0
Release:          3%{?dist}
Summary:          Generalized Mass Spectrum Missing Peaks Abundance Imputation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-utils 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 

%description
Two-Step Lasso (TS-Lasso) and compound minimum methods to recover the
abundance of missing peaks in mass spectrum analysis. TS-Lasso is an
imputation method that handles various types of missing peaks
simultaneously. This package provides the procedure to generate missing
peaks (or data) for simulation study, as well as a tool to estimate and
visualize the proportion of missing at random.

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
%{rlibdir}/%{packname}/INDEX
