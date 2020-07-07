%global packname  HDCI
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          High Dimensional Confidence Interval Based on Lasso andBootstrap

License:          GNU General Public License version 2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-lattice 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-slam 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-doParallel 
Requires:         R-lattice 
Requires:         R-Matrix 
Requires:         R-CRAN-mvtnorm 

%description
Fits regression models on high dimensional data to estimate coefficients
and use bootstrap method to obtain confidence intervals. Choices for
regression models are Lasso, Lasso+OLS, Lasso partial ridge, Lasso+OLS
partial ridge.

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
