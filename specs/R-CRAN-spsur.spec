%global packname  spsur
%global packver   1.0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.3
Release:          1%{?dist}
Summary:          Spatial Seemingly Unrelated Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.50
BuildRequires:    R-methods >= 3.5.0
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1
BuildRequires:    R-CRAN-minqa >= 1.2.4
BuildRequires:    R-CRAN-Formula >= 1.2.3
BuildRequires:    R-Matrix >= 1.2.14
BuildRequires:    R-CRAN-spdep >= 0.7.9
BuildRequires:    R-CRAN-sparseMVN >= 0.2.1.1
Requires:         R-MASS >= 7.3.50
Requires:         R-methods >= 3.5.0
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-numDeriv >= 2016.8.1
Requires:         R-CRAN-minqa >= 1.2.4
Requires:         R-CRAN-Formula >= 1.2.3
Requires:         R-Matrix >= 1.2.14
Requires:         R-CRAN-spdep >= 0.7.9
Requires:         R-CRAN-sparseMVN >= 0.2.1.1

%description
A collection of functions to test and estimate Seemingly Unrelated
Regression (usually called SUR) models, with spatial structure, by maximum
likelihood and three-stage least squares. The package estimates the most
common spatial specifications, that is, SUR with Spatial Lag of X
regressors (called SUR-SLX), SUR with Spatial Lag Model (called SUR-SLM),
SUR with Spatial Error Model (called SUR-SEM), SUR with Spatial Durbin
Model (called SUR-SDM), SUR with Spatial Durbin Error Model (called
SUR-SDEM), SUR with Spatial Autoregressive terms and Spatial
Autoregressive Disturbances (called SUR-SARAR) and SUR with Spatially
Independent Model (called SUR-SIM). The methodology of these models can be
found in next references Mur, J., Lopez, F., and Herrera, M. (2010)
<doi:10.1080/17421772.2010.516443> Lopez, F.A., Mur, J., and Angulo, A.
(2014) <doi:10.1007/s00168-014-0624-2>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
