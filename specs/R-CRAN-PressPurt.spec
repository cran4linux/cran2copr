%global __brp_check_rpaths %{nil}
%global packname  PressPurt
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Indeterminacy of Networks via Press Perturbations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.11
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-utils 
Requires:         R-CRAN-reticulate >= 1.11
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-utils 

%description
This is a computational package designed to identify the most sensitive
interactions within a network which must be estimated most accurately in
order to produce qualitatively robust predictions to a press perturbation.
This is accomplished by enumerating the number of sign switches (and their
magnitude) in the net effects matrix when an edge experiences uncertainty.
The package produces data and visualizations when uncertainty is
associated to one or more edges in the network and according to a variety
of distributions. The software requires the network to be described by a
system of differential equations but only requires as input a numerical
Jacobian matrix evaluated at an equilibrium point. This package is based
on Koslicki, D., & Novak, M. (2017) <doi:10.1007/s00285-017-1163-0>.

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
