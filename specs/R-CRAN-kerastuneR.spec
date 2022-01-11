%global __brp_check_rpaths %{nil}
%global packname  kerastuneR
%global packver   0.1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'Keras Tuner'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-tidyjson 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-echarts4r 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-magick 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-tidyjson 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-echarts4r 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-magick 

%description
'Keras Tuner' <https://keras-team.github.io/keras-tuner/> is a hypertuning
framework made for humans. It aims at making the life of AI practitioners,
hypertuner algorithm creators and model designers as simple as possible by
providing them with a clean and easy to use API for hypertuning. 'Keras
Tuner' makes moving from a base model to a hypertuned one quick and easy
by only requiring you to change a few lines of code.

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
