%global packname  modeltime.gluonts
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          'GluonTS' Deep Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-modeltime >= 0.3.1
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-timetk 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-fs 
Requires:         R-CRAN-modeltime >= 0.3.1
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-timetk 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-fs 

%description
Use the 'GluonTS' deep learning library inside of 'modeltime'. Available
models include 'DeepAR', 'N-BEATS', and 'N-BEATS' Ensemble. Refer to
"GluonTS - Probabilistic Time Series Modeling"
(<https://ts.gluon.ai/index.html>).

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
