%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SIPDIBGE
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Household Survey Packages Conducted by IBGE

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-PNADcIBGE >= 0.6.0
BuildRequires:    R-CRAN-COVIDIBGE >= 0.1.0
BuildRequires:    R-CRAN-PNSIBGE >= 0.1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-PNADcIBGE >= 0.6.0
Requires:         R-CRAN-COVIDIBGE >= 0.1.0
Requires:         R-CRAN-PNSIBGE >= 0.1.0
Requires:         R-CRAN-cli 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-png 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Provides access to packages developed for downloading, reading and
analyzing microdata from household surveys conducted by Brazilian
Institute of Geography and Statistics - IBGE. More information can be
obtained from the official website <https://www.ibge.gov.br/>.

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
