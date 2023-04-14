%global __brp_check_rpaths %{nil}
%global packname  drgee
%global packver   1.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.10
Release:          3%{?dist}%{?buildtag}
Summary:          Doubly Robust Generalized Estimating Equations

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-nleqslv 
Requires:         R-survival 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 

%description
Fit restricted mean models for the conditional association between an
exposure and an outcome, given covariates. Three methods are implemented:
O-estimation, where a nuisance model for the association between the
covariates and the outcome is used; E-estimation where a nuisance model
for the association between the covariates and the exposure is used, and
doubly robust (DR) estimation where both nuisance models are used. In
DR-estimation, the estimates will be consistent when at least one of the
nuisance models is correctly specified, not necessarily both. For more
information, see Zetterqvist and Sjölander (2015)
<doi:10.1515/em-2014-0021>.

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
