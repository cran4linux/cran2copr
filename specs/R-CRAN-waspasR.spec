%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  waspasR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tool Kit to Implement a W.A.S.P.A.S. Based Multi-Criteria Decision Analysis Solution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch

%description
Provides a set of functions to implement decision-making systems based on
the W.A.S.P.A.S. method (Weighted Aggregated Sum Product Assessment),
Chakraborty and Zavadskas (2012) <doi:10.5755/j01.eee.122.6.1810>. So this
package offers functions that analyze and validate the raw data, which
must be entered in a determined format; extract specific vectors and
matrices from this raw database; normalize the input data; calculate
rankings by intermediate methods; apply the lambda parameter for the main
method; and a function that does everything at once. The package has an
example database called choppers, with which the user can see how the
input data should be organized so that everything works as recommended by
the decision methods based on multiple criteria that this package solves.
Basically, the data are composed of a set of alternatives, which will be
ranked, a set of choice criteria, a matrix of values for each
Alternative-Criterion relationship, a vector of weights associated with
the criteria, since certain criteria are considered more important than
others, as well as a vector that defines each criterion as cost or
benefit, this determines the calculation formula, as there are those
criteria that we want the highest possible value (e.g. durability) and
others that we want the lowest possible value (e.g. price).

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
