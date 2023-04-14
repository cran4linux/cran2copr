%global __brp_check_rpaths %{nil}
%global packname  MVR
%global packver   1.33.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.33.0
Release:          3%{?dist}%{?buildtag}
Summary:          Mean-Variance Regularization

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
Requires:         R-CRAN-statmod 
Requires:         R-parallel 
Requires:         R-methods 

%description
This is a non-parametric method for joint adaptive mean-variance
regularization and variance stabilization of high-dimensional data. It is
suited for handling difficult problems posed by high-dimensional
multivariate datasets (p >> n paradigm). Among those are that the variance
is often a function of the mean, variable-specific estimators of variances
are not reliable, and tests statistics have low powers due to a lack of
degrees of freedom. Key features include: (i) Normalization and/or
variance stabilization of the data, (ii) Computation of
mean-variance-regularized t-statistics (F-statistics to follow), (iii)
Generation of diverse diagnostic plots, (iv) Computationally efficient
implementation using C/C++ interfacing and an option for parallel
computing to enjoy a faster and easier experience in the R environment.

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
