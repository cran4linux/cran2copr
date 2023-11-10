%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  versioning
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Settings and File I/O using a Configuration YAML File

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-yaml 

%description
R data pipelines commonly require reading and writing data to versioned
directories. Each directory might correspond to one step of a multi-step
process, where that version corresponds to particular settings for that
step and a chain of previous steps that each have their own versions. This
package creates a configuration object that makes it easy to read and
write versioned data, based on YAML configuration files loaded and saved
to each versioned folder.

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
