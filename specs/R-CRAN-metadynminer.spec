%global __brp_check_rpaths %{nil}
%global packname  metadynminer
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Read, Analyze and Visualize Metadynamics HILLS Files from 'Plumed'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Metadynamics is a state of the art biomolecular simulation technique.
'Plumed' Tribello, G.A. et al. (2014) <doi:10.1016/j.cpc.2013.09.018>
program makes it possible to perform metadynamics using various simulation
codes. The results of metadynamics done in 'Plumed' can be analyzed by
'metadynminer'. The package 'metadynminer' reads 1D and 2D metadynamics
hills files from 'Plumed' package. It uses a fast algorithm by Hosek, P.
and Spiwok, V. (2016) <doi:10.1016/j.cpc.2015.08.037> to calculate a free
energy surface from hills. Minima can be located and plotted on the free
energy surface. Transition states can be analyzed by Nudged Elastic Band
method by Henkelman, G. and Jonsson, H. (2000) <doi:10.1063/1.1323224>.
Free energy surfaces, minima and transition paths can be plotted to
produce publication quality images.

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
