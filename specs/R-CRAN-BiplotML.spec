%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BiplotML
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Logistic Biplot Estimation Using Machine Learning Algorithms

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-RSpectra 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-RSpectra 

%description
Implements methods for fitting logistic biplot models to multivariate
binary data. The logistic biplot represents individuals as points and
binary variables as directed vectors in a low-dimensional subspace; the
orthogonal projection of each individual onto a variable vector
approximates the expected probability that the corresponding
characteristic is present. Available fitting methods include conjugate
gradient algorithms, a coordinate descent Majorization-Minimization (MM)
algorithm, and a block coordinate descent algorithm based on data
projection that supports matrices with missing values and allows new
individuals to be projected as supplementary rows without refitting the
model. A cross-validation procedure is provided to select the number of
latent dimensions k. References: Babativa-Marquez and Vicente-Villardon
(2021) <doi:10.3390/math9162015>; Vicente-Villardon and Galindo (2006,
ISBN:9780470973196).

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
