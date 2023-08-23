%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RESTK
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Implementation of the RESTK Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-purrr 

%description
Implementation of the RESTK algorithm based on Markov's Inequality from
Vilardell, Sergi, Serra, Isabel, Mezzetti, Enrico, Abella, Jaume, Cazorla,
Francisco J. and Del Castillo, J. (2022). "Using Markov's Inequality with
Power-Of-k Function for Probabilistic WCET Estimation". In 34th Euromicro
Conference on Real-Time Systems (ECRTS 2022). Leibniz International
Proceedings in Informatics (LIPIcs) 231 20:1-20:24.
<doi:10.4230/LIPIcs.ECRTS.2022.20>. This work has been supported by the
European Research Council (ERC) under the European Union's Horizon 2020
research and innovation programme (grant agreement No. 772773).

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
