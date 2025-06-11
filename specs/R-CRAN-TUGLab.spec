%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TUGLab
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Laboratory for TU Games

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rcdd 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-volesti 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rcdd 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-volesti 

%description
Cooperative game theory models decision-making situations in which a group
of agents, called players, may achieve certain benefits by cooperating to
reach an optimal outcome. It has great potential in different fields,
since it offers a scenario to analyze and solve problems in which
cooperation is essential to achieve a common goal. The 'TUGLab'
(Transferable Utility Games Laboratory) R package contains a set of
scripts that could serve as a helpful complement to the books and other
materials used in courses on cooperative game theory, and also as a
practical tool for researchers working in this field. The 'TUGLab' project
was born in 2006 trying to highlight the geometrical aspects of the theory
of cooperative games for 3 and 4 players. 'TUGlabWeb' is an online
platform on which the basic functions of 'TUGLab' are implemented, and it
is being used all over the world as a resource in degree, master's and
doctoral programs. This package is an extension of the first versions and
enables users to work with games in general (computational restrictions
aside). The user can check properties of games, compute well-known games
and calculate several set-valued and single-valued solutions such as the
core, the Shapley value, the nucleolus or the core-center. The package
also illustrates how the Shapley value flexibly adapts to various
cooperative game settings, including weighted players and coalitions, a
priori unions, and restricted communication structures. In keeping with
the original philosophy of the first versions, special emphasis is placed
on the graphical representation of the solution concepts for 3 and 4
players.

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
