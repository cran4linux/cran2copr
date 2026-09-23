%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BioMixModel
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed Models for Biological, Clustered and Longitudinal Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Fits and interprets mixed-effects models for clustered, longitudinal and
heterogeneous biological data. Provides variance partitioning, intraclass
correlation, penalized likelihood summaries, a heterogeneous-data
information criterion, model comparison, diagnostics, and ensemble-style
summaries for multilevel data. The package is designed as a complementary,
interpretable workflow around established mixed-model methods. Methods for
intraclass correlation and variance partitioning are informed by Nakagawa
and Schielzeth (2010) <doi:10.1111/j.1469-185X.2010.00141.x> and Nakagawa
et al. (2017) <doi:10.1098/rsif.2017.0213>. Mixed-effects modeling
approaches are described by Zuur et al. (2009)
<doi:10.1007/978-0-387-87458-6>.

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
