%global __brp_check_rpaths %{nil}
%global packname  scalpel
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Processes Calcium Imaging Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-protoclust 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-gam 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-protoclust 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-gam 

%description
Identifies the locations of neurons, and estimates their calcium
concentrations over time using the SCALPEL method proposed in Petersen,
Ashley; Simon, Noah; Witten, Daniela. SCALPEL: Extracting neurons from
calcium imaging data. Ann. Appl. Stat. 12 (2018), no. 4, 2430--2456.
<doi:10.1214/18-AOAS1159>.
<https://projecteuclid.org/euclid.aoas/1542078051>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
