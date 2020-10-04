%global packname  Amelia
%global packver   1.7.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.6
Release:          3%{?dist}%{?buildtag}
Summary:          A Program for Missing Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.11
BuildRequires:    R-foreign 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11
Requires:         R-foreign 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 

%description
A tool that "multiply imputes" missing data in a single cross-section
(such as a survey), from a time series (like variables collected for each
year in a country), or from a time-series-cross-sectional data set (such
as collected by years for each of several countries). Amelia II implements
our bootstrapping-based algorithm that gives essentially the same answers
as the standard IP or EMis approaches, is usually considerably faster than
existing approaches and can handle many more variables.  Unlike Amelia I
and other statistically rigorous imputation software, it virtually never
crashes (but please let us know if you find to the contrary!).  The
program also generalizes existing approaches by allowing for trends in
time series across observations within a cross-sectional unit, as well as
priors that allow experts to incorporate beliefs they have about the
values of missing cells in their data.  Amelia II also includes useful
diagnostics of the fit of multiple imputation models.  The program works
from the R command line or via a graphical user interface that does not
require users to know R.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/gui
%doc %{rlibdir}/%{packname}/test
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
