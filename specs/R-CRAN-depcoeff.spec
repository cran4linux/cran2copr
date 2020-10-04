%global packname  depcoeff
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Dependency Coefficients

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-copula 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-copula 

%description
Functions to compute coefficients measuring the dependence of two or more
than two variables. The functions can be deployed to gain information
about functional dependencies of the variables with emphasis on monotone
functions. The statistics describe how well one response variable can be
approximated by a monotone function of other variables. In regression
analysis the variable selection is an important issue. In this framework
the functions could be useful tools in modeling the regression function.
Detailed explanations on the subject can be found in papers Liebscher
(2014) <doi:10.2478/demo-2014-0004>; Liebscher (2017)
<doi:10.1515/demo-2017-0012>; Liebscher (2019, submitted).

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
