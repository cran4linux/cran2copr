%global __brp_check_rpaths %{nil}
%global packname  qkerntool
%global packver   1.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.19
Release:          3%{?dist}%{?buildtag}
Summary:          Q-Kernel-Based and Conditionally Negative Definite Kernel-BasedMachine Learning Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-class 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-class 
Requires:         R-graphics 
Requires:         R-methods 

%description
Nonlinear machine learning tool for classification, clustering and
dimensionality reduction. It integrates 12 q-kernel functions and 15
conditional negative definite kernel functions and includes the q-kernel
and conditional negative definite kernel version of density-based spatial
clustering of applications with noise, spectral clustering, generalized
discriminant analysis, principal component analysis, multidimensional
scaling, locally linear embedding, sammon's mapping and t-Distributed
stochastic neighbor embedding.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
