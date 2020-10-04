%global packname  funreg
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Functional Regression for Irregularly Timed Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-splines 
Requires:         R-MASS 
Requires:         R-mgcv 
Requires:         R-CRAN-mvtnorm 
Requires:         R-splines 

%description
Performs functional regression, and some related approaches, for intensive
longitudinal data (see the book by Walls & Schafer, 2006, Models for
Intensive Longitudinal Data, Oxford) when such data is not necessarily
observed on an equally spaced grid of times.  The approach generally
follows the ideas of Goldsmith, Bobb, Crainiceanu, Caffo, and Reich
(2011)<DOI:10.1198/jcgs.2010.10007> and the approach taken in their sample
code, but with some modifications to make it more feasible to use with
long rather than wide, non-rectangular longitudinal datasets with unequal
and potentially random measurement times.  It also allows easy plotting of
the correlation between the smoothed covariate and the outcome as a
function of time, which can add additional insights on how to interpret a
functional regression.  Additionally, it also provides several permutation
tests for the significance of the functional predictor.  The heuristic
interpretation of ``time'' is used to describe the index of the functional
predictor, but the same methods can equally be used for another
unidimensional continuous index, such as space along a north-south axis.
The development of this package was part of a research project supported
by Award R03 CA171809-01 from the National Cancer Institute and Award P50
DA010075 from the National Institute on Drug Abuse. The content is solely
the responsibility of the authors and does not necessarily represent the
official views of the National Institute on Drug Abuse, the National
Cancer Institute, or the National Institutes of Health.

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
