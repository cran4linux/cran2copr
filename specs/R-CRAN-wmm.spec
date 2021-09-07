%global __brp_check_rpaths %{nil}
%global packname  wmm
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          World Magnetic Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Calculate magnetic field at a given location and time according to the
World Magnetic Model (WMM). Both the main field and secular variation
components are returned. This functionality is useful for physicists and
geophysicists who need orthogonal components from WMM. Currently, this
package supports annualized time inputs between 2000 and 2025. If desired,
users can specify which WMM version to use, e.g., the original WMM2015
release or the recent out-of-cycle WMM2015 release. Methods used to
implement WMM, including the Gauss coefficients for each release, are
described in the following publications: Chulliat et al (2020)
<doi:10.25923/ytk1-yx35>, Chulliat et al (2019) <doi:10.25921/xhr3-0t19>,
Chulliat et al (2015) <doi:10.7289/V5TB14V7>, Maus et al (2010)
<https://www.ngdc.noaa.gov/geomag/WMM/data/WMMReports/WMM2010_Report.pdf>,
McLean et al (2004)
<https://www.ngdc.noaa.gov/geomag/WMM/data/WMMReports/TRWMM_2005.pdf>, and
Macmillian et al (2000)
<https://www.ngdc.noaa.gov/geomag/WMM/data/WMMReports/wmm2000.pdf>.

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
