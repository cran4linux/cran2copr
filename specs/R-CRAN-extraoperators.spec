%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  extraoperators
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extra Binary Relational and Logical Operators

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Speed up common tasks, particularly logical or relational comparisons and
routine follow up tasks such as finding the indices and subsetting.
Inspired by mathematics, where something like: 3 < x < 6 is a standard,
elegant and clear way to assert that x is both greater than 3 and less
than 6 (see for example
<https://en.wikipedia.org/wiki/Relational_operator>), a chaining operator
is implemented. The chaining operator, %%c%%, allows multiple relational
operations to be used in quotes on the right hand side for the same
object, on the left hand side. The %%e%% operator allows something like
set-builder notation (see for example
<https://en.wikipedia.org/wiki/Set-builder_notation>) to be used on the
right hand side. Operators have built in prefixes defined for all, any,
subset, and which to reduce the amount of code needed for common tasks,
such as return those values that are true.

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
