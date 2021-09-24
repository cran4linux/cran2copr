%global __brp_check_rpaths %{nil}
%global packname  adoption
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          1%{?dist}%{?buildtag}
Summary:          Modelling Adoption Process in Marketing

License:          GPL (>= 3) | CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-RandomFieldsUtils >= 0.5.4
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tkrplot 
Requires:         R-CRAN-RandomFieldsUtils >= 0.5.4
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-quadprog 
Requires:         R-tcltk 
Requires:         R-CRAN-tkrplot 

%description
The classical Bass (1969) <doi:10.1287/mnsc.15.5.215> model and the agent
based models, such as that by Goldenberg, Libai and Muller (2010)
<doi:10.1016/j.ijresmar.2009.06.006> have been two different approaches to
model adoption processes in marketing. These two approaches can be unified
by explicitly modelling the utility functions. This package provides a GUI
that allows, in a unified way, the modelling of these two processes and
other processes.

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
