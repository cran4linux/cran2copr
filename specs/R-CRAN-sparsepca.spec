%global packname  sparsepca
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Sparse Principal Component Analysis (SPCA)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rsvd 
Requires:         R-CRAN-rsvd 

%description
Sparse principal component analysis (SPCA) attempts to find sparse weight
vectors (loadings), i.e., a weight vector with only a few 'active'
(nonzero) values. This approach provides better interpretability for the
principal components in high-dimensional data settings. This is, because
the principal components are formed as a linear combination of only a few
of the original variables. This package provides efficient routines to
compute SPCA. Specifically, a variable projection solver is used to
compute the sparse solution. In addition, a fast randomized accelerated
SPCA routine and a robust SPCA routine is provided. Robust SPCA allows to
capture grossly corrupted entries in the data. The methods are discussed
in detail by N. Benjamin Erichson et al. (2018) <arXiv:1804.00341>.

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
