%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  embryogrowth
%global packver   8.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.7
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Analyze the Thermal Reaction Norm of Embryo Growth

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-HelpersMG >= 5.5
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-parallel 
Requires:         R-CRAN-HelpersMG >= 5.5
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-numDeriv 
Requires:         R-parallel 

%description
Tools to analyze the embryo growth and the sexualisation thermal reaction
norms. See <doi:10.7717/peerj.8451> for tsd functions; see
<doi:10.1016/j.jtherbio.2014.08.005> for thermal reaction norm of embryo
growth.

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
