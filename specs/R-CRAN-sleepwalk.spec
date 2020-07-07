%global packname  sleepwalk
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          Interactively Explore Dimension-Reduced Embeddings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jrc >= 0.2.0
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-jrc >= 0.2.0
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggplot2 

%description
A tool to interactively explore the embeddings created by dimension
reduction methods such as Principal Components Analysis (PCA),
Multidimensional Scaling (MDS), T-distributed Stochastic Neighbour
Embedding (t-SNE), Uniform Manifold Approximation and Projection (UMAP) or
any other.

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
%doc %{rlibdir}/%{packname}/d3-lasso.min.js
%doc %{rlibdir}/%{packname}/d3.v5.min.js
%doc %{rlibdir}/%{packname}/lasso.js
%doc %{rlibdir}/%{packname}/sleepwalk_canvas.html
%doc %{rlibdir}/%{packname}/sleepwalk_svg.html
%{rlibdir}/%{packname}/INDEX
