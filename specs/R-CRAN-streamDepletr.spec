%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  streamDepletr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Streamflow Depletion Due to Groundwater Pumping

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sf 

%description
Implementation of analytical models for estimating streamflow depletion
due to groundwater pumping, and other related tools. Functions are broadly
split into two groups: (1) analytical streamflow depletion models, which
estimate streamflow depletion for a single stream reach resulting from
groundwater pumping; and (2) depletion apportionment equations, which
distribute estimated streamflow depletion among multiple stream reaches
within a stream network. See Zipper et al. (2018)
<doi:10.1029/2018WR022707> for more information on depletion apportionment
equations and Zipper et al. (2019) <doi:10.1029/2018WR024403> for more
information on analytical depletion functions, which combine analytical
models and depletion apportionment equations.

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
