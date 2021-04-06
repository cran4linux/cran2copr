%global packname  modeltime.h2o
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Modeltime 'H2O' Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-timetk >= 2.6.0
BuildRequires:    R-CRAN-modeltime >= 0.4.1
BuildRequires:    R-CRAN-parsnip >= 0.1.4
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-h2o 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-fs 
Requires:         R-CRAN-timetk >= 2.6.0
Requires:         R-CRAN-modeltime >= 0.4.1
Requires:         R-CRAN-parsnip >= 0.1.4
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-h2o 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-fs 

%description
Use the 'H2O' machine learning library inside of 'modeltime'. Available
models include 'AutoML' for Automatic Machine Learning. Please see H2O.ai
for more information <https://github.com/h2oai/h2o-3>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
