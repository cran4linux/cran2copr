%global __brp_check_rpaths %{nil}
%global packname  datapack
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Flexible Container to Transport and Manipulate Data and Associated Resources

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-redland 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-fs 
Requires:         R-methods 
Requires:         R-CRAN-redland 
Requires:         R-CRAN-XML 
Requires:         R-utils 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-zip 

%description
Provides a flexible container to transport and manipulate complex sets of
data. These data may consist of multiple data files and associated meta
data and ancillary files. Individual data objects have associated system
level meta data, and data files are linked together using the OAI-ORE
standard resource map which describes the relationships between the files.
The OAI- ORE standard is described at <https://www.openarchives.org/ore/>.
Data packages can be serialized and transported as structured files that
have been created following the BagIt specification. The BagIt
specification is described at
<https://tools.ietf.org/html/draft-kunze-bagit-08>.

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
