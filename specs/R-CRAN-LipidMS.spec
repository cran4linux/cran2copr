%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LipidMS
%global packver   3.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Lipid Annotation for LC-MS/MS DDA or DIA Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-readMzXmlData 
BuildRequires:    R-CRAN-CHNOSZ 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-iterators 
Requires:         R-CRAN-shiny 
Requires:         R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-readMzXmlData 
Requires:         R-CRAN-CHNOSZ 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shinythemes 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-iterators 

%description
Lipid annotation in untargeted LC-MS lipidomics based on fragmentation
rules. Alcoriza-Balaguer MI, Garcia-Canaveras JC, Lopez A, Conde I, Juan
O, Carretero J, Lahoz A (2019) <doi:10.1021/acs.analchem.8b03409>.

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
