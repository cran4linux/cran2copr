%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hcidata
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          HCI Datasets

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-Rdpack 

%description
A collection of datasets of human-computer interaction (HCI) experiments.
Each dataset is from an HCI paper, with all fields described and the
original publication linked. All paper authors of included data have
consented to the inclusion of their data in this package. The datasets
include data from a range of HCI studies, such as pointing tasks, user
experience ratings, and steering tasks. Dataset sources: Bergström et al.
(2022) <doi:10.1145/3490493>; Dalsgaard et al. (2021)
<doi:10.1145/3489849.3489853>; Larsen et al. (2019)
<doi:10.1145/3338286.3340115>; Lilija et al. (2019)
<doi:10.1145/3290605.3300676>; Pohl and Murray-Smith (2013)
<doi:10.1145/2470654.2481307>; Pohl and Mottelson (2022)
<doi:10.3389/frvir.2022.719506>.

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
