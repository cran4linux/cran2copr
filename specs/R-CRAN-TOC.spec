%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TOC
%global packver   0.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Total Operating Characteristic Curve and ROC Curve

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-bit 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-bit 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Construction of the Total Operating Characteristic (TOC) Curve and the
Receiver (aka Relative) Operating Characteristic (ROC) Curve for spatial
and non-spatial data. The TOC method is a modification of the ROC method
which measures the ability of an index variable to diagnose either
presence or absence of a characteristic. The diagnosis depends on whether
the value of an index variable is above a threshold. Each threshold
generates a two-by-two contingency table, which contains four entries:
hits (H), misses (M), false alarms (FA), and correct rejections (CR).
While ROC shows for each threshold only two ratios, H/(H + M) and FA/(FA +
CR), TOC reveals the size of every entry in the contingency table for each
threshold (Pontius Jr., R.G., Si, K. 2014.
<doi:10.1080/13658816.2013.862623>).

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
