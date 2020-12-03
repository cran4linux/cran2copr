%global packname  ordinalCont
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Ordinal Regression Analysis for Continuous Scales

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-Deriv 
Requires:         R-CRAN-boot 
Requires:         R-splines 
Requires:         R-CRAN-Deriv 

%description
A regression framework for response variables which are continuous
self-rating scales such as the Visual Analog Scale (VAS) used in pain
assessment, or the Linear Analog Self-Assessment (LASA) scales in quality
of life studies. These scales measure subjects' perception of an
intangible quantity, and cannot be handled as ratio variables because of
their inherent non-linearity. We treat them as ordinal variables, measured
on a continuous scale. A function (the g function) connects the scale with
an underlying continuous latent variable. The link function is the inverse
of the CDF of the assumed underlying distribution of the latent variable.
A variety of link functions are currently implemented. Such models are
described in Manuguerra et al (2020) <doi:10.18637/jss.v096.i08>.

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
