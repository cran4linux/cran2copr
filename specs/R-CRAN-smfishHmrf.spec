%global packname  smfishHmrf
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hidden Markov Random Field for Spatial Transcriptomic Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-pracma >= 1.9.0
BuildRequires:    R-CRAN-fs >= 1.2
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-pracma >= 1.9.0
Requires:         R-CRAN-fs >= 1.2
Requires:         R-CRAN-Rdpack 

%description
Discovery of spatial patterns with Hidden Markov Random Field. This
package is designed for spatial transcriptomic data and single molecule
fluorescent in situ hybridization (FISH) data such as sequential
fluorescence in situ hybridization (seqFISH) and multiplexed error-robust
fluorescence in situ hybridization (MERFISH). The methods implemented in
this package are described in Zhu et al. (2018) <doi:10.1038/nbt.4260>.

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
