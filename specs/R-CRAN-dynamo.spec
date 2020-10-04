%global packname  dynamo
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Fit a Stochastic Dynamical Array Model to Array Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-glamlasso >= 3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-MortalitySmooth 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-glamlasso >= 3.0
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-abind 
Requires:         R-CRAN-MortalitySmooth 

%description
An implementation of the method proposed in Lund and Hansen (2018) for
fitting 3-dimensional dynamical array models.  The implementation is based
on the glamlasso package, see Lund et al. (2017)
<doi:10.1080/10618600.2017.1279548>, for efficient design matrix free
lasso regularized estimation in a generalized linear array model. The
implementation uses a block relaxation scheme to fit each individual
component in the model using functions from the glamlasso package.

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
%{rlibdir}/%{packname}/libs
