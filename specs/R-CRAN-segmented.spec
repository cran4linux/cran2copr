%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  segmented
%global packver   2.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Regression Models with Break-Points / Change-Points Estimation (with Possibly Random Effects)

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nlme 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nlme 

%description
Fitting regression models where, in addition to possible linear terms, one
or more covariates have segmented (i.e., broken-line or piece-wise linear)
or stepmented (i.e. piece-wise constant) effects. Multiple breakpoints for
the same variable are allowed. The estimation method is discussed in
Muggeo (2003, <doi:10.1002/sim.1545>) and illustrated in Muggeo (2008,
<https://www.r-project.org/doc/Rnews/Rnews_2008-1.pdf>). An approach for
hypothesis testing is presented in Muggeo (2016,
<doi:10.1080/00949655.2016.1149855>), and interval estimation for the
breakpoint is discussed in Muggeo (2017, <doi:10.1111/anzs.12200>).
Segmented mixed models, i.e. random effects in the change point, are
discussed in Muggeo (2014, <doi:10.1177/1471082X13504721>). Estimation of
piecewise-constant relationships and changepoints (mean-shift models) is
discussed in Fasola et al. (2018, <doi:10.1007/s00180-017-0740-4>).

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
