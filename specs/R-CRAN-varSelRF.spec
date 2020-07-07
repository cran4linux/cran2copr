%global packname  varSelRF
%global packver   0.7-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.8
Release:          3%{?dist}
Summary:          Variable Selection using Random Forests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-parallel 
Requires:         R-CRAN-randomForest 
Requires:         R-parallel 

%description
Variable selection from random forests using both backwards variable
elimination (for the selection of small sets of non-redundant variables)
and selection based on the importance spectrum (somewhat similar to scree
plots; for the selection of large, potentially highly-correlated
variables). Main applications in high-dimensional data (e.g., microarray
data, and other genomics and proteomics applications).

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
