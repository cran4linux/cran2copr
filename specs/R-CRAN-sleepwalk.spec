%global __brp_check_rpaths %{nil}
%global packname  sleepwalk
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interactively Explore Dimension-Reduced Embeddings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jrc >= 0.4.0
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-jrc >= 0.4.0
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
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
