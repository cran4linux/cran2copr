%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  memoria
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantifying Ecological Memory in Palaeoecological Datasets and Other Long Time-Series

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-rlang 

%description
Quantifies ecological memory in long time-series using Random Forest
models ('Benito', 'Gil-Romera', and 'Birks' 2019 <doi:10.1111/ecog.04772>)
fitted with 'ranger' (Wright and Ziegler 2017
<doi:10.18637/jss.v077.i01>). Ecological memory is assessed by modeling a
response variable as a function of lagged predictors, distinguishing
endogenous memory (lagged response) from exogenous memory (lagged
environmental drivers). Designed for palaeoecological datasets and
simulated pollen curves from 'virtualPollen', but applicable to any long
time-series with environmental drivers and a biotic response.

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
