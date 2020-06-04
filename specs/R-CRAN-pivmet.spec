%global packname  pivmet
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Pivotal Methods for Bayesian Relabelling and k-Means Clustering

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
Requires:         pandoc-citeproc
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-runjags 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-CRAN-bayesmix 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-RcmdrMisc 
BuildRequires:    R-CRAN-bayesplot 
Requires:         R-cluster 
Requires:         R-CRAN-mclust 
Requires:         R-MASS 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-runjags 
Requires:         R-CRAN-rstan 
Requires:         R-CRAN-bayesmix 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-RcmdrMisc 
Requires:         R-CRAN-bayesplot 

%description
Collection of pivotal algorithms for: relabelling the MCMC chains in order
to undo the label switching problem in Bayesian mixture models, as
proposed in Egidi, Pappadà, Pauli and Torelli
(2018a)<doi:10.1007/s11222-017-9774-2>; initializing the centers of the
classical k-means algorithm in order to obtain a better clustering
solution. For further details see Egidi, Pappadà, Pauli and Torelli
(2018b)<ISBN:9788891910233>.

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
