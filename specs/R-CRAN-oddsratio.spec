%global packname  oddsratio
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Odds Ratio Calculation for GAM(M)s & GLM(M)s

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-mgcv 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 

%description
Simplified odds ratio calculation of GAM(M)s & GLM(M)s.  Provides
structured output (data frame) of all predictors and their corresponding
odds ratios and confident intervals for further analyses.  It helps to
avoid false references of predictors and increments by specifying these
parameters in a list instead of using 'exp(coef(model))' (standard
approach of odds ratio calculation for GLMs) which just returns a plain
numeric output.  For GAM(M)s, odds ratio calculation is highly simplified
with this package since it takes care of the multiple 'predict()' calls of
the chosen predictor while holding other predictors constant.  Also, this
package allows odds ratio calculation of percentage steps across the whole
predictor distribution range for GAM(M)s.  In both cases, confident
intervals are returned additionally.  Calculated odds ratio of GAM(M)s can
be inserted into the smooth function plot.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
