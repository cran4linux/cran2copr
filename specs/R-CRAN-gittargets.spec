%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gittargets
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Data Version Control for the Targets Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         git
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.1.0
BuildRequires:    R-CRAN-callr >= 3.0.0
BuildRequires:    R-CRAN-processx >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-gert >= 1.0.0
BuildRequires:    R-CRAN-targets >= 0.6.0
BuildRequires:    R-CRAN-uuid >= 0.1.4
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.1.0
Requires:         R-CRAN-callr >= 3.0.0
Requires:         R-CRAN-processx >= 3.0.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-gert >= 1.0.0
Requires:         R-CRAN-targets >= 0.6.0
Requires:         R-CRAN-uuid >= 0.1.4
Requires:         R-stats 
Requires:         R-utils 

%description
In computationally demanding data analysis pipelines, the 'targets' R
package (2021, <doi:10.21105/joss.02959>) maintains an up-to-date set of
results while skipping tasks that do not need to rerun. This process
increases speed and increases trust in the final end product. However, it
also overwrites old output with new output, and past results disappear by
default. To preserve historical output, the 'gittargets' package captures
version-controlled snapshots of the data store, and each snapshot links to
the underlying commit of the source code. That way, when the user rolls
back the code to a previous branch or commit, 'gittargets' can recover the
data contemporaneous with that commit so that all targets remain up to
date.

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
