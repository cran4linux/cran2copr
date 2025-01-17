%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phylosignalDB
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Explore Phylogenetic Signals Using Distance-Based Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.7
BuildRequires:    R-CRAN-cluster >= 2.1.6
BuildRequires:    R-CRAN-castor >= 1.8.3
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-doParallel >= 1.0.17
Requires:         R-CRAN-ape >= 5.7
Requires:         R-CRAN-cluster >= 2.1.6
Requires:         R-CRAN-castor >= 1.8.3
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-doParallel >= 1.0.17

%description
A unified method, called M statistic, is provided for detecting
phylogenetic signals in continuous traits, discrete traits, and
multi-trait combinations. Blomberg and Garland (2002)
<doi:10.1046/j.1420-9101.2002.00472.x> provided a widely accepted
statistical definition of the phylogenetic signal, which is the "tendency
for related species to resemble each other more than they resemble species
drawn at random from the tree". The M statistic strictly adheres to the
definition of phylogenetic signal, formulating an index and developing a
method of testing in strict accordance with the definition, instead of
relying on correlation analysis or evolutionary models. The novel method
equivalently expressed the textual definition of the phylogenetic signal
as an inequality equation of the phylogenetic and trait distances and
constructed the M statistic. Also, there are more distance-based methods
under development.

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
