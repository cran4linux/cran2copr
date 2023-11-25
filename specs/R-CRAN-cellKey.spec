%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cellKey
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Consistent Perturbation of Statistical Frequency- And Magnitude Tables

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ptable >= 1.0.0
BuildRequires:    R-CRAN-digest >= 0.6.23
BuildRequires:    R-CRAN-sdcTable >= 0.32.2
BuildRequires:    R-CRAN-sdcHierarchies >= 0.19.3
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-parallel 
Requires:         R-CRAN-ptable >= 1.0.0
Requires:         R-CRAN-digest >= 0.6.23
Requires:         R-CRAN-sdcTable >= 0.32.2
Requires:         R-CRAN-sdcHierarchies >= 0.19.3
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-CRAN-cli 
Requires:         R-utils 
Requires:         R-CRAN-yaml 
Requires:         R-parallel 

%description
Data from statistical agencies and other institutions often need to be
protected before they can be published. This package can be used to
perturb statistical tables in a consistent way. The main idea is to add -
at the micro data level - a record key for each unit. Based on these keys,
for any cell in a statistical table a cell key is computed as a function
on the record keys contributing to a specific cell. Values that are added
to the cell in order to perturb it are derived from a lookup-table that
maps values of cell keys to specific perturbation values. The theoretical
basis for the methods implemented can be found in Thompson, Broadfoot and
Elazar (2013)
<https://unece.org/fileadmin/DAM/stats/documents/ece/ces/ge.46/2013/Topic_1_ABS.pdf>
which was extended and enhanced by Giessing and Tent (2019)
<https://unece.org/fileadmin/DAM/stats/documents/ece/ces/ge.46/2019/mtg1/SDC2019_S2_Germany_Giessing_Tent_AD.pdf>.

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
