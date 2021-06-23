%global __brp_check_rpaths %{nil}
%global packname  tailDepFun
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Minimum Distance Estimation of Tail Dependence Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-SpatialExtremes 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-SpatialExtremes 
Requires:         R-CRAN-copula 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides functions implementing minimal distance estimation methods for
parametric tail dependence models, as proposed in Einmahl, J.H.J.,
Kiriliouk, A., Krajina, A., and Segers, J. (2016) <doi:10.1111/rssb.12114>
and Einmahl, J.H.J., Kiriliouk, A., and Segers, J. (2018)
<doi:10.1007/s10687-017-0303-7>.

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
