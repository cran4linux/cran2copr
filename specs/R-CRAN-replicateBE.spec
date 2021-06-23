%global __brp_check_rpaths %{nil}
%global packname  replicateBE
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Average Bioequivalence with Expanding Limits (ABEL)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-PowerTOST >= 1.5.3
BuildRequires:    R-CRAN-readxl >= 1.0.0
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-pbkrtest 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-PowerTOST >= 1.5.3
Requires:         R-CRAN-readxl >= 1.0.0
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-pbkrtest 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Performs comparative bioavailability calculations for Average
Bioequivalence with Expanding Limits (ABEL). Implemented are 'Method A'
and 'Method B' and the detection of outliers. If the design allows,
assessment of the empiric Type I Error and iteratively adjusting alpha to
control the consumer risk. Average Bioequivalence - optionally with a
tighter (narrow therapeutic index drugs) or wider acceptance range (Gulf
Cooperation Council, South Africa: Cmax) - is implemented as well.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
