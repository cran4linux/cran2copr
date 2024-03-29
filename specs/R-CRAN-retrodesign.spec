%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  retrodesign
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Type S (Sign) and Type M (Magnitude) Errors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
Requires:         R-graphics 

%description
Provides tools for working with Type S (Sign) and Type M (Magnitude)
errors, as proposed in Gelman and Tuerlinckx (2000)
<doi:10.1007/s001800000040> and Gelman & Carlin (2014)
<doi:10.1177/1745691614551642>. In addition to simply calculating the
probability of Type S/M error, the package includes functions for
calculating these errors across a variety of effect sizes for comparison,
and recommended sample size given "tolerances" for Type S/M errors. To
improve the speed of these calculations, closed forms solutions for the
probability of a Type S/M error from Lu, Qiu, and Deng (2018)
<doi:10.1111/bmsp.12132> are implemented. As of 1.0.0, this includes
support only for simple research designs. See the package vignette for a
fuller exposition on how Type S/M errors arise in research, and how to
analyze them using the type of design analysis proposed in the above
papers.

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
