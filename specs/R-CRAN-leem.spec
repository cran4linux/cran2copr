%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  leem
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Laboratory of Teaching to Statistics and Mathematics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tkRplotR 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-CRAN-manipulate 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-methods 
Requires:         R-tcltk 
Requires:         R-CRAN-tkRplotR 
Requires:         R-CRAN-tkrplot 
Requires:         R-CRAN-manipulate 
Requires:         R-CRAN-crayon 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-diagram 
Requires:         R-methods 

%description
An educational package for teaching statistics and mathematics in both
primary and higher education. The objective is to assist in the
teaching/learning process, both for student study planning and teacher
teaching strategies. The leem package aims to provide, in a simple yet
in-depth manner, knowledge of statistics and mathematics to anyone who
wants to study these areas of knowledge.

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
