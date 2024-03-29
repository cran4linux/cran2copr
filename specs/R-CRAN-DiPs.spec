%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DiPs
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          1%{?dist}%{?buildtag}
Summary:          Directional Penalties for Optimal Matching in Observational Studies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlemon 
Requires:         R-stats 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-mvnfast 
Requires:         R-methods 
Requires:         R-CRAN-rlemon 

%description
Improves the balance of optimal matching with near-fine balance by giving
penalties on the unbalanced covariates with the unbalanced directions.
Many directional penalties can also be viewed as Lagrange multipliers,
pushing a matched sample in the direction of satisfying a linear
constraint that would not be satisfied without penalization. Yu and
Rosenbaum (2019) <doi:10.1111/biom.13098>.

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
