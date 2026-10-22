%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cldreducer
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reduce Compact Letter Displays

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-highs >= 1.14.0
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-highs >= 1.14.0
Requires:         R-CRAN-Matrix 

%description
Reduces compact letter displays (CLDs) of all pairwise comparisons. A CLD
gives two groups a common letter exactly when they are not significantly
different. The package finds a display with the fewest letter assignments
that keeps every one of these relationships. This is the
assignment-minimum clique covering problem of Ennis, Fayle, and Ennis
(2012) <doi:10.1145/2133803.2275596>, solved as a mixed-integer linear
program with 'HiGHS'. Among the displays with the fewest assignments, it
returns one fixed canonical display, so the result does not depend on the
solver. The package includes the wheat yield example of Piepho (2004)
<doi:10.1198/1061860043515>.

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
