%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forestdynR
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Forest Dynamics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BIOMASS >= 2.1.11
BuildRequires:    R-tcltk >= 1.0.0
Requires:         R-CRAN-BIOMASS >= 2.1.11
Requires:         R-tcltk >= 1.0.0

%description
Determines the dynamics of tree species communities (mortality rates,
recruitment, loss and gain in basal area, net changes and turnover).
Important notes are a) The 'forest_df' argument (data) must contain the
columns 'plot' (plot identification), 'spp' (species identification),
DBH_1 (Diameter at breast height in first year of measure) and DBH_2
(Diameter at breast height in second year of measure). DBH_1 and DBH_2
must be numeric values; b) example input file in
'data(forest_df_example)'; c) The argument 'inv_time' represents the time
between inventories, in years; d) The 'coord' argument must be of the type
'c(longitude, latitude)', with decimal degree values; e) Argument 'add_wd'
represents a dataframe with wood density values (g cm-3) format with three
columns ('genus', 'species', 'wd'). This argument is set to NULL by
default, and if isn't provided, the wood density will be estimated with
the getWoodDensity() function from the 'BIOMASS' package.

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
