%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LikertMakeR
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Synthesise and Correlate Rating-Scale Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DEoptim >= 2.2.0
Requires:         R-CRAN-DEoptim >= 2.2.0

%description
Synthesise and correlate rating-scale data with predefined first & second
moments and, optionally, predefined correlation matrix. The function,
`lexact()`, uses the 'DEoptim'
<https://CRAN.R-project.org/package=DEoptim> package, described in Mullen,
Ardia, Gil, Windover, & Cline (2011) <doi:10.18637/jss.v040.i06>, to
synthesise a vector of discrete values with predefined mean and standard
deviation exact to two decimal places, if feasible. The function,
`lfast()`, draws a random sample from a _Beta_ distribution which is
rescaled to give a vector with approximate first and second moments. It is
much faster than `lexact()` but not as precise. The function, `lcor()`,
systematically swaps values within each column of a data-frame so that
they are correlated to fit a predefined correlation matrix.

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
