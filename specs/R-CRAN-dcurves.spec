%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dcurves
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Decision Curve Analysis for Model Evaluation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-tibble >= 3.1.0
BuildRequires:    R-CRAN-glue >= 1.4.2
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.5
BuildRequires:    R-CRAN-broom >= 0.7.10
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-tibble >= 3.1.0
Requires:         R-CRAN-glue >= 1.4.2
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.5
Requires:         R-CRAN-broom >= 0.7.10
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-survival 

%description
Diagnostic and prognostic models are typically evaluated with measures of
accuracy that do not address clinical consequences. Decision-analytic
techniques allow assessment of clinical outcomes, but often require
collection of additional information may be cumbersome to apply to models
that yield a continuous result. Decision curve analysis is a method for
evaluating and comparing prediction models that incorporates clinical
consequences, requires only the data set on which the models are tested,
and can be applied to models that have either continuous or dichotomous
results. See the following references for details on the methods: Vickers
(2006) <doi:10.1177/0272989X06295361>, Vickers (2008)
<doi:10.1186/1472-6947-8-53>, and Pfeiffer (2020)
<doi:10.1002/bimj.201800240>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
