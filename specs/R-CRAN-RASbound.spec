%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RASbound
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bounded RAS / Biproportional Matrix Balancing with Cell-Level Constraints

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Implements the RAS method for adjusting a matrix to match target row and
column totals. In RAS, a matrix A is multiplied on the left by a diagonal
matrix R and on the right by a diagonal matrix S, which gives the method
its name. It is also known as biproportional matrix balancing, iterative
proportional fitting (IPF) or raking. The package extends it with lower
and upper bounds on individual cells. Provides several algorithmic
variants for handling bound violations: hard cell-freezing with
simultaneous, sequential, or hybrid fixation; two dependency-free
clamp-and-compensate heuristics (proportional redistribution and iterative
renormalization); and a naive unconstrained-recompute baseline; together
with thin wrapper functions exposing equivalent bounded-calibration
methods from the 'survey' package under a common interface. Intended for
updating or regionalizing input-output tables, social accounting matrices
(SAMs), and other applications where classic RAS/IPF is used but
cell-level plausibility ranges must be respected. References: Deming and
Stephan (1940) <doi:10.1214/aoms/1177731829> Deville, Saerndal and Sautory
(1993) <doi:10.1080/01621459.1993.10476369> Acknowledgements: The author
wishes to thank Conselleria de Educacion, Cultura y Universidades,
Generalitat Valenciana (grant CIAICO/2023/031) for supporting this
research.

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
