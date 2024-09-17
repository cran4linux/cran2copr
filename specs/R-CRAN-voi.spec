%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  voi
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Expected Value of Information

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-dbarts 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-dbarts 
Requires:         R-CRAN-posterior 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-Matrix 

%description
Methods to calculate the expected value of information from a
decision-analytic model.  This includes the expected value of perfect
information (EVPI), partial perfect information (EVPPI) and sample
information (EVSI), and the expected net benefit of sampling (ENBS).  A
range of alternative computational methods are provided under the same
user interface.  See Heath et al. (2024) <doi:10.1201/9781003156109>,
Jackson et al. (2022) <doi:10.1146/annurev-statistics-040120-010730>.

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
