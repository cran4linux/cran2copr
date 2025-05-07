%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KOLaide
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Pick and Plot Key Opinion Leaders from a Network Given Constraints

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-utils 

%description
Assists researchers in choosing Key Opinion Leaders (KOLs) in a network to
help disseminate or encourage adoption of an innovation by other network
members. Potential KOL teams are evaluated using the ABCDE framework (Neal
et al., 2025 <doi:10.31219/osf.io/3vxy9_v1>). This framework which
considers: (1) the team members' Availability, (2) the Breadth of the
team's network coverage, (3) the Cost of recruiting a team of a given
size, and (4) the Diversity of the team's members, (5) which are pooled
into a single Evaluation score.

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
