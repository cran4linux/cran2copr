%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fwb
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fractional Weighted Bootstrap

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-chk 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-chk 
Requires:         R-CRAN-pbapply 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 

%description
An implementation of the fractional weighted bootstrap to be used as a
drop-in for functions in the 'boot' package. The fractional weighted
bootstrap (also known as the Bayesian bootstrap) involves drawing weights
randomly that are applied to the data rather than resampling units from
the data. See Xu et al. (2020) <doi:10.1080/00031305.2020.1731599> for
details.

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
