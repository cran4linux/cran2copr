%global __brp_check_rpaths %{nil}
%global packname  idar
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Individual Diversity-Area Relationships

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-spatstat >= 2.0.0
BuildRequires:    R-CRAN-FD 
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.core 
BuildRequires:    R-CRAN-spatstat.random 
Requires:         R-CRAN-spatstat >= 2.0.0
Requires:         R-CRAN-FD 
Requires:         R-CRAN-picante 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.core 
Requires:         R-CRAN-spatstat.random 

%description
Computes and tests individual (species, phylogenetic and functional)
diversity-area relationships, i.e., how species-, phylogenetic- and
functional-diversity varies with spatial scale around the individuals of
some species in a community. See applications of these methods in Wiegand
et al. (2007) <doi:10.1073/pnas.0705621104> or Chacon-Labella et al.
(2016) <doi:10.1007/s00442-016-3547-z>.

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
