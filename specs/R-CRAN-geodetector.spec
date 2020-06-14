%global packname  geodetector
%global packver   1.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          2%{?dist}
Summary:          Stratified Heterogeneity Measure, Dominant Driving ForceDetection, Interaction Relationship Investigation

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sp >= 1.2.7
BuildRequires:    R-CRAN-rgdal >= 1.2.16
BuildRequires:    R-CRAN-rgeos >= 0.3.26
BuildRequires:    R-CRAN-maptools 
Requires:         R-CRAN-sp >= 1.2.7
Requires:         R-CRAN-rgdal >= 1.2.16
Requires:         R-CRAN-rgeos >= 0.3.26
Requires:         R-CRAN-maptools 

%description
Spatial stratified heterogeneity (SSH), referring to the within strata are
more similar than the between strata, a model with global parameters would
be confounded if input data is SSH. Note that the "spatial" here can be
either geospatial or the space in mathematical meaning. Geographical
detector is a novel tool to investigate SSH: (1) measure and find SSH of a
variable Y; (2) test the power of determinant X of a dependent variable Y
according to the consistency between their spatial distributions; and (3)
investigate the interaction between two explanatory variables X1 and X2 to
a dependent variable Y (Wang et al 2014 <doi:10.1080/13658810802443457>,
Wang, Zhang, and Fu 2016 <doi:10.1016/j.ecolind.2016.02.052>).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
