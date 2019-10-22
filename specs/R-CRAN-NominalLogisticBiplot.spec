%global packname  NominalLogisticBiplot
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Biplot representations of categorical data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-gmodels 
BuildRequires:    R-MASS 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-gmodels 
Requires:         R-MASS 

%description
Analysis of a matrix of polytomous items using Nominal Logistic Biplots
(NLB) according to Hernandez-Sanchez and Vicente-Villardon (2013). The NLB
procedure extends the binary logistic biplot to nominal (polytomous) data.
The individuals are represented as points on a plane and the variables are
represented as convex prediction regions rather than vectors as in a
classical or binary biplot. Using the methods from Computational Geometry,
the set of prediction regions is converted to a set of points in such a
way that the prediction for each individual is established by its closest
"category point". Then interpretation is based on distances rather than on
projections. In this package we implement the geometry of such a
representation and construct computational algorithms for the estimation
of parameters and the calculation of prediction regions.

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
