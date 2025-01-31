%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  javateak
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Javanese Teak Above Ground Biomass Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Simplifies the process of estimating above ground biomass components for
teak trees using a few basic inputs, based on the equations taken from the
journal "Allometric equations for estimating above ground biomass and leaf
area of planted teak (Tectona grandis) forests under agroforestry
management in East Java, Indonesia" (Purwanto & Shiba, 2006)
<doi:10.60409/forestresearch.76.0_1>. This function is most reliable when
applied to trees from the same region where the equations were developed,
specifically East Java, Indonesia. This function help to estimate the stem
diameter at the lowest major living branch (DB) using the stem diameter at
breast height with R^2 = 0.969. Estimate the branch dry weight (WB) using
the stem diameter at breast height and tree height (R^2 = 0.979). Estimate
the stem weight (WS) using the stem diameter at breast height and tree
height (R^2 = 0.997. Also estimate the leaf dry weight (WL) using the stem
diameter at the lowest major living branch (R^2 = 0.996).

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
