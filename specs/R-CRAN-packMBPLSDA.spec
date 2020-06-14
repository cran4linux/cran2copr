%global packname  packMBPLSDA
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          2%{?dist}
Summary:          Multi-Block Partial Least Squares Discriminant Analysis

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-DiscriMiner 
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-FactoMineR 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-DiscriMiner 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-FactoMineR 

%description
Several functions are provided to implement a MBPLSDA : components search,
optimal model components number search, optimal model validity test by
permutation tests, observed values evaluation of optimal model parameters
and predicted categories, bootstrap values evaluation of optimal model
parameters and predicted cross-validated categories. The use of this
package is described in Brandolini-Bunlon et al (2019, Multi-block PLS
discriminant analysis for the joint analysis of metabolomic and
epidemiological data (submitted in Metabolomics)).

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
