%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qlifetable
%global packver   0.0.2-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Managing and Building of Quarterly Life Tables

License:          EPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-methods 

%description
Manages, builds and computes statistics and datasets for the construction
of quarterly (sub-annual) life tables by exploiting micro-data from either
a general or an insured population. References: Pavía and Lledó (2022)
<doi:10.1111/rssa.12769>. Pavía and Lledó (2023)
<doi:10.1017/asb.2023.16>. Acknowledgements: The authors wish to thank
Consellería de Educación, Universidades y Empleo, Generalitat Valenciana
(grant AICO/2021/257), Ministerio de Ciencia e Innovación (grant
PID2021-128228NB-I00) and Fundación Mapfre (grant 'Modelización espacial e
intra-anual de la mortalidad en España. Una herramienta automática para el
cálculo de productos de vida') for supporting this research.

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
