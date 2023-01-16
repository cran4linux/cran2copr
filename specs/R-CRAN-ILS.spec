%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ILS
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Interlaboratory Study

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-depthTools 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-depthTools 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
It performs interlaboratory studies (ILS) to detect those laboratories
that provide non-consistent results when comparing to others. It permits
to work simultaneously with various testing materials, from standard
univariate, and functional data analysis (FDA) perspectives. The
univariate approach based on ASTM E691-08 consist of estimating the
Mandel's h and k statistics to identify those laboratories that provide
more significant different results, testing also the presence of outliers
by Cochran and Grubbs tests, Analysis of variance (ANOVA) techniques are
provided (F and Tuckey tests) to test differences in means corresponding
to different laboratories per each material. Taking into account the
functional nature of data retrieved in analytical chemistry, applied
physics and engineering (spectra, thermograms, etc.). ILS package provides
a FDA approach for finding the Mandel's k and h statistics distribution by
smoothing bootstrap resampling.

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
