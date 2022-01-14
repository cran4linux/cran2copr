%global __brp_check_rpaths %{nil}
%global packname  gittargets
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Version Control for the Targets Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.1.0
BuildRequires:    R-CRAN-processx >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-gert >= 1.0.0
BuildRequires:    R-CRAN-targets >= 0.6.0
BuildRequires:    R-CRAN-uuid >= 0.1.4
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.1.0
Requires:         R-CRAN-processx >= 3.0.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-gert >= 1.0.0
Requires:         R-CRAN-targets >= 0.6.0
Requires:         R-CRAN-uuid >= 0.1.4
Requires:         R-stats 
Requires:         R-utils 

%description
Pipelines with the 'targets' R package (2021, <doi:10.21105/joss.02959>)
skip steps that are up to already date. Although this behavior reduces the
runtime of subsequent runs, it comes at the cost of overwriting previous
results. So if the pipeline source code is under version control, and if
you revert to a previous commit or branch, the data will no longer be up
to date with the code you just checked out. Ordinarily, you would need to
rerun the pipeline in order to recover the targets you had before.
However, 'gittargets' preserves historical output, creating version
control snapshots of data store. Each data snapshot remembers the
contemporaneous Git commit of the pipeline source code, so you can recover
the right data when you navigate the Git history. In other words,
'gittargets' makes it possible to switch commits or branches without
invalidating the pipeline. You can simply check out the up-to-date targets
from the past instead of taking the time to recompute them from scratch.

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
