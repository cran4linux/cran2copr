%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qCBA
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Postprocessing of Rule Classification Models Learnt on Quantized Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arules >= 1.7.4
BuildRequires:    R-CRAN-arc >= 1.3
BuildRequires:    R-CRAN-arulesCBA >= 1.2.5
BuildRequires:    R-CRAN-rJava >= 0.5.0
BuildRequires:    R-methods 
Requires:         R-CRAN-arules >= 1.7.4
Requires:         R-CRAN-arc >= 1.3
Requires:         R-CRAN-arulesCBA >= 1.2.5
Requires:         R-CRAN-rJava >= 0.5.0
Requires:         R-methods 

%description
Implements the Quantitative Classification-based on Association Rules
(QCBA) algorithm (<doi:10.1007/s10489-022-04370-x>). QCBA postprocesses
rule classification models making them typically smaller and in some cases
more accurate. Supported are 'CBA' implementations from 'rCBA',
'arulesCBA' and 'arc' packages, and 'CPAR', 'CMAR', 'FOIL2' and 'PRM'
implementations from 'arulesCBA' package and 'SBRL' implementation from
the 'sbrl' package. The result of the post-processing is an ordered
CBA-like rule list.

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
