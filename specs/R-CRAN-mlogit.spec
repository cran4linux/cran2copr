%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlogit
%global packver   2.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multinomial Logit Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-dfidx 
BuildRequires:    R-CRAN-micsr 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-dfidx 
Requires:         R-CRAN-micsr 
Requires:         R-CRAN-numDeriv 

%description
Maximum likelihood estimation of random utility discrete choice models.
The software is described in Croissant (2020) <doi:10.18637/jss.v095.i11>
and the underlying methods in Train (2009) <doi:10.1017/CBO9780511805271>.

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
