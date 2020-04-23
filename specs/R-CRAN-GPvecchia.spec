%global packname  GPvecchia
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Scalable Gaussian-Process Approximations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-Matrix >= 1.2.14
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sparseinv 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-GpGp 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-BH 
Requires:         R-Matrix >= 1.2.14
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-sparseinv 
Requires:         R-CRAN-fields 
Requires:         R-parallel 
Requires:         R-CRAN-GpGp 
Requires:         R-CRAN-FNN 

%description
Fast scalable Gaussian process approximations, particularly well suited to
spatial (aerial, remote-sensed) and environmental data, described in more
detail in Katzfuss and Guinness (2017) <arXiv:1708.06302>. Package also
contains a fast implementation of the incomplete Cholesky decomposition
(IC0), based on Schaefer et al. (2019) <arXiv:1706.02205> and MaxMin
ordering proposed in Guinness (2018) <arXiv:1609.05372>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
