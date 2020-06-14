%global packname  OneArmPhaseTwoStudy
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          2%{?dist}
Summary:          Planning, Conducting, and Analysing Single-Arm Phase II Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.9.11
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.9.11
Requires:         R-methods 
Requires:         R-stats 

%description
Purpose of this package is it to plan, monitor and evaluate oncological
phase II studies. In general this kind of studies are single-arm trials
with planned interim analysis and binary endpoint. To meet the resulting
requirements, the package provides functions to calculate and evaluate
'Simon's two-stage designs' and 'so-called' 'subset designs'. If you are
unfamiliar with this package a good starting point is to take a closer
look at the functions getSolutions() and getSolutionsSub1().The web-based
tool (<https://imbi.shinyapps.io/phaseII-app/>) extends the functionality
of our R package by means of a proper dealing with over- and underrunning.
The R function binom.test of the 'stats' R package and the package 'binom'
might be helpful to assess the performance of the corresponding one-stage
design as a reference.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
