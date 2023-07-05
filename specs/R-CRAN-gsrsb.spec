%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gsrsb
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Group Sequential Refined Secondary Boundary

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-CRAN-ldbounds >= 2.0.0
BuildRequires:    R-CRAN-xtable >= 1.8.0
BuildRequires:    R-CRAN-mvtnorm >= 1.1.0
Requires:         R-stats >= 4.0.0
Requires:         R-CRAN-ldbounds >= 2.0.0
Requires:         R-CRAN-xtable >= 1.8.0
Requires:         R-CRAN-mvtnorm >= 1.1.0

%description
A gate-keeping procedure to test a primary and a secondary endpoint in a
group sequential design with multiple interim looks. Computations related
to group sequential primary and secondary boundaries. Refined secondary
boundaries are calculated for a gate-keeping test on a primary and a
secondary endpoint in a group sequential design with multiple interim
looks. The choices include both the standard boundaries and the boundaries
using error spending functions. See Tamhane et al. (2018), "A gatekeeping
procedure to test a primary and a secondary endpoint in a group sequential
design with multiple interim looks", Biometrics, 74(1), 40-48.

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
