%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  musicMCT
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze the Structure of Musical Scales

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-igraph 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 

%description
Analysis of musical scales (& modes, grooves, etc.) in the vein of
Sherrill 2025 <doi:10.1215/00222909-11595194>. The initials MCT in the
package title refer to the article's title: "Modal Color Theory." Offers
support for conventional musical pitch class set theory as developed by
Forte (1973, ISBN: 9780300016109) and David Lewin (1987, ISBN:
9780300034936), as well as for the continuous geometries of Callender,
Quinn, & Tymoczko (2008) <doi:10.1126/science.1153021>. Identifies
structural properties of scales and calculates derived values (sign
vector, color number, brightness ratio, etc.). Creates plots such as
"brightness graphs" which visualize these properties.

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
