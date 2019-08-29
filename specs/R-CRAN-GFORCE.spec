%global packname  GFORCE
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Clustering and Inference Procedures for High-Dimensional LatentVariable Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-lpSolve 
Requires:         R-stats 

%description
A complete suite of computationally efficient methods for high dimensional
clustering and inference problems in G-Latent Models (a type of Latent
Variable Gaussian graphical model). The main feature is the FORCE
(First-Order, Certifiable, Efficient) clustering algorithm which is a fast
solver for a semi-definite programming (SDP) relaxation of the K-means
problem. For certain types of graphical models (G-Latent Models), with
high probability the algorithm not only finds the optimal clustering, but
produces a certificate of having done so. This certificate, however, is
model independent and so can also be used to certify data clustering
problems. The 'GFORCE' package also contains implementations of
inferential procedures for G-Latent graphical models using n-fold cross
validation. Also included are native code implementations of other popular
clustering methods such as Lloyd's algorithm with kmeans++ initialization
and complete linkage hierarchical clustering. The FORCE method is due to
Eisenach and Liu (2019) <arxiv:1806.00530>.

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
%{rlibdir}/%{packname}/libs
