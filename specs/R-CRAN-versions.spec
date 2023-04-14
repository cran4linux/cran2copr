%global __brp_check_rpaths %{nil}
%global packname  versions
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Query and Install Specific Versions of Packages on CRAN

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Installs specified versions of R packages hosted on CRAN and provides
functions to list available versions and the versions of currently
installed packages. These tools can be used to help make R projects and
packages more reproducible. 'versions' fits in the narrow gap between the
'devtools' install_version() function and the 'checkpoint' package.
devtools::install_version() installs a stated package version from source
files stored on the CRAN archives. However CRAN does not store binary
versions of packages so Windows users need to have RTools installed and
Windows and OSX users get longer installation times. 'checkpoint' uses the
Revolution Analytics MRAN server to install packages (from source or
binary) as they were available on a given date. It also provides a helpful
interface to detect the packages in use in a directory and install all of
those packages for a given date. 'checkpoint' doesn't provide
install.packages-like functionality however, and that's what 'versions'
aims to do, by querying MRAN. As MRAN only goes back to 2014-09-17,
'versions' can't install packages archived before this date.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
