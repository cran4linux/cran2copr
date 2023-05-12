%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ech
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Downloading and Processing Microdata from ECH-INE (Uruguay)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         /usr/bin/unrar
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-haven >= 2.3.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-srvyr >= 0.4.0
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-geouy 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-laeken 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-statar 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-haven >= 2.3.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-srvyr >= 0.4.0
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-geouy 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-laeken 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-statar 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
A consistent tool for downloading ECH data, processing them and generating
new indicators: poverty, education, employment, etc. All data are
downloaded from the official site of the National Institute of Statistics
at
<https://www.gub.uy/instituto-nacional-estadistica/datos-y-estadisticas/encuestas/encuesta-continua-hogares>.

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
