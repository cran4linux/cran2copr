%global __brp_check_rpaths %{nil}
%global packname  deltaccd
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Quantify Rhythmic Gene Co-Expression Relative to a Reference

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-doRNG >= 1.6.6
BuildRequires:    R-CRAN-statmod >= 1.4.30
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-scales >= 0.5.0
BuildRequires:    R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-doRNG >= 1.6.6
Requires:         R-CRAN-statmod >= 1.4.30
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-scales >= 0.5.0
Requires:         R-CRAN-rlang >= 0.4.11

%description
Infer progression of circadian rhythms in transcriptome data in which
samples are not labeled with time of day and coverage of the circadian
cycle may be incomplete. See Shilts et al. (2018)
<doi:10.7717/peerj.4327>.

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
