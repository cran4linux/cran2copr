%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ebrahim.gof
%global packver   2.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit and Calibration Tests for Logistic Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-parallel 
Requires:         R-stats 

%description
Provides a unified battery of goodness-of-fit and calibration tests for
binary logistic regression, runnable in a single call via 'run.all.gof()'.
The package introduces the author's own tests aimed at sparse data --- the
omnibus Ebrahim-Farrington (EF) test, the Directed EF ('EDGE') test that
targets smooth calibration-shape departures, and a Cauchy-combination
ensemble --- and aggregates a wide range of classical and modern tests for
comparison, including Hosmer-Lemeshow, McCullagh, Osius-Rojek, le
Cessie-van Houwelingen, Stute-Zhu, the binary-adaptive 'BAGofT' test, and
the 'GiViTI' calibration test (each obtained from its own package, where
installed, and attributed to its authors). The tools are particularly
suited to sparse data, where the Hosmer-Lemeshow test loses power. For
more details see Hosmer (1980) <doi:10.1080/03610928008827941> and
Farrington (1996) <doi:10.1111/j.2517-6161.1996.tb02086.x>.

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
