%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rtmpinvi
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Tabular Matrix Problems via Pseudoinverse Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rtmpinv >= 0.2.0
Requires:         R-CRAN-rtmpinv >= 0.2.0

%description
Provides an interactive wrapper for the 'tmpinv()' function from the
'rtmpinv' package with options extending its functionality to pre- and
post-estimation processing and streamlined incorporation of prior cell
information. The Tabular Matrix Problems via Pseudoinverse Estimation
(TMPinv) is a two-stage estimation method that reformulates structured
table-based systems - such as allocation problems, transaction matrices,
and input-output tables - as structured least-squares problems. Based on
the Convex Least Squares Programming (CLSP) framework, TMPinv solves
systems with row and column constraints, block structure, and optionally
reduced dimensionality by (1) constructing a canonical constraint form and
applying a pseudoinverse-based projection, followed by (2) a
convex-programming refinement stage to improve fit, coherence, and
regularization (e.g., via Lasso, Ridge, or Elastic Net).

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
