%global __brp_check_rpaths %{nil}
%global packname  MBHdesign
%global packver   2.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Designs for Ecological and Environmental Surveys

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-stats 
BuildRequires:    R-class 
BuildRequires:    R-parallel 
Requires:         R-mgcv 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-class 
Requires:         R-parallel 

%description
Provides spatially balanced designs from a set of (contiguous) potential
sampling locations in a study region for point-based and for
transect-based surveys. Accommodates, without detrimental effects on
spatial balance, sites that the researcher wishes to include in the survey
for reasons other than the current randomisation (legacy sites).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
