%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BiVariAn
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bivariate Automatic Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-epitools 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggprism 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-logistf 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rrtable 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-table1 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-car 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-epitools 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggprism 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-logistf 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rrtable 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-table1 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Simplify bivariate and regression analyses by automating result
generation, including summary tables, statistical tests, and customizable
graphs. It supports tests for continuous and dichotomous data, as well as
stepwise regression for linear, logistic, and Firth penalized logistic
models.  While not a substitute for tailored analysis, 'BiVariAn'
accelerates workflows and is expanding features like multilingual
interpretations of results.The methods for selecting significant
statistical tests, as well as the predictor selection in prediction
functions, can be referenced in the works of Marc Kery (2003)
<doi:10.1890/0012-9623(2003)84[92:NORDIG]2.0.CO;2> and Rainer Puhr (2017)
<doi:10.1002/sim.7273>.

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
