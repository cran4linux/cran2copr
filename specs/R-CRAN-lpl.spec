%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lpl
%global packver   0.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12
Release:          1%{?dist}%{?buildtag}
Summary:          Local Partial Likelihood Estimation and Simultaneous Confidence Band

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-survival 

%description
Local partial likelihood estimation by Fan, Lin and
Zhou(2006)<doi:10.1214/009053605000000796> and simultaneous confidence
band is a set of tools to test the covariates-biomarker interaction for
survival data. Test for the covariates-biomarker interaction using the
bootstrap method and the asymptotic method with simultaneous confidence
band (Liu, Jiang and Chen (2015)<doi:10.1002/sim.6563>).

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
