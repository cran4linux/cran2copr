%global debug_package %{nil}
%global packname  bcgam
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Bayesian Constrained Generalised Linear Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-nimble >= 0.6.9
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-nimble >= 0.6.9
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-coda 

%description
Fits generalised partial linear regression models using a Bayesian
approach, where shape and smoothness constraints are imposed on
nonparametrically modelled predictors through shape-restricted splines,
and no constraints are imposed on optional parametrically modelled
covariates. See Meyer et al. (2011) <doi/10.1080/10485252.2011.597852> for
more details. IMPORTANT: before installing 'bcgam', you need to install
'Rtools' (Windows) or 'Xcode' (Mac OS X). These are required for the
correct installation of 'nimble' (<https://r-nimble.org/download>).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
