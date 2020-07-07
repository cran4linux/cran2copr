%global packname  FPDclustering
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          3%{?dist}
Summary:          PD-Clustering and Factor PD-Clustering

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ThreeWay 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ExPosition 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-CRAN-ThreeWay 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ExPosition 
Requires:         R-cluster 
Requires:         R-CRAN-rootSolve 

%description
Probabilistic distance clustering (PD-clustering) is an iterative,
distribution free, probabilistic clustering method. PD-clustering assigns
units to a cluster according to their probability of membership, under the
constraint that the product of the probability and the distance of each
point to any cluster centre is a constant. PD-clustering is a flexible
method that can be used with non-spherical clusters, outliers, or noisy
data. PDQ is an extension of the algorithm for clusters of different size.
GPDC and TPDC uses a dissimilarity measure based on densities. Factor
PD-clustering (FPDC) is a recently proposed factor clustering method that
involves a linear transformation of variables and a cluster optimizing the
PD-clustering criterion. It works on high dimensional datasets.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
