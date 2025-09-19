%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SimDesign
%global packver   2.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.21
Release:          1%{?dist}%{?buildtag}
Summary:          Structure for Organizing Monte Carlo Simulation Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pbapply >= 1.3.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sessioninfo 
BuildRequires:    R-CRAN-beepr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-stats 
Requires:         R-CRAN-pbapply >= 1.3.0
Requires:         R-methods 
Requires:         R-CRAN-testthat 
Requires:         R-parallel 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sessioninfo 
Requires:         R-CRAN-beepr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-codetools 
Requires:         R-CRAN-clipr 
Requires:         R-stats 

%description
Provides tools to safely and efficiently organize and execute Monte Carlo
simulation experiments in R. The package controls the structure and
back-end of Monte Carlo simulation experiments by utilizing a
generate-analyse-summarise workflow. The workflow safeguards against
common simulation coding issues, such as automatically re-simulating
non-convergent results, prevents inadvertently overwriting simulation
files, catches error and warning messages during execution, implicitly
supports parallel processing with high-quality random number generation,
and provides tools for managing high-performance computing (HPC) array
jobs submitted to schedulers such as SLURM. For a pedagogical introduction
to the package see Sigal and Chalmers (2016)
<doi:10.1080/10691898.2016.1246953>. For a more in-depth overview of the
package and its design philosophy see Chalmers and Adkins (2020)
<doi:10.20982/tqmp.16.4.p248>.

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
