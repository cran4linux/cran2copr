%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MARVEL
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Revealing Splicing Dynamics at Single-Cell Resolution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-Matrix >= 1.3.3
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-Matrix >= 1.3.3
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-methods 

%description
Alternative splicing represents an additional and underappreciated layer
of complexity underlying gene expression profiles. Nevertheless, there
remains hitherto a paucity of software to investigate splicing dynamics at
single-cell resolution. 'MARVEL' enables splicing analysis of single-cell
RNA-sequencing data generated from plate- and droplet-based library
preparation methods.

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
