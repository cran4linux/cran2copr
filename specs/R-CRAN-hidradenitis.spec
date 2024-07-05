%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hidradenitis
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Clinical Scores for Hidradenitis Suppurativa (HS), a Dermatologic Disease

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-checkmate 

%description
Calculate clinical scores for hidradenitis suppurativa (HS), a
dermatologic disease.  The scores are typically used for evaluation of
efficacy in clinical trials.  The scores are not commonly used in clinical
practice.  The specific scores implemented are Hidradenitis Suppurativa
Clinical Response (HiSCR) (Kimball, et al. (2015)
<doi:10.1111/jdv.13216>), Hidradenitis Suppurativa Area and Severity Index
Revised (HASI-R) (Goldfarb, et al. (2020) <doi:10.1111/bjd.19565>),
hidradenitis suppurativa Physician Global Assessment (HS PGA) (Marzano, et
al. (2020) <doi:10.1111/jdv.16328>), and the International Hidradenitis
Suppurativa Severity Score System (IHS4) (Zouboulis, et al. (2017)
<doi:10.1111/bjd.15748>).

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
