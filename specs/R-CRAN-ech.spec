%global packname  ech
%global packver   0.1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Toolbox for ECH with R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-haven >= 2.3.0
BuildRequires:    R-CRAN-survey >= 1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-srvyr >= 0.4.0
BuildRequires:    R-CRAN-geouy >= 0.2.3
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-statar 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-laeken 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-pdftables 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-textclean 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-attempt 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-haven >= 2.3.0
Requires:         R-CRAN-survey >= 1.2
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-srvyr >= 0.4.0
Requires:         R-CRAN-geouy >= 0.2.3
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-statar 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-laeken 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-pdftables 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-textclean 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-tidyselect 
Requires:         R-methods 
Requires:         R-CRAN-attempt 
Requires:         R-CRAN-curl 

%description
R toolbox for the processing of the Encuesta Continua de Hogares (ECH)
from Uruguay at <http://www.ine.gub.uy/encuesta-continua-de-hogares1>
conducted by the Instituto Nacional de Estadistica (INE).

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
