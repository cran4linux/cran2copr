%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LDlinkR
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculating Linkage Disequilibrium (LD) in Human Population Groups of Interest

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils >= 3.4.2
BuildRequires:    R-CRAN-httr >= 1.4.0
Requires:         R-utils >= 3.4.2
Requires:         R-CRAN-httr >= 1.4.0

%description
Provides access to the 'LDlink' API
(<https://ldlink.nih.gov/?tab=apiaccess>) using the R console.  This
programmatic access facilitates researchers who are interested in
performing batch queries in 1000 Genomes Project (2015)
<doi:10.1038/nature15393> data using 'LDlink'. 'LDlink' is an interactive
and powerful suite of web-based tools for querying germline variants in
human population groups of interest. For more details, please see Machiela
et al. (2015) <doi:10.1093/bioinformatics/btv402>.

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
