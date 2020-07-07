%global packname  simml
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Single-Index Models with Multiple-Links

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-plyr 
Requires:         R-mgcv 
Requires:         R-CRAN-plyr 

%description
A major challenge in estimating treatment decision rules from a randomized
clinical trial dataset with covariates measured at baseline lies in
detecting relatively small treatment effect modification-related
variability (i.e., the treatment-by-covariates interaction effects on
treatment outcomes) against a relatively large non-treatment-related
variability (i.e., the main effects of covariates on treatment outcomes).
The class of Single-Index Models with Multiple-Links is a novel
single-index model specifically designed to estimate a single-index (a
linear combination) of the covariates associated with the treatment effect
modification-related variability, while allowing a nonlinear association
with the treatment outcomes via flexible link functions. The models
provide a flexible regression approach to developing treatment decision
rules based on patients' data measured at baseline. We refer to Petkova,
Tarpey, Su, and Ogden (2017) <doi: 10.1093/biostatistics/kxw035> and "A
constrained single-index model for estimating interactions between a
treatment and covariates" (under review, 2019) for detail. The main
function of this package is simml().

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
