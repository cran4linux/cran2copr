%global packname  hergm
%global packver   4.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.6
Release:          1%{?dist}
Summary:          Hierarchical Exponential-Family Random Graph Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-CRAN-ergm 
BuildRequires:    R-CRAN-latentnet 
BuildRequires:    R-CRAN-mcgibbsit 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mlergm 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-intergraph 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-CRAN-ergm 
Requires:         R-CRAN-latentnet 
Requires:         R-CRAN-mcgibbsit 
Requires:         R-CRAN-network 
Requires:         R-CRAN-sna 
Requires:         R-methods 
Requires:         R-CRAN-mlergm 
Requires:         R-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-intergraph 
Requires:         R-parallel 
Requires:         R-CRAN-stringr 

%description
Hierarchical exponential-family random graph models with local dependence.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
