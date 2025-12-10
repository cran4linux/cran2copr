%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robmed
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          (Robust) Mediation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg >= 5.36
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-sn >= 1.5.4
BuildRequires:    R-CRAN-boot >= 1.3.20
BuildRequires:    R-CRAN-robustbase >= 0.92.7
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-quantreg >= 5.36
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-sn >= 1.5.4
Requires:         R-CRAN-boot >= 1.3.20
Requires:         R-CRAN-robustbase >= 0.92.7
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-utils 

%description
Perform mediation analysis via the fast-and-robust bootstrap test ROBMED
(Alfons, Ates & Groenen, 2022a; <doi:10.1177/1094428121999096>), as well
as various other methods. Details on the implementation and code examples
can be found in Alfons, Ates, and Groenen (2022b)
<doi:10.18637/jss.v103.i13>. Further discussion on robust mediation
analysis can be found in Alfons & Schley (2025) <doi:10.1002/wics.70051>.

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
