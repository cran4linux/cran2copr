%global packname  mvMISE
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          A General Framework of Multivariate Mixed-Effects SelectionModels

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-MASS 
Requires:         R-CRAN-lme4 
Requires:         R-MASS 

%description
Offers a general framework of multivariate mixed-effects models for the
joint analysis of multiple correlated outcomes with clustered data
structures and potential missingness proposed by Wang et al. (2018)
<doi:10.1093/biostatistics/kxy022>. The missingness of outcome values may
depend on the values themselves (missing not at random and non-ignorable),
or may depend on only the covariates (missing at random and ignorable), or
both. This package provides functions for two models: 1) mvMISE_b() allows
correlated outcome-specific random intercepts with a factor-analytic
structure, and 2) mvMISE_e() allows the correlated outcome-specific error
terms with a graphical lasso penalty on the error precision matrix. Both
functions are motivated by the multivariate data analysis on data with
clustered structures from labelling-based quantitative proteomic studies.
These models and functions can also be applied to univariate and
multivariate analyses of clustered data with balanced or unbalanced design
and no missingness.

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
