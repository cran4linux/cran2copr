%global packname  spmoran
%global packver   0.2.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0.1
Release:          1%{?dist}
Summary:          Moran Eigenvector-Based Scalable Spatial Additive Mixed Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-splines 
BuildRequires:    R-methods 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-vegan 
Requires:         R-Matrix 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-rARPACK 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-splines 
Requires:         R-methods 

%description
Functions for estimating Moran eigenvector-based spatial additive mixed
models, and other spatial regression models. For details see Murakami
(2020) <arXiv:1703.04467>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
