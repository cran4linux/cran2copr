%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  POMS
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetic Organization of Metagenomic Signals

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.3.0
BuildRequires:    R-CRAN-ape >= 3.0
BuildRequires:    R-CRAN-phylolm >= 2.6
BuildRequires:    R-CRAN-phangorn >= 2.0.0
BuildRequires:    R-CRAN-XNomial >= 1.0.4
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-utils 
Requires:         R-parallel >= 3.3.0
Requires:         R-CRAN-ape >= 3.0
Requires:         R-CRAN-phylolm >= 2.6
Requires:         R-CRAN-phangorn >= 2.0.0
Requires:         R-CRAN-XNomial >= 1.0.4
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-MASS 
Requires:         R-utils 

%description
Code to identify functional enrichments across diverse taxa in
phylogenetic tree, particularly where these taxa differ in abundance
across samples in a non-random pattern. The motivation for this approach
is to identify microbial functions encoded by diverse taxa that are at
higher abundance in certain samples compared to others, which could
indicate that such functions are broadly adaptive under certain
conditions. See 'GitHub' repository for tutorial and examples:
<https://github.com/gavinmdouglas/POMS/wiki>. Citation: Gavin M. Douglas,
Molly G. Hayes, Morgan G. I. Langille, Elhanan Borenstein (2022)
<doi:10.1093/bioinformatics/btac655>.

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
