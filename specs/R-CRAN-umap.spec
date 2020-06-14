%global packname  umap
%global packver   0.2.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5.0
Release:          2%{?dist}
Summary:          Uniform Manifold Approximation and Projection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.6
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.12.6
Requires:         R-methods 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-RSpectra 
Requires:         R-stats 

%description
Uniform manifold approximation and projection is a technique for dimension
reduction. The algorithm was described by McInnes and Healy (2018) in
<arXiv:1802.03426>. This package provides an interface for two
implementations. One is written from scratch, including components for
nearest-neighbor search and for embedding. The second implementation is a
wrapper for 'python' package 'umap-learn' (requires separate installation,
see vignette for more details).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
