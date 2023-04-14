%global __brp_check_rpaths %{nil}
%global packname  ClusVis
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Gaussian-Based Visualization of Gaussian and Non-GaussianModel-Based Clustering

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-VarSelLCM >= 2.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rmixmod 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-VarSelLCM >= 2.1
Requires:         R-CRAN-Rcpp 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-mgcv 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rmixmod 

%description
Gaussian-Based Visualization of Gaussian and Non-Gaussian Model-Based
Clustering done on any type of data. Visualization is based on the
probabilities of classification.

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
