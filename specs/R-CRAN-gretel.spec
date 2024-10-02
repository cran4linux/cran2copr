%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gretel
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Path Analysis for Social Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-ResistorArray >= 1.0.32
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-ResistorArray >= 1.0.32
Requires:         R-CRAN-Rcpp >= 1.0.0

%description
The social network literature features numerous methods for assigning
value to paths as a function of their ties. 'gretel' systemizes these
approaches, casting them as instances of a generalized path value function
indexed by a penalty parameter. The package also calculates probabilistic
path value and identifies optimal paths in either value framework.
Finally, proximity matrices can be generated in these frameworks that
capture high-order connections overlooked in primitive adjacency
sociomatrices. Novel methods are described in Buch (2019)
<https://davidbuch.github.io/analyzing-networks-with-gretel.html>. More
traditional methods are also implemented, as described in Yang, Knoke
(2001) <doi:10.1016/S0378-8733(01)00043-0>.

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
