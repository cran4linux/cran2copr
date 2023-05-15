%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pRepDesigns
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Partially Replicated (p-Rep) Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Early generation breeding trials are to be conducted in multiple
environments where it may not be possible to replicate all the lines in
each environment due to scarcity of resources. For such situations,
partially replicated (p-Rep) designs have wide application potential as
only a proportion of the test lines are replicated at each environment. A
collection of several utility functions related to p-Rep designs have been
developed. Here, the package contains six functions for a complete
stepwise analytical study of these designs. Five functions pRep1(),
pRep2(), pRep3(), pRep4() and pRep5(), are used to generate five new
series of p-Rep designs and also compute average variance factors and
canonical efficiency factors of generated designs. A fourth function
NCEV() is used to generate incidence matrix (N), information matrix (C),
canonical efficiency factor (E) and average variance factor (V). This
function is general in nature and can be used for studying the
characterization properties of any block design. A construction procedure
for p-Rep designs was given by Williams et al.(2011)
<doi:10.1002/bimj.201000102> which was tedious and time consuming. Here,
in this package, five different methods have been given to generate p-Rep
designs easily.

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
