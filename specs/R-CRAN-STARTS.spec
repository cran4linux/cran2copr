%global packname  STARTS
%global packver   1.2-35
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.35
Release:          4%{?dist}
Summary:          Functions for the STARTS Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-CDM >= 7.1.19
BuildRequires:    R-CRAN-sirt >= 2.3
BuildRequires:    R-CRAN-LAM >= 0.3.27
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-CDM >= 7.1.19
Requires:         R-CRAN-sirt >= 2.3
Requires:         R-CRAN-LAM >= 0.3.27
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Contains functions for estimating the STARTS model of Kenny and Zautra
(1995, 2001) <DOI:10.1037/0022-006X.63.1.52>, <DOI:10.1037/10409-008>.
Penalized maximum likelihood estimation and Markov Chain Monte Carlo
estimation are also provided, see Luedtke, Robitzsch and Wagner (2018)
<DOI:10.1037/met0000155>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
