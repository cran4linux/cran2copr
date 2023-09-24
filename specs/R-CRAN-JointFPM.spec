%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  JointFPM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Parametric Model for Estimating the Mean Number of Events

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival >= 3.2.13
BuildRequires:    R-CRAN-rstpm2 >= 1.5.2
BuildRequires:    R-CRAN-data.table >= 1.14.2
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-rmutil 
Requires:         R-CRAN-survival >= 3.2.13
Requires:         R-CRAN-rstpm2 >= 1.5.2
Requires:         R-CRAN-data.table >= 1.14.2
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-rmutil 

%description
Implementation of a parametric joint model for modelling recurrent and
competing event processes using generalised survival models. The joint
model can subsequently be used to predict the mean number of events in the
presence of competing risks at different time points. Comparisons of the
mean number of event functions, e.g. the differences in mean number of
events between two exposure groups, are also available.

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
