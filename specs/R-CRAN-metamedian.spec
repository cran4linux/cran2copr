%global __brp_check_rpaths %{nil}
%global packname  metamedian
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Meta-Analysis of Medians

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-estmeansd 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-stats 
Requires:         R-CRAN-estmeansd 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-metafor 
Requires:         R-stats 

%description
Implements several methods to meta-analyze studies that report the sample
median of the outcome. When the primary studies are one-group studies, the
methods of McGrath et al. (2019) <doi:10.1002/sim.8013> can be applied to
estimate the pooled median. In the two-group context, the methods of
McGrath et al. (2020) <doi:10.1002/bimj.201900036> can be applied to
estimate the pooled raw difference of medians across groups.

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
