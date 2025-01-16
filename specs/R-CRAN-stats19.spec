%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stats19
%global packver   3.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Work with Open Road Traffic Casualty Data from Great Britain

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-tools 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-readr 
Requires:         R-tools 

%description
Tools to help download, process and analyse the UK road collision data
collected using the 'STATS19' form. The datasets are provided as 'CSV'
files with detailed road safety information about the circumstances of car
crashes and other incidents on the roads resulting in casualties in Great
Britain from 1979 to present. Tables are available on 'colissions' with
the circumstances (e.g. speed limit of road), information about 'vehicles'
involved (e.g. type of vehicle), and 'casualties' (e.g. age). The
statistics relate only to events on public roads that were reported to the
police, and subsequently recorded, using the 'STATS19' collision reporting
form. See the Department for Transport website
<https://www.data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-accidents-safety-data>
for more information on these datasets. The package is described in a
paper in the Journal of Open Source Software (Lovelace et al. 2019)
<doi:10.21105/joss.01181>. See Gilardi et al. (2022)
<doi:10.1111/rssa.12823>, Vidal-Tortosa et al. (2021)
<doi:10.1016/j.jth.2021.101291>, and Tait et al. (2023)
<doi:10.1016/j.aap.2022.106895> for examples of how the data can be used
for methodological and empirical road safety research.

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
