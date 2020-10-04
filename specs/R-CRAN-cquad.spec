%global packname  cquad
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Conditional Maximum Likelihood for Quadratic Exponential Modelsfor Binary Panel Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-plm 
Requires:         R-MASS 
Requires:         R-CRAN-plm 

%description
Estimation, based on conditional maximum likelihood, of the quadratic
exponential model proposed by Bartolucci, F. & Nigro, V. (2010,
Econometrica) <DOI:10.3982/ECTA7531> and of a simplified and a modified
version of this model. The quadratic exponential model is suitable for the
analysis of binary longitudinal data when state dependence (further to the
effect of the covariates and a time-fixed individual intercept) has to be
taken into account. Therefore, this is an alternative to the dynamic logit
model having the advantage of easily allowing conditional inference in
order to eliminate the individual intercepts and then getting consistent
estimates of the parameters of main interest (for the covariates and the
lagged response). The simplified version of this model does not
distinguish, as the original model does, between the last time occasion
and the previous occasions. The modified version formulates in a different
way the interaction terms and it may be used to test in a easy way state
dependence as shown in Bartolucci, F., Nigro, V. & Pigini, C. (2018,
Econometric Reviews) <DOI:10.1080/07474938.2015.1060039>. The package also
includes estimation of the dynamic logit model by a pseudo conditional
estimator based on the quadratic exponential model, as proposed by
Bartolucci, F. & Nigro, V. (2012, Journal of Econometrics)
<DOI:10.1016/j.jeconom.2012.03.004>. For large time dimensions of the
panel, the computation of the proposed models involves a recursive
function adapted from Krailo M. D., & Pike M. C. (1984, Journal of the
Royal Statistical Society. Series C (Applied Statistics)).

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
