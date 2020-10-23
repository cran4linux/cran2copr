%global packname  embryogrowth
%global packver   8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Analyze the Thermal Reaction Norm of Embryo Growth

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-HelpersMG >= 4.0
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-parallel 
Requires:         R-CRAN-HelpersMG >= 4.0
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-numDeriv 
Requires:         R-parallel 

%description
Tools to analyze the embryo growth and the sexualisation thermal reaction
norms.

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
