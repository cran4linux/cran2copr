%global packname  DiscreteFDR
%global packver   1.3-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          3%{?dist}%{?buildtag}
Summary:          Multiple Testing Procedures with Adaptation for Discrete Tests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-methods 

%description
Multiple testing procedures described in the paper Döhler, Durand and
Roquain (2018) "New FDR bounds for discrete and heterogeneous tests"
<doi:10.1214/18-EJS1441>. The main procedures of the paper (HSU and HSD),
their adaptive counterparts (AHSU and AHSD), and the HBR variant are
available and are coded to take as input a set of observed p-values and
their discrete support under the null. A function to compute such p-values
and supports for Fisher's exact tests is also provided, along with a
wrapper allowing to apply discrete procedures directly from contingency
tables.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
