%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aws
%global packver   2.5-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.5
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Weights Smoothing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-awsMethods >= 1.1.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gsl 
Requires:         R-CRAN-awsMethods >= 1.1.1
Requires:         R-methods 
Requires:         R-CRAN-gsl 

%description
We provide a collection of R-functions implementing adaptive smoothing
procedures in 1D, 2D and 3D. This includes the Propagation-Separation
Approach to adaptive smoothing, the Intersecting Confidence Intervals
(ICI), variational approaches and a non-local means filter. The package is
described in detail in Polzehl J, Papafitsoros K, Tabelow K (2020).
Patch-Wise Adaptive Weights Smoothing in R. Journal of Statistical
Software, 95(6), 1-27. <doi:10.18637/jss.v095.i06>, Usage of the package
in MR imaging is illustrated in Polzehl and Tabelow (2023), Magnetic
Resonance Brain Imaging, 2nd Ed. Appendix A, Springer, Use R! Series.
<doi:10.1007/978-3-031-38949-8>.

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
test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R && echo "FFLAGS=$(R CMD config FFLAGS) -fallow-argument-mismatch" > ~/.R/Makevars
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
