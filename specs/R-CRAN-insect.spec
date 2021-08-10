%global __brp_check_rpaths %{nil}
%global packname  insect
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Informatic Sequence Classification Trees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 3.0
BuildRequires:    R-CRAN-phylogram >= 2.0.0
BuildRequires:    R-CRAN-aphid >= 1.3.1
BuildRequires:    R-CRAN-kmer >= 1.1.0
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-ape >= 3.0
Requires:         R-CRAN-phylogram >= 2.0.0
Requires:         R-CRAN-aphid >= 1.3.1
Requires:         R-CRAN-kmer >= 1.1.0
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-seqinr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-xml2 

%description
Provides tools for probabilistic taxon assignment with informatic sequence
classification trees. See Wilkinson et al (2018)
<doi:10.7287/peerj.preprints.26812v1>.

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
