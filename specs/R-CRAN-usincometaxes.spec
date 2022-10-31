%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  usincometaxes
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Federal and State Income Taxes in the United States

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-V8 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-datasets 
Requires:         R-CRAN-vroom 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-V8 
Requires:         R-CRAN-tidyselect 

%description
Calculates federal and state income taxes in the United States. It acts as
a wrapper to the NBER's TAXSIM 35 (<http://taxsim.nber.org/taxsim35/>) tax
simulator. TAXSIM 35 conducts the calculations, while 'usincometaxes'
prepares the data for TAXSIM 35, sends the data to TAXSIM 35's server or
communicates with the Web Assembly file, retrieves the data, and places it
into a data frame. All without the user worrying about this process.

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
