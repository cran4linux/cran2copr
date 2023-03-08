%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  negligible
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Functions for Negligible Effect/Equivalence Testing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-WRS2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-nptest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fungible 
BuildRequires:    R-CRAN-rockchalk 
BuildRequires:    R-CRAN-MBESS 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-WRS2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-nptest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fungible 
Requires:         R-CRAN-rockchalk 
Requires:         R-CRAN-MBESS 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 

%description
Researchers often want to evaluate whether there is a negligible
relationship among variables. The 'negligible' package provides functions
that are useful for conducting negligible effect testing (also called
equivalence testing). For example, there are functions for evaluating the
equivalence of means or the presence of a negligible association
(correlation/ regression). Beribisky, N., Mara, C., & Cribbie, R. A.
(2020) <doi:10.20982/tqmp.16.4.p424>. Beribisky, N., Davidson, H.,
Cribbie, R. A. (2019) <doi:10.7717/peerj.6853>. Shiskina, T., Farmus, L.,
& Cribbie, R. A. (2018) <doi:10.20982/tqmp.14.3.p167>. Mara, C. & Cribbie,
R. A. (2017) <doi:10.1080/00220973.2017.1301356>. Counsell, A. & Cribbie,
R. A. (2015) <doi:10.1111/bmsp.12045>. van Wieringen, K. & Cribbie, R. A.
(2014) <doi:10.1111/bmsp.12015>. Goertzen, J. R. & Cribbie, R. A. (2010)
<doi:10.1348/000711009x475853>. Cribbie, R. A., Gruman, J. &
Arpin-Cribbie, C. (2004) <doi:10.1002/jclp.10217>.

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
