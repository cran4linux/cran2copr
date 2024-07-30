%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  triplesmatch
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Match Triples Consisting of Two Controls and a Treated Unit or Vice Versa

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rcbalance 
BuildRequires:    R-CRAN-rlemon 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-optmatch 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-rcbalance 
Requires:         R-CRAN-rlemon 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-optmatch 
Requires:         R-utils 
Requires:         R-CRAN-rlang 

%description
Attain excellent covariate balance by matching two treated units and one
control unit or vice versa within strata. Using such triples, as opposed
to also allowing pairs of treated and control units, allows easier
interpretation of the two possible weights of observations and better
insensitivity to unmeasured bias in the test statistic. Using triples
instead of matching in a fixed 1:2 or 2:1 ratio allows for the match to be
feasible in more situations. The 'rrelaxiv' package, which provides an
alternative solver for the underlying network flow problems, carries an
academic license and is not available on CRAN, but may be downloaded from
'GitHub' at <https://github.com/josherrickson/rrelaxiv/>. The 'Gurobi'
commercial optimization software is required to use the two functions
[infsentrip()] and [triplesIP()]. These functions are not essential to the
main purpose of this package. A free academic license can be obtained at
<https://www.gurobi.com/features/academic-named-user-license/>. The
'gurobi' R package can then be installed following the instructions at
<https://www.gurobi.com/documentation/9.1/refman/ins_the_r_package.html>.

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
