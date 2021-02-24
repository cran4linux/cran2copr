%global packname  Dominance
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate and Visualize Dominance Hierarchies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-chron 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-chron 

%description
Functions to calculate ADI (Average Dominance Index) and FDI
(Frequency-Based Dominance Index). Functions to visualize the Data with
Social Network Graphs with Dual Directions and Music Notation Graph.
'XLConnect' or 'openxlsx' or 'RcmdrMisc' is only necessary for comfortable
Excel file handling. See ADI-FDI Hemelrijk et al. (2005)
<doi:10.1163/156853905774405290> de Vries et al.  (2009)
<doi:10.1163/156853909X412241> Musicnotition: Chase (2006)
<doi:10.1186/1742-9994-3-18>.

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
