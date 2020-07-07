%global packname  frailtyEM
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Fitting Frailty Models with the EM Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.8
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-expint 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-Rcpp >= 0.12.8
Requires:         R-survival 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-expint 
Requires:         R-CRAN-tibble 
Requires:         R-Matrix 
Requires:         R-CRAN-numDeriv 

%description
Contains functions for fitting shared frailty models with a
semi-parametric baseline hazard with the Expectation-Maximization
algorithm. Supported data formats include clustered failures with left
truncation and recurrent events in gap-time or Andersen-Gill format.
Several frailty distributions, such as the the gamma, positive stable and
the Power Variance Family are supported.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
