%global packname  enetLTS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Robust and Sparse Methods for High Dimensional Linear andLogistic Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-robustHD 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-cvTools 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-robustHD 
Requires:         R-grid 
Requires:         R-CRAN-reshape 
Requires:         R-parallel 
Requires:         R-CRAN-cvTools 
Requires:         R-stats 

%description
Fully robust versions of the elastic net estimator are introduced for
linear and logistic regression, in particular high dimensional data by
Kurnaz, Hoffmann and Filzmoser (2017)
<DOI:10.1016/j.chemolab.2017.11.017>. The algorithm searches for outlier
free subsets on which the classical elastic net estimators can be applied.

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
