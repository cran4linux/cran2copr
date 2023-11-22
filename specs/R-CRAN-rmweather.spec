%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmweather
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Conduct Meteorological Normalisation and Counterfactual Modelling for Air Quality Data

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.1
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pdp 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-dplyr >= 1.0.1
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pdp 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-cli 

%description
An integrated set of tools to allow data users to conduct meteorological
normalisation and counterfactual modelling for air quality data. The
meteorological normalisation technique uses predictive random forest
models to remove variation of pollutant concentrations so trends and
interventions can be explored in a robust way. For examples, see Grange et
al. (2018) <doi:10.5194/acp-18-6223-2018> and Grange and Carslaw (2019)
<doi:10.1016/j.scitotenv.2018.10.344>. The random forest models can also
be used for counterfactual or business as usual (BAU) modelling by using
the models to predict, from the model's perspective, the future. For an
example, see Grange et al. (2021) <doi:10.5194/acp-2020-1171>.

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
