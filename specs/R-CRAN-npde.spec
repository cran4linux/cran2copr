%global __brp_check_rpaths %{nil}
%global packname  npde
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Normalised Prediction Distribution Errors for Nonlinear Mixed-Effect Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-methods 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-rlang 

%description
Provides routines to compute normalised prediction distribution errors, a
metric designed to evaluate non-linear mixed effect models such as those
used in pharmacokinetics and pharmacodynamics. Documentation about 'npde'
is provided by a comprehensive user guide on the github repository
(<https://github.com/ecomets/npde30/blob/main/userguide_npde_3.0.pdf>),
and references concerning the methods include the papers by Brendel et al.
(2006, <doi:10.1007/s11095-006-9067-5>; 2010,
<doi:10.1007/s10928-009-9143-7>), Comets et al. (2008,
<doi:10.1016/j.cmpb.2007.12.002> ; 2010,
<http://journal-sfds.fr/article/view/45>), and Nguyen et al. (2012,
<doi:10.1007/s10928-012-9264-2>). See 'citation("npde")' for details.

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
