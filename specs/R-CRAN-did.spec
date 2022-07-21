%global __brp_check_rpaths %{nil}
%global packname  did
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Treatment Effects with Multiple Periods and Groups

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-BMisc >= 1.4.4
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-DRDID 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-BMisc >= 1.4.4
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-DRDID 
Requires:         R-CRAN-generics 
Requires:         R-methods 
Requires:         R-CRAN-tidyr 

%description
The standard Difference-in-Differences (DID) setup involves two periods
and two groups -- a treated group and untreated group.  Many applications
of DID methods involve more than two periods and have individuals that are
treated at different points in time.  This package contains tools for
computing average treatment effect parameters in Difference in Differences
setups with more than two periods and with variation in treatment timing
using the methods developed in Callaway and Sant'Anna (2021)
<doi:10.1016/j.jeconom.2020.12.001>.  The main parameters are group-time
average treatment effects which are the average treatment effect for a
particular group at a a particular time.  These can be aggregated into a
fewer number of treatment effect parameters, and the package deals with
the cases where there is selective treatment timing, dynamic treatment
effects, calendar time effects, or combinations of these.  There are also
functions for testing the Difference in Differences assumption, and
plotting group-time average treatment effects.

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
