%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  reflectR
%global packver   2.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Scoring of the Cognitive Reflection Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-stringr 

%description
Automatic coding of open-ended responses to the Cognitive Reflection Test
(CRT), a widely used class of tests in cognitive science and psychology
that assess the tendency to override an initial intuitive (but incorrect)
answer and engage in reflection to reach a correct solution. The package
standardizes CRT response coding across datasets in cognitive psychology,
decision-making, and related fields. Automated coding reduces manual
effort and improves reproducibility by limiting variability from
subjective interpretation of open-ended responses. The package supports
automatic coding and machine scoring for the original English-language CRT
(Frederick, 2005) <doi:10.1257/089533005775196732>, CRT4 and CRT7 (Toplak
et al., 2014) <doi:10.1080/13546783.2013.844729>, CRT-long (Primi et al.,
2016) <doi:10.1002/bdm.1883>, and CRT-2 (Thomson & Oppenheimer, 2016)
<doi:10.1017/s1930297500007622>.

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
