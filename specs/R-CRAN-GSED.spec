%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GSED
%global packver   2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Group Sequential Enrichment Design

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-survival >= 2.37.7
BuildRequires:    R-CRAN-R.utils >= 2.3.0
BuildRequires:    R-CRAN-rootSolve >= 1.6.6
BuildRequires:    R-CRAN-memoise >= 1.0.0
Requires:         R-CRAN-survival >= 2.37.7
Requires:         R-CRAN-R.utils >= 2.3.0
Requires:         R-CRAN-rootSolve >= 1.6.6
Requires:         R-CRAN-memoise >= 1.0.0

%description
Provides function to apply "Group sequential enrichment design
incorporating subgroup selection" (GSED) method proposed by Magnusson and
Turnbull (2013) <doi:10.1002/sim.5738>.

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
