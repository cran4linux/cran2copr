%global packname  vfcp
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          3%{?dist}
Summary:          Computation of v Values for U and Copula C(U, v)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-stringr 

%description
Computation the value of one of two uniformly distributed marginals if the
copula probability value is known and the value of the second marginal is
also known. Computation and plotting corresponding cumulative distribution
function or survival function. The numerical definition of a common area
limited by lines of the cumulative distribution function and survival
function. Approximate quantification of the probability of this area. In
addition to 'amh', the copula dimension may be larger than 2.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
