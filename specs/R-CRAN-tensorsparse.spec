%global packname  tensorsparse
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Multiway Clustering via Tensor Block Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-HDCI 
BuildRequires:    R-CRAN-clues 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-methods 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-HDCI 
Requires:         R-CRAN-clues 
Requires:         R-parallel 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-rTensor 
Requires:         R-methods 

%description
Implements the multiway sparse clustering approach of Zeng and Wang (2019)
<arXiv:1906.03807>.

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
%{rlibdir}/%{packname}/INDEX
