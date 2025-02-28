%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GPCsign
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Process Classification as Described in Bachoc et al. (2020)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-TruncatedNormal >= 2.3
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-TruncatedNormal >= 2.3
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-future 
Requires:         R-methods 
Requires:         R-stats 

%description
Parameter estimation and prediction of Gaussian Process Classifier models
as described in Bachoc et al. (2020) <doi:10.1007/S10898-020-00920-0>.
Important functions : gpcm(), predict.gpcm(), update.gpcm().

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
