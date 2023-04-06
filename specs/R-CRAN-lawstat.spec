%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lawstat
%global packver   3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Biostatistics, Public Policy, and Law

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Kendall 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-Kendall 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rdpack 

%description
Statistical tests widely utilized in biostatistics, public policy, and
law. Along with the well-known tests for equality of means and variances,
randomness, and measures of relative variability, the package contains new
robust tests of symmetry, omnibus and directional tests of normality, and
their graphical counterparts such as robust QQ plot, robust trend tests
for variances, etc. All implemented tests and methods are illustrated by
simulations and real-life examples from legal statistics, economics, and
biostatistics.

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
