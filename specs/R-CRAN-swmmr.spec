%global packname  swmmr
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          2%{?dist}
Summary:          R Interface for US EPA's SWMM

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-tibble >= 1.2.4
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-xts >= 0.10.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-tibble >= 1.2.4
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-xts >= 0.10.1
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
Functions to connect the widely used Storm Water Management Model (SWMM)
of the United States Environmental Protection Agency (US EPA)
<https://www.epa.gov/water-research/storm-water-management-model-swmm> to
R with currently two main goals: (1) Run a SWMM simulation from R and (2)
provide fast access to simulation results, i.e. SWMM's binary
'.out'-files. High performance is achieved with help of Rcpp.
Additionally, reading SWMM's '.inp' and '.rpt' files is supported to
glance model structures and to get direct access to simulation summaries.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
