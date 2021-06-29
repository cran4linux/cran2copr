%global __brp_check_rpaths %{nil}
%global packname  SimDesign
%global packver   2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Structure for Organizing Monte Carlo Simulation Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pbapply >= 1.3.0
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sessioninfo 
BuildRequires:    R-CRAN-RPushbullet 
BuildRequires:    R-stats 
Requires:         R-CRAN-pbapply >= 1.3.0
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sessioninfo 
Requires:         R-CRAN-RPushbullet 
Requires:         R-stats 

%description
Provides tools to safely and efficiently organize and execute Monte Carlo
simulation experiments in R. The package controls the structure and
back-end of Monte Carlo simulation experiments by utilizing a
generate-analyse-summarise workflow. The workflow safeguards against
common simulation coding issues, such as automatically re-simulating
non-convergent results, prevents inadvertently overwriting simulation
files, catches error and warning messages during execution, and implicitly
supports parallel processing. For a pedagogical introduction to the
package see Sigal and Chalmers (2016) <doi:10.1080/10691898.2016.1246953>.
For a more in-depth overview of the package and its design philosophy see
Chalmers and Adkins (2020) <doi:10.20982/tqmp.16.4.p248>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
