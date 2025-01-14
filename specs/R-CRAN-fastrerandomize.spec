%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastrerandomize
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hardware-Accelerated Rerandomization for Improved Balance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-assertthat 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 

%description
Provides hardware-accelerated tools for performing rerandomization and
randomization testing in experimental research. Using a 'JAX' backend, the
package enables exact rerandomization inference even for large experiments
with hundreds of billions of possible randomizations. Key functionalities
include generating pools of acceptable rerandomizations based on covariate
balance, conducting exact randomization tests, and performing pre-analysis
evaluations to determine optimal rerandomization acceptance thresholds.
The package supports various hardware acceleration frameworks including
'CPU', 'CUDA', and 'METAL', making it versatile across accelerated
computing environments. This allows researchers to efficiently implement
stringent rerandomization designs and conduct valid inference even with
large sample sizes. The package is partly based on Jerzak and Goldstein
(2023) <doi:10.48550/arXiv.2310.00861>.

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
