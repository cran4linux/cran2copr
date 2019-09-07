%global packname  dyndimred
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Dimensionality Reduction Methods in a Common Format

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dynutils >= 1.0.3
BuildRequires:    R-CRAN-irlba 
Requires:         R-CRAN-dynutils >= 1.0.3
Requires:         R-CRAN-irlba 

%description
Provides a common interface for applying dimensionality reduction methods,
such as Principal Component Analysis ('PCA'), Independent Component
Analysis ('ICA'), diffusion maps, Locally-Linear Embedding ('LLE'),
t-distributed Stochastic Neighbor Embedding ('t-SNE'), and Uniform
Manifold Approximation and Projection ('UMAP'). Has built-in support for
sparse matrices.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
