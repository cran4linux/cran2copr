%global packname  naivereg
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Nonparametric Additive Instrumental Variable Estimator: A GroupShrinkage Estimation Perspective

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-grpreg 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-gmm 
BuildRequires:    R-stats 
Requires:         R-CRAN-grpreg 
Requires:         R-splines 
Requires:         R-CRAN-gmm 
Requires:         R-stats 

%description
In empirical studies, instrumental variable (IV) regression is the
signature method to solve the endogeneity problem. If we enforce the
exogeneity condition of the IV, it is likely that we end up with a large
set of IVs without knowing which ones are good. This package uses adaptive
group lasso and B-spline methods to select the nonparametric components of
the IV function, with the linear function being a special case. The
package incorporates two stage least squares estimator (2SLS), generalized
method of moment (GMM), generalized empirical likelihood (GEL) methods
post instrument selection. It is nonparametric version of 'ivregress' in
'Stata' with IV selection and high dimensional features. The package is
based on the paper "Nonparametric Additive Instrumental Variable
Estimator: A Group Shrinkage Estimation Perspective" (2017) published
online in Journal of Business & Economic Statistics
<doi:10.1080/07350015.2016.1180991>.

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
