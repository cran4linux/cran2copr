%global packname  gwdegree
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          A Shiny App to Aid Interpretation of Geometrically-WeightedDegree Estimates in Exponential Random Graph Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ergm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ergm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-network 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-tidyr 

%description
This is a Shiny application intended to provide better understanding of
how geometrically-weighted degree terms function in exponential random
graph models of networks. It contains just one user function, gwdegree(),
which launches the Shiny application.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/app.R
%{rlibdir}/%{packname}/INDEX
