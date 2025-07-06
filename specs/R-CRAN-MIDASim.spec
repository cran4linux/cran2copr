%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MIDASim
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulating Realistic Microbiome Data using 'MIDASim'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-scam 
BuildRequires:    R-stats 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-scam 
Requires:         R-stats 

%description
The 'MIDASim' package is a microbiome data simulator for generating
realistic microbiome datasets by adapting a user-provided template. It
supports the controlled introduction of experimental signals-such as
shifts in taxon relative abundances, prevalence, and sample library
sizes-to create distinct synthetic populations under diverse simulation
scenarios. For more details, see He et al. (2024)
<doi:10.1186/s40168-024-01822-z>.

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
