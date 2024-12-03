%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  orthGS
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Orthology vs Paralogy Relationships among Glutamine Synthetase from Plants

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-bio3d 
BuildRequires:    R-CRAN-castor 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-TreeTools 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-bio3d 
Requires:         R-CRAN-castor 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-TreeTools 

%description
Tools to analyze and infer orthology and paralogy relationships between
glutamine synthetase proteins in seed plants.

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
