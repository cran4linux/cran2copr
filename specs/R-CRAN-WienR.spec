%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WienR
%global packver   0.3-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          Derivatives of the First-Passage Time Density and Cumulative Distribution Function, and Random Sampling from the (Truncated) First-Passage Time Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
First, we provide functions to calculate the partial derivative of the
first-passage time diffusion probability density function (PDF) and
cumulative distribution function (CDF) with respect to the first-passage
time t (only for PDF), the upper barrier a, the drift rate v, the relative
starting point w, the non-decision time t0, the inter-trial variability of
the drift rate sv, the inter-trial variability of the rel. starting point
sw, and the inter-trial variability of the non-decision time st0. In
addition the PDF and CDF themselves are also provided. Most calculations
are done on the logarithmic scale to make it more stable. Since the PDF,
CDF, and their derivatives are represented as infinite series, we give the
user the option to control the approximation errors with the argument
'precision'. For the numerical integration we used the C library cubature
by Johnson, S. G. (2005-2013) <https://github.com/stevengj/cubature>.
Numerical integration is required whenever sv, sw, and/or st0 is not zero.
Note that numerical integration reduces speed of the computation and the
precision cannot be guaranteed anymore. Therefore, whenever numerical
integration is used an estimate of the approximation error is provided in
the output list. Note: The large number of contributors (ctb) is due to
copying a lot of C/C++ code chunks from the GNU Scientific Library (GSL).
Second, we provide methods to sample from the first-passage time
distribution with or without user-defined truncation from above. The first
method is a new adaptive rejection sampler building on the works of Gilks
and Wild (1992; <doi:10.2307/2347565>) and Hartmann and Klauer (in press).
The second method is a rejection sampler provided by Drugowitsch (2016;
<doi:10.1038/srep20490>). The third method is an inverse transformation
sampler. The fourth method is a "pseudo" adaptive rejection sampler that
builds on the first method. For more details see the corresponding help
files.

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
