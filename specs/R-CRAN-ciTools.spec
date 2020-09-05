%global packname  ciTools
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Confidence or Prediction Intervals, Quantiles, and Probabilities for Statistical Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-survival 
BuildRequires:    R-utils 
Requires:         R-CRAN-arm 
Requires:         R-boot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lme4 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-survival 
Requires:         R-utils 

%description
Functions to append confidence intervals, prediction intervals, and other
quantities of interest to data frames. All appended quantities are for the
response variable, after conditioning on the model and covariates. This
package has a data frame first syntax that allows for easy piping.
Currently supported models include (log-) linear, (log-) linear mixed,
generalized linear models, generalized linear mixed models, and
accelerated failure time models.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
