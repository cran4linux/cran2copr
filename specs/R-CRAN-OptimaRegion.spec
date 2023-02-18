%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OptimaRegion
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Confidence Regions for Optima of Response Surfaces

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-DepthProc 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-rsm 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Rdsdp 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-DepthProc 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-rsm 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Rdsdp 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-stringr 

%description
Computes confidence regions on the location of response surface optima.
Response surface models can be up to cubic polynomial models in up to 5
controllable factors, or Thin Plate Spline models in 2 controllable
factors.

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
