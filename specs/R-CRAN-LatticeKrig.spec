%global __brp_check_rpaths %{nil}
%global packname  LatticeKrig
%global packver   8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.4
Release:          3%{?dist}%{?buildtag}
Summary:          Multi-Resolution Kriging Based on Markov Random Fields

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-fields >= 9.9
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-spam 
Requires:         R-CRAN-fields >= 9.9
Requires:         R-methods 
Requires:         R-CRAN-spam 

%description
Methods for the interpolation of large spatial datasets. This package
follows a "fixed rank Kriging" approach but provides a surface fitting
method that can approximate standard spatial data models. Using a large
number of basis functions allows for estimates that can come close to
interpolating the observations (a spatial model with a small nugget
variance.)  Moreover, the covariance model for this method can approximate
the Matern covariance family but also allows for a multi-resolution model
and supports efficient computation of the profile likelihood for
estimating covariance parameters. This is accomplished through compactly
supported basis functions and a Markov random field model for the basis
coefficients. These features lead to sparse matrices for the computations
and this package makes of the R spam package for sparse linear algebra. An
extension of this version over previous ones ( < 5.4 ) is the support for
different geometries besides a rectangular domain. The Markov random field
approach combined with a basis function representation makes the
implementation of different geometries simple where only a few specific R
functions need to be added with most of the computation and evaluation
done by generic routines that have been tuned to be efficient.  One
benefit of this package's model/approach is the facility to do
unconditional and conditional simulation of the field for large numbers of
arbitrary points. There is also the flexibility for estimating
non-stationary covariances and also the case when the observations are a
linear combination (e.g. an integral) of the spatial process. Included are
generic methods for prediction, standard errors for prediction, plotting
of the estimated surface and conditional and unconditional simulation. See
the 'LatticeKrig' GitHub repository for a vignette of this package.
Development of this package was supported in part by the National Science
Foundation Grant 1417857 and the National Center for Atmospheric Research.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
