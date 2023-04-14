%global __brp_check_rpaths %{nil}
%global packname  genridge
%global packver   0.6.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.7
Release:          3%{?dist}%{?buildtag}
Summary:          Generalized Ridge Trace Plots for Ridge Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.11.1
Requires:         R-core >= 2.11.1
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-car 

%description
The genridge package introduces generalizations of the standard univariate
ridge trace plot used in ridge regression and related methods.  These
graphical methods show both bias (actually, shrinkage) and precision, by
plotting the covariance ellipsoids of the estimated coefficients, rather
than just the estimates themselves.  2D and 3D plotting methods are
provided, both in the space of the predictor variables and in the
transformed space of the PCA/SVD of the predictors.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
