%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qPCRhelper
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          qPCR Ct Values to Expression Values

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rstatix >= 0.7.2
BuildRequires:    R-CRAN-ggpubr >= 0.5.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rstatix >= 0.7.2
Requires:         R-CRAN-ggpubr >= 0.5.0

%description
Computes normalized cycle threshold (Ct) values (delta Ct) from raw
quantitative polymerase chain reaction (qPCR) Ct values and conducts test
of significance using t.test(). Plots expression values based from
log2(2^(-1*delta delta Ct)) across groups per gene of interest. Methods
for calculation of delta delta Ct and relative expression (2^(-1*delta
delta Ct)) values are described in: Livak & Schmittgen, (2001)
<doi:10.1006/meth.2001.1262>.

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
