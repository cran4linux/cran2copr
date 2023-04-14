%global __brp_check_rpaths %{nil}
%global packname  ECoL
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Complexity Measures for Supervised Problems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-MASS 
Requires:         R-cluster 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-igraph 
Requires:         R-MASS 

%description
Provides measures to characterize the complexity of classification and
regression problems based on aspects that quantify the linearity of the
data, the presence of informative feature, the sparsity and dimensionality
of the datasets. This package provides bug fixes, generalizations and
implementations of many state of the art measures. The measures are
described in the papers: Lorena et al. (2019) <doi:10.1145/3347711> and
Lorena et al. (2018) <doi:10.1007/s10994-017-5681-1>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
