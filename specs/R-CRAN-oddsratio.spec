%global __brp_check_rpaths %{nil}
%global packname  oddsratio
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}%{?buildtag}
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
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-mgcv 
Requires:         R-stats 

%description
Simplified odds ratio calculation of GAM(M)s & GLM(M)s. Provides
structured output (data frame) of all predictors and their corresponding
odds ratios and confident intervals for further analyses.  It helps to
avoid false references of predictors and increments by specifying these
parameters in a list instead of using 'exp(coef(model))' (standard
approach of odds ratio calculation for GLMs) which just returns a plain
numeric output.  For GAM(M)s, odds ratio calculation is highly simplified
with this package since it takes care of the multiple 'predict()' calls of
the chosen predictor while holding other predictors constant. Also, this
package allows odds ratio calculation of percentage steps across the whole
predictor distribution range for GAM(M)s.  In both cases, confident
intervals are returned additionally. Calculated odds ratio of GAM(M)s can
be inserted into the smooth function plot.

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
%{rlibdir}/%{packname}
