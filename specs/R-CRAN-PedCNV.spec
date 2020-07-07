%global packname  PedCNV
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}
Summary:          An implementation for association analysis with CNV data.

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-RcppArmadillo >= 0.3.900.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.4
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-RcppArmadillo >= 0.3.900.0
Requires:         R-CRAN-Rcpp >= 0.10.4
Requires:         R-CRAN-ggplot2 

%description
An implementation for association analysis with CNV data in R. It provides
two methods for association study: first, the observed probe intensity
measurement can be directly used to detect the association of CNV with
phenotypes of interest. Second, the most probable copy number is estimated
with the proposed likelihood and the association of the most probable copy
number with phenotype is tested. This method can be applied to both the
independent and correlated population.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
