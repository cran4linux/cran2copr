%global packname  metadynminer3d
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}
Summary:          Tools to Read, Analyze and Visualize Metadynamics 3D HILLS Filesfrom 'Plumed'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-metadynminer 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-misc3d 
Requires:         R-CRAN-metadynminer 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-misc3d 

%description
Metadynamics is a state of the art biomolecular simulation technique.
'Plumed' Tribello, G.A. et al. (2014) <doi:10.1016/j.cpc.2013.09.018>
program makes it possible to perform metadynamics using various simulation
codes. The results of metadynamics done in 'Plumed' can be analyzed by
'metadynminer'. The package 'metadynminer' reads 1D and 2D metadynamics
hills files from 'Plumed' package. As an addendum, 'metadynaminer3d' is
used to visualize 3D hills. It uses a fast algorithm by Hosek, P. and
Spiwok, V. (2016) <doi:10.1016/j.cpc.2015.08.037> to calculate a free
energy surface from hills. Minima can be located and plotted on the free
energy surface. Free energy surfaces and minima can be plotted to produce
publication quality images.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
