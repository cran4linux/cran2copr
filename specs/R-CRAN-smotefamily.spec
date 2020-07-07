%global packname  smotefamily
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}
Summary:          A Collection of Oversampling Techniques for Class ImbalanceProblem Based on SMOTE

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-igraph 

%description
A collection of various oversampling techniques developed from SMOTE is
provided. SMOTE is a oversampling technique which synthesizes a new
minority instance between a pair of one minority instance and one of its K
nearest neighbor. (see
<https://www.jair.org/media/953/live-953-2037-jair.pdf> for more
information) Other techniques adopt this concept with other criteria in
order to generate balanced dataset for class imbalance problem.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
