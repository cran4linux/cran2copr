%global packname  ReIns
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}
Summary:          Functions from "Reinsurance: Actuarial and Statistical Aspects"

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-foreach >= 1.4.1
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-survival 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-CRAN-foreach >= 1.4.1
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-survival 
Requires:         R-utils 
Requires:         R-parallel 

%description
Functions from the book "Reinsurance: Actuarial and Statistical Aspects"
(2017) by Hansjoerg Albrecher, Jan Beirlant and Jef Teugels
<http://www.wiley.com/WileyCDA/WileyTitle/productCd-0470772689.html>.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
