%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  verbalisr
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Describe Pedigree Relationships in Words

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-pedtools >= 2.2.0
BuildRequires:    R-CRAN-ribd >= 1.6.1
Requires:         R-CRAN-pedtools >= 2.2.0
Requires:         R-CRAN-ribd >= 1.6.1

%description
Describe in words the genealogical relationship between two members of a
given pedigree, using the algorithm in Vigeland (2022)
<doi:10.1186/s12859-022-04759-y>. 'verbalisr' is part of the 'pedsuite'
collection of packages for pedigree analysis. For a demonstration of
'verbalisr', see the online app 'QuickPed' at
<https://magnusdv.shinyapps.io/quickped>.

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
