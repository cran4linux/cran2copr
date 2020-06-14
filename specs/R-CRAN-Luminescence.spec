%global packname  Luminescence
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          2%{?dist}
Summary:          Comprehensive Luminescence Dating Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-XML >= 3.98.1.9
BuildRequires:    R-CRAN-plotrix >= 3.7
BuildRequires:    R-CRAN-raster >= 2.8.0
BuildRequires:    R-CRAN-DEoptim >= 2.2.4
BuildRequires:    R-CRAN-zoo >= 1.8
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-shape >= 1.4.3
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-readxl >= 1.3.0
BuildRequires:    R-CRAN-minpack.lm >= 1.2
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-bbmle >= 1.0.20
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.300.0.0
BuildRequires:    R-CRAN-matrixStats >= 0.54.0
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
Requires:         R-CRAN-XML >= 3.98.1.9
Requires:         R-CRAN-plotrix >= 3.7
Requires:         R-CRAN-raster >= 2.8.0
Requires:         R-CRAN-DEoptim >= 2.2.4
Requires:         R-CRAN-zoo >= 1.8
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-shape >= 1.4.3
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-readxl >= 1.3.0
Requires:         R-CRAN-minpack.lm >= 1.2
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-bbmle >= 1.0.20
Requires:         R-CRAN-matrixStats >= 0.54.0
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-parallel 

%description
A collection of various R functions for the purpose of Luminescence dating
data analysis. This includes, amongst others, data import, export,
application of age models, curve deconvolution, sequence analysis and
plotting of equivalent dose distributions.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
