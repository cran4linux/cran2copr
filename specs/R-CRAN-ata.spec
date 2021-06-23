%global __brp_check_rpaths %{nil}
%global packname  ata
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Test Assembly

License:          LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-stats 
Requires:         R-CRAN-lpSolve 
Requires:         R-stats 

%description
Provides a collection of psychometric methods to process item metadata and
use target assessment and measurement blueprint constraints to assemble a
test form. Currently two automatic test assembly (ata) approaches are
enabled. For example, the weighted (positive) deviations method, wdm(),
proposed by Swanson and Stocking (1993) <doi:10.1177/014662169301700205>
was implemented in its full specification allowing for both item selection
as well as test form refinement. The linear constraint programming
approach, atalp(), uses the linear equation solver by Berkelaar et. al
(2014) <http://lpsolve.sourceforge.net/5.5/> to enable a variety of
approaches to select items.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
