%global packname  chebpol
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          2%{?dist}
Summary:          Multivariate Interpolation

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw-devel >= 3.1.2
BuildRequires:    gsl-devel
Requires:         fftw
Requires:         gsl
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-geometry 
Requires:         R-stats 
Requires:         R-CRAN-geometry 

%description
Contains methods for creating multivariate/multidimensional interpolations
of functions on a hypercube. If available through fftw3, the DCT-II/FFT is
used to compute coefficients for a Chebyshev interpolation. Other
interpolation methods for arbitrary Cartesian grids are also provided, a
piecewise multilinear, and the Floater-Hormann barycenter method. For
scattered data polyharmonic splines with a linear term is provided. The
time-critical parts are written in C for speed. All interpolants are
parallelized if used to evaluate more than one point.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
