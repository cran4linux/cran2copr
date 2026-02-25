%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rgph
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pair Critical Points and Compute Persistent Homology of Reeb Graphs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava >= 0.5.0
BuildRequires:    R-CRAN-phutil 
Requires:         R-CRAN-rJava >= 0.5.0
Requires:         R-CRAN-phutil 

%description
Interface to the 'ReebGraphPairing' program to compute critical points of
Reeb graphs following Tu, Hajij, & Rosen (2019)
<doi:10.1007/978-3-030-33720-9_8> via the 'rJava' package. Also store Reeb
graphs in a minimal S3 class, convert between other network data
structures, and post-process pairing data to obtain extended persistent
homology following Carrière & Oudot (2018)
<doi:10.1007/s10208-017-9370-z>.

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
