%global __brp_check_rpaths %{nil}
%global packname  OSTE
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Survival Trees Ensemble

License:          GPL (>= 3.5.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-pec 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-prodlim 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-pec 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-prodlim 

%description
Function for growing survival trees ensemble ('Naz Gul', 'Nosheen Faiz',
'Dan Brawn', 'Rafal Kulakowski', 'Zardad Khan', and 'Berthold Lausen'
(2020) <arXiv:2005.09043>) is given. The trees are grown by the method of
random survival forest ('Marvin Wright', 'Andreas Ziegler' (2017)
<doi:10.18637/jss.v077.i01>). The survival trees grown are assessed for
both individual and collective performances. The ensemble can give
promising results on fewer survival trees selected in the final ensemble.

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
