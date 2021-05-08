%global packname  WienR
%global packver   0.1-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Derivatives of the Diffusion Density and Cumulative Distribution Function

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0

%description
Calculate the partial derivative of the first-passage time diffusion
probability density function (PDF) and cumulative distribution function
(CDF) with respect to the first-passage time t (only for PDF), the upper
barrier a, the drift rate v, the relative starting point w, the
non-decision time t0, the inter-trial variability of the drift rate sv,
the inter-trial variability of the rel. starting point sw, and the
inter-trial variability of the non-decision time st0. In addition the PDF
and CDF themselves are also provided. Most calculations are done on the
logarithmic scale to make it more stable. For the numerical integration we
used the C library cubature by Johnson, S. G. (2005-2013)
<https://github.com/stevengj/cubature>. Numerical integration is required
whenever sv, sw, and/or st0 is not zero. Note that numerical integration
reduces speed of the computation.

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
