%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psyverse
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Decentralized Unequivocality in Psychological Science

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.0.0
BuildRequires:    R-CRAN-yaml >= 2.1.19
BuildRequires:    R-CRAN-yum >= 0.0.1
Requires:         R-stats >= 3.0.0
Requires:         R-CRAN-yaml >= 2.1.19
Requires:         R-CRAN-yum >= 0.0.1

%description
The constructs used to study the human psychology have many definitions
and corresponding instructions for eliciting and coding qualitative data
pertaining to constructs' content and for measuring the constructs. This
plethora of definitions and instructions necessitates unequivocal
reference to specific definitions and instructions in empirical and
secondary research. This package implements a human- and machine-readable
standard for specifying construct definitions and instructions for
measurement and qualitative research based on 'YAML'. This standard
facilitates systematic unequivocal reference to specific construct
definitions and corresponding instructions in a decentralized manner (i.e.
without requiring central curation; Peters (2020)
<doi:10.31234/osf.io/xebhn>).

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
