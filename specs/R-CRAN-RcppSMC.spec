%global packname  RcppSMC
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}
Summary:          Rcpp Bindings for Sequential Monte Carlo

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-methods 

%description
R access to the Sequential Monte Carlo Template Classes by Johansen
<doi:10.18637/jss.v030.i06> is provided. At present, four additional
examples have been added, and the first example from the JSS paper has
been extended. Further integration and extensions are planned.

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
%doc %{rlibdir}/%{packname}/announce
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/rawdata
%doc %{rlibdir}/%{packname}/sampleData
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
