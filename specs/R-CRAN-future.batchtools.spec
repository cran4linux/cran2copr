%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  future.batchtools
%global packver   0.32.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.32.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Future Backend for HPC Schedulers using 'batchtools'

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-future >= 1.80.0
BuildRequires:    R-CRAN-batchtools >= 0.9.17
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-future >= 1.80.0
Requires:         R-CRAN-batchtools >= 0.9.17
Requires:         R-CRAN-parallelly 
Requires:         R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-stringi 

%description
Implementation of the Future API <doi:10.32614/RJ-2021-048> on top of the
'batchtools' package. The backend is fully compliant with the Future API,
as validated by the 'future.tests' conformance test suite, meaning that
code using futures gives identical results and behaves the same regardless
of which future backend is used. Futures are resolved on the local
machine, on an ad-hoc cluster of machines, or via job schedulers on
high-performance compute ('HPC') clusters, such as 'Slurm', 'SGE', 'LSF',
'OpenLava', and 'TORQUE' / 'PBS'. A common use is to parallelize existing
map-reduce calls via the 'futurize' package
<doi:10.48550/arXiv.2601.17578>, e.g.
'plan(future.batchtools::batchtools_slurm)' followed by 'lapply(xs, fcn)
|> futurize()' or 'purrr::map(xs, fcn) |> futurize()'.

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
