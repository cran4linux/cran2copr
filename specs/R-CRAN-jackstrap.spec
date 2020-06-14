%global packname  jackstrap
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Correcting Nonparametric Frontier Measurements for Outliers

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-Benchmarking 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-Benchmarking 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-scales 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rlang 
Requires:         R-utils 

%description
Provides method used to check whether data have outlier in efficiency
measurement of big samples with data envelopment analysis (DEA). In this
jackstrap method, the package provides two criteria to define outliers:
heaviside and k-s test. The technique was developed by Sousa and Stosic
(2005) "Technical Efficiency of the Brazilian Municipalities: Correcting
Nonparametric Frontier Measurements for Outliers."
<doi:10.1007/s11123-005-4702-4>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
