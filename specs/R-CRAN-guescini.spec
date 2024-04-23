%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  guescini
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Real-Time PCR Data Sets by Guescini et al. (2008)

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-tibble 

%description
Real-time quantitative polymerase chain reaction (qPCR) data by Guescini
et al. (2008) <doi:10.1186/1471-2105-9-326> in tidy format. This package
provides two data sets where the amplification efficiency has been
modulated: either by changing the amplification mix concentration, or by
increasing the concentration of IgG, a PCR inhibitor. Original raw data
files:
<https://static-content.springer.com/esm/art%%3A10.1186%%2F1471-2105-9-326/MediaObjects/12859_2008_2311_MOESM1_ESM.xls>
and
<https://static-content.springer.com/esm/art%%3A10.1186%%2F1471-2105-9-326/MediaObjects/12859_2008_2311_MOESM5_ESM.xls>.

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
