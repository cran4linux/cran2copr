%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fwb
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fractional Weighted Bootstrap

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pbapply >= 1.7.2
BuildRequires:    R-CRAN-rlang >= 1.1.6
BuildRequires:    R-CRAN-chk >= 0.10.0
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-pbapply >= 1.7.2
Requires:         R-CRAN-rlang >= 1.1.6
Requires:         R-CRAN-chk >= 0.10.0
Requires:         R-CRAN-generics 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

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
