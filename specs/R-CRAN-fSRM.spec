%global packname  fSRM
%global packver   0.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          Social Relations Analyses with Roles ("Family SRM")

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-foreign 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 

%description
Social Relations Analysis with roles ("Family SRM") are computed, using a
structural equation modeling approach. Groups ranging from three members
up to an unlimited number of members are supported and the mean structure
can be computed. Means and variances can be compared between different
groups of families and between roles.

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
