%global __brp_check_rpaths %{nil}
%global packname  kin.cohort
%global packver   0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Kin-Cohort Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-survival 
Requires:         R-survival 

%description
Analysis of kin-cohort studies. kin.cohort provides estimates of
age-specific cumulative risk of a disease for carriers and noncarriers of
a mutation. The cohorts are retrospectively built from relatives of
probands for whom the genotype is known. Currently the method of moments
and marginal maximum likelihood are implemented. Confidence intervals are
calculated from bootstrap samples. Most of the code is a translation from
previous 'MATLAB' code by N. Chatterjee.

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
