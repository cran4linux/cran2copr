%global __brp_check_rpaths %{nil}
%global packname  mlt
%global packver   1.3-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Most Likely Transformations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-basefun >= 1.1.0
BuildRequires:    R-CRAN-variables >= 1.1.0
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-coneproj 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-basefun >= 1.1.0
Requires:         R-CRAN-variables >= 1.1.0
Requires:         R-CRAN-BB 
Requires:         R-CRAN-alabama 
Requires:         R-stats 
Requires:         R-CRAN-coneproj 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-Matrix 

%description
Likelihood-based estimation of conditional transformation models via the
most likely transformation approach described in Hothorn et al. (2018)
<DOI:10.1111/sjos.12291> and Hothorn (2020) <DOI:10.18637/jss.v092.i01>.

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
