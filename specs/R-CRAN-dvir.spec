%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dvir
%global packver   3.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Disaster Victim Identification

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pedtools >= 2.6.0
BuildRequires:    R-CRAN-forrel >= 1.5.2
BuildRequires:    R-CRAN-pedprobr >= 0.8.0
BuildRequires:    R-CRAN-verbalisr >= 0.7.1
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pedFamilias 
BuildRequires:    R-CRAN-ribd 
Requires:         R-CRAN-pedtools >= 2.6.0
Requires:         R-CRAN-forrel >= 1.5.2
Requires:         R-CRAN-pedprobr >= 0.8.0
Requires:         R-CRAN-verbalisr >= 0.7.1
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pedFamilias 
Requires:         R-CRAN-ribd 

%description
Joint DNA-based disaster victim identification (DVI), as described in
Vigeland and Egeland (2021) <doi:10.21203/rs.3.rs-296414/v1>.
Identification is performed by optimising the joint likelihood of all
victim samples and reference individuals. Individual identification
probabilities, conditional on all available information, are derived from
the joint solution in the form of posterior pairing probabilities. 'dvir'
is part of the 'pedsuite' collection of packages for pedigree analysis.

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
