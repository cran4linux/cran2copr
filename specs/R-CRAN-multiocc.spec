%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multiocc
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fits Multivariate Spatio-Temporal Occupancy Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-interp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-coda 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-interp 

%description
Spatio-temporal multivariate occupancy models can handle multiple species
in occupancy models.  This method for fitting such models is described in
Hepler and Erhardt (2021) "A spatiotemporal model for multivariate
occupancy data"
<https://onlinelibrary.wiley.com/doi/abs/10.1002/env.2657>.

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
