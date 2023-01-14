%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RNAsmc
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          RNA Secondary Structure Module Mining, Comparison and Plotting

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RRNA 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-circlize 
Requires:         R-CRAN-RRNA 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-circlize 

%description
Provides function for RNA secondary structure plotting, comparison and
module mining. Given a RNA secondary structure, you can obtain stem
regions, hairpin loops, internal loops, bulge loops and multibranch loops
of this RNA structure using this program. They are the basic modules of
RNA secondary structure. For each module you get, you can use this program
to label the RNA structure with a specific color. You can also use this
program to compare two RNA secondary structures to get a score that
represents similarity. Reference: Reuter JS, Mathews DH (2010)
<doi:10.1186/1471-2105-11-129>.

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
