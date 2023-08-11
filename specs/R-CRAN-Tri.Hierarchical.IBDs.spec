%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Tri.Hierarchical.IBDs
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tri-Hierarchical IBDs (Tri- Hierarchical Incomplete Block Designs)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Tri-hierarchical incomplete block design is defined as an arrangement of v
treatments each replicated r times in a three system of blocks if, each
block of the first system contains m_1 blocks of second system and each
block of the second system contains m_2 blocks of the third system.
Ignoring the first and second system of blocks, it leaves an incomplete
block design with b_3 blocks of size k_3i units; ignoring first and third
system of blocks, it leaves an incomplete block design with b_2 blocks
each of size k_2i units and ignoring the second and third system of
blocks, it leaves an incomplete block design with b_1 blocks each of size
k_1 units. For dealing with experimental circumstances where there are
three nested sources of variation, a tri-hierarchical incomplete block
design can be adopted. Tri - hierarchical incomplete block designs can
find application potential in obtaining mating-environmental designs for
breeding trials. To know more about nested block designs one can refer
Preece (1967) <doi:10.1093/biomet/54.3-4.479>. This package includes
series1(), series2(), series3() and series4() functions. This package
generates tri-hierarchical designs with six component designs under
certain parameter restrictions.

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
