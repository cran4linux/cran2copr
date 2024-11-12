%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forestSAS
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Forest Spatial Structure Analysis Systems

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-spatstat.data 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.random 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-spatstat.data 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.random 

%description
Recent years have seen significant interest in neighborhood-based
structural parameters that effectively represent the spatial
characteristics of tree populations and forest communities, and possess
strong applicability for guiding forestry practices. This package provides
valuable information that enhances our understanding and analysis of the
fine-scale spatial structure of tree populations and forest stands.
Reference: Yan L, Tan W, Chai Z, et al (2019)
<doi:10.13323/j.cnki.j.fafu(nat.sci.).2019.03.007>.

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
