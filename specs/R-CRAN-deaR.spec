%global packname  deaR
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Conventional and Fuzzy Data Envelopment Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-gridExtra 

%description
Set of functions for Data Envelopment Analysis. It runs both classic and
fuzzy DEA models.See: Banker, R.; Charnes, A.; Cooper, W.W. (1984).
<doi:10.1287/mnsc.30.9.1078>, Charnes, A.; Cooper, W.W.; Rhodes, E.
(1978). <doi:10.1016/0377-2217(78)90138-8> and Charnes, A.; Cooper, W.W.;
Rhodes, E. (1981). <doi:10.1287/mnsc.27.6.668>.

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
