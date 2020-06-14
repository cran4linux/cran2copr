%global packname  cemco
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          2%{?dist}
Summary:          Fit 'CemCO' Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-clusteval 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-clusteval 
Requires:         R-CRAN-doParallel 
Requires:         R-nnet 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-foreach 
Requires:         R-MASS 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-mvtnorm 

%description
Functions to fit the 'CemCO' algorithm, a model-based (Gaussian)
clustering algorithm that removes/minimizes the effects of undesirable
covariates during the clustering process both in cluster centroid and in
cluster covariance structures (Relvas C. & Fujita A., (2020)
<arXiv:2004.02333>).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
