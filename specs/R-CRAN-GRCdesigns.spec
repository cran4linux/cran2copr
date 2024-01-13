%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GRCdesigns
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Row-Column Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
When the number of treatments is large with limited experimental resources
then Row-Column(RC) designs with multiple units per cell can be used.
These designs are called Generalized Row-Column (GRC) designs and are
defined as designs with v treatments in p rows and q columns such that the
intersection of each row and column (cell) consists of k experimental
units. For example (Bailey & Monod (2001)<doi:10.1111/1467-9469.00235>),
to conduct an experiment for comparing 4 treatments using 4 plants with
leaves at 2 different heights row-column design with two units per cell
can be used. A GRC design is said to be structurally complete if
corresponding to the intersection of each row and column, there appears at
least two treatments. A GRC design is said to be structurally incomplete
if corresponding to the intersection of any row and column, there is at
least one cell which does not contain any treatment.

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
