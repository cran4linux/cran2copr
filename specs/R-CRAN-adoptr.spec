%global packname  adoptr
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Optimal Two-Stage Designs in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-nloptr 
Requires:         R-methods 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-stringr 

%description
Optimize one or two-arm, two-stage designs for clinical trials with
respect to several pre-implemented objective criteria or implement custom
objectives. Optimization under uncertainty and conditional (given
stage-one outcome) constraints are supported. See Pilz M, Kunzmann K,
Herrmann C, Rauch G, Kieser M. A variational approach to optimal two-stage
designs. Statistics in Medicine. 2019;38(21):4159–4171.
<doi:10.1002/sim.8291> for details.

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
