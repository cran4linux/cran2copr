%global packname  hts
%global packver   6.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.0
Release:          3%{?dist}
Summary:          Hierarchical and Grouped Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-forecast >= 8.12
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-forecast >= 8.12
Requires:         R-CRAN-SparseM 
Requires:         R-Matrix 
Requires:         R-CRAN-matrixcalc 
Requires:         R-parallel 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Provides methods for analysing and forecasting hierarchical and grouped
time series. The available forecast methods include bottom-up, top-down,
optimal combination reconciliation (Hyndman et al. 2011)
<doi:10.1016/j.csda.2011.03.006>, and trace minimization reconciliation
(Wickramasuriya et al. 2018) <doi:10.1080/01621459.2018.1448825>.

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
%doc %{rlibdir}/%{packname}/docs
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
