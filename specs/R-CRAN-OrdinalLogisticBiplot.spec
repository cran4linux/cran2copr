%global packname  OrdinalLogisticBiplot
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          2%{?dist}
Summary:          Biplot representations of ordinal variables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-NominalLogisticBiplot 
Requires:         R-CRAN-mirt 
Requires:         R-MASS 
Requires:         R-CRAN-NominalLogisticBiplot 

%description
Analysis of a matrix of polytomous items using Ordinal Logistic Biplots
(OLB) The OLB procedure extends the binary logistic biplot to ordinal
(polytomous) data. The individuals are represented as points on a plane
and the variables are represented as lines rather than vectors as in a
classical or binary biplot, specifying the points for each of the
categories of the variable. The set of prediction regions is established
by stripes perpendicular to the line between the category points, in such
a way that the prediction for each individual is given by its projection
into the line of the variable.

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
