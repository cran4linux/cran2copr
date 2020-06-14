%global packname  vennLasso
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          2%{?dist}
Summary:          Variable Selection for Heterogeneous Populations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-survival 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-VennDiagram 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppNumerical 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-foreach 
Requires:         R-survival 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-VennDiagram 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-igraph 
Requires:         R-methods 

%description
Provides variable selection and estimation routines for models with main
effects stratified on multiple binary factors. The 'vennLasso' package is
an implementation of the method introduced in Huling, et al. (2017)
<doi:10.1111/biom.12769>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
