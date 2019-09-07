%global packname  urbin
%global packver   0.1-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}
Summary:          Unifying Estimation Results with Binary Dependent Variables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch

%description
Calculate unified measures that quantify the effect of a covariate on a
binary dependent variable (e.g., for meta-analyses). This can be
particularly important if the estimation results are obtained with
different models/estimators (e.g., linear probability model, logit,
probit, ...) and/or with different transformations of the explanatory
variable of interest (e.g., linear, quadratic, interval-coded, ...). The
calculated unified measures are: (a) semi-elasticities of linear,
quadratic, or interval-coded covariates and (b) effects of linear,
quadratic, interval-coded, or categorical covariates when a linear or
quadratic covariate changes between distinct intervals, the reference
category of a categorical variable or the reference interval of an
interval-coded variable needs to be changed, or some categories of a
categorical covariate or some intervals of an interval-coded covariate
need to be grouped together. Approximate standard errors of the unified
measures are also calculated. All methods that are implemented in this
package are described in the 'vignette' "Extracting and Unifying
Semi-Elasticities and Effect Sizes from Studies with Binary Dependent
Variables" that is included in this package.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
