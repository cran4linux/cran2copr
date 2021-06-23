%global __brp_check_rpaths %{nil}
%global packname  eyedata
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Open Source Ophthalmic Data Sets Curated for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-dplyr >= 1.0.2

%description
Open source data allows for reproducible research and helps advance our
knowledge. The purpose of this package is to collate open source
ophthalmic data sets curated for direct use. This is real life data of
people with intravitreal injections with anti-vascular endothelial growth
factor (anti-VEGF), due to age-related macular degeneration or diabetic
macular edema. Associated publications of the data sets: Fu et al. (2020)
<doi:10.1001/jamaophthalmol.2020.5044>, Moraes et al (2020)
<doi:10.1016/j.ophtha.2020.09.025>, Fasler et al. (2019)
<doi:10.1136/bmjopen-2018-027441>, Arpa et al. (2020)
<doi:10.1136/bjophthalmol-2020-317161>, Kern et al. 2020,
<doi:10.1038/s41433-020-1048-0>.

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
