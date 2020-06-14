%global packname  epimdr
%global packver   0.6-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.5
Release:          2%{?dist}
Summary:          Functions and Data for "Epidemics: Models and Data in R"

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-polspline 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-polspline 

%description
Functions, data sets and shiny apps for "Epidemics: Models and Data in R"
by Ottar N. Bjornstad (ISBN 978-3-319-97487-3)
<https://www.springer.com/gp/book/9783319974866>. The package contains
functions to study the S(E)IR model, spatial and age-structured SIR
models; time-series SIR and chain-binomial stochastic models; catalytic
disease models; coupled map lattice models of spatial transmission and
network models for social spread of infection. The package is also an
advanced quantitative companion to the coursera Epidemics Massive Online
Open Course <https://www.coursera.org/learn/epidemics>.

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
