%global packname  cem
%global packver   1.1.27
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.27
Release:          1%{?dist}%{?buildtag}
Summary:          Coarsened Exact Matching

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-nlme 
Requires:         R-tcltk 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-MatchIt 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-nlme 

%description
Implementation of the Coarsened Exact Matching algorithm discussed along
with its properties in Iacus, King, Porro (2011)
<DOI:10.1198/jasa.2011.tm09599>; Iacus, King, Porro (2012)
<DOI:10.1093/pan/mpr013> and Iacus, King, Porro (2019)
<DOI:10.1017/pan.2018.29>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
