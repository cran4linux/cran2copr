%global packname  shapes
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}
Summary:          Statistical Shape Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-MASS 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-rgl 
Requires:         R-MASS 

%description
Routines for the statistical analysis of landmark shapes, including
Procrustes analysis, graphical displays, principal components analysis,
permutation and bootstrap tests, thin-plate spline transformation grids
and comparing covariance matrices. See Dryden, I.L. and Mardia, K.V.
(2016). Statistical shape analysis, with Applications in R (2nd Edition),
John Wiley and Sons.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
