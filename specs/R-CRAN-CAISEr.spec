%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CAISEr
%global packver   1.0.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.17
Release:          1%{?dist}%{?buildtag}
Summary:          Comparison of Algorithms with Iterative Sample Size Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.5.1
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-pbmcapply >= 1.4.1
BuildRequires:    R-CRAN-assertthat >= 0.2.1
Requires:         R-parallel >= 3.5.1
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-pbmcapply >= 1.4.1
Requires:         R-CRAN-assertthat >= 0.2.1

%description
Functions for performing experimental comparisons of algorithms using
adequate sample sizes for power and accuracy. Implements the methodology
originally presented in Campelo and Takahashi (2019)
<doi:10.1007/s10732-018-9396-7> for the comparison of two algorithms, and
later generalised in Campelo and Wanner (Submitted, 2019)
<arxiv:1908.01720>.

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
