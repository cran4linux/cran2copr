%global packname  FIT
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          3%{?dist}
Summary:          Transcriptomic Dynamics Models in Field Conditions

License:          MPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildRequires:    R-CRAN-gglasso >= 1.4
BuildRequires:    R-CRAN-RcppEigen >= 0.3.2.1.2
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-MASS 
Requires:         R-CRAN-gglasso >= 1.4
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-methods 
Requires:         R-CRAN-XML 
Requires:         R-MASS 

%description
Provides functionality for constructing statistical models of
transcriptomic dynamics in field conditions. It further offers the
function to predict expression of a gene given the attributes of samples
and meteorological data. Nagano, A. J., Sato, Y., Mihara, M., Antonio, B.
A., Motoyama, R., Itoh, H., Naganuma, Y., and Izawa, T. (2012).
<doi:10.1016/j.cell.2012.10.048>. Iwayama, K., Aisaka, Y., Kutsuna, N.,
and Nagano, A. J. (2017). <doi:10.1093/bioinformatics/btx049>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
