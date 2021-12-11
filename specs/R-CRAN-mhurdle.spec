%global __brp_check_rpaths %{nil}
%global packname  mhurdle
%global packver   1.3-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Hurdle Tobit Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-truncreg 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-prediction 
BuildRequires:    R-CRAN-margins 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-truncreg 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-prediction 
Requires:         R-CRAN-margins 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-numDeriv 

%description
Estimation of models with zero left-censored variables. Null values may be
caused by a selection process Cragg (1971) <doi:10.2307/1909582>,
insufficient resources Tobin (1958) <doi:10.2307/1907382> or infrequency
of purchase Deaton and Irish (1984) <doi:10.1016/0047-2727(84)90067-7>.

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
