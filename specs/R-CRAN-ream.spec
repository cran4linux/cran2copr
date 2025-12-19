%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ream
%global packver   1.0-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Density, Distribution, and Sampling Functions for Evidence Accumulation Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Calculate the probability density functions (PDFs) for two threshold
evidence accumulation models (EAMs). These are defined using the following
Stochastic Differential Equation (SDE), dx(t) = v(x(t),t)*dt+D(x(t),t)*dW,
where x(t) is the accumulated evidence at time t, v(x(t),t) is the drift
rate, D(x(t),t) is the noise scale, and W is the standard Wiener process.
The boundary conditions of this process are the upper and lower decision
thresholds, represented by b_u(t) and b_l(t), respectively. Upper
threshold b_u(t) > 0, while lower threshold b_l(t) < 0. The initial
condition of this process x(0) = z where b_l(t) < z < b_u(t). We represent
this as the relative start point w = z/(b_u(0)-b_l(0)), defined as a ratio
of the initial threshold location. This package generates the PDF using
the same approach as the 'python' package it is based upon, 'PyBEAM' by
Murrow and Holmes (2023) <doi:10.3758/s13428-023-02162-w>. First, it
converts the SDE model into the forwards Fokker-Planck equation dp(x,t)/dt
= d(v(x,t)*p(x,t))/dt-0.5*d^2(D(x,t)^2*p(x,t))/dx^2, then solves this
equation using the Crank-Nicolson method to determine p(x,t). Finally, it
calculates the flux at the decision thresholds, f_i(t) =
0.5*d(D(x,t)^2*p(x,t))/dx evaluated at x = b_i(t), where i is the relevant
decision threshold, either upper (i = u) or lower (i = l). The flux at
each thresholds f_i(t) is the PDF for each threshold, specifically its
PDF. We discuss further details of this approach in this package and
'PyBEAM' publications. Additionally, one can calculate the cumulative
distribution functions of and sampling from the EAMs.

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
