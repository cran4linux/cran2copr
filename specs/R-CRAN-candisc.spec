%global packname  candisc
%global packver   0.8-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          2%{?dist}
Summary:          Visualizing Generalized Canonical Discriminant and CanonicalCorrelation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-heplots >= 0.8.6
BuildRequires:    R-CRAN-car 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-heplots >= 0.8.6
Requires:         R-CRAN-car 
Requires:         R-graphics 
Requires:         R-stats 

%description
Functions for computing and visualizing generalized canonical discriminant
analyses and canonical correlation analysis for a multivariate linear
model. Traditional canonical discriminant analysis is restricted to a
one-way 'MANOVA' design and is equivalent to canonical correlation
analysis between a set of quantitative response variables and a set of
dummy variables coded from the factor variable. The 'candisc' package
generalizes this to higher-way 'MANOVA' designs for all factors in a
multivariate linear model, computing canonical scores and vectors for each
term. The graphic functions provide low-rank (1D, 2D, 3D) visualizations
of terms in an 'mlm' via the 'plot.candisc' and 'heplot.candisc' methods.
Related plots are now provided for canonical correlation analysis when all
predictors are quantitative.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
