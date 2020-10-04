%global packname  ade4
%global packver   1.7-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.15
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Ecological Data: Exploratory and Euclidean Methodsin Environmental Sciences

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pixmap 
BuildRequires:    R-CRAN-sp 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-MASS 
Requires:         R-CRAN-pixmap 
Requires:         R-CRAN-sp 

%description
Tools for multivariate data analysis. Several methods are provided for the
analysis (i.e., ordination) of one-table (e.g., principal component
analysis, correspondence analysis), two-table (e.g., coinertia analysis,
redundancy analysis), three-table (e.g., RLQ analysis) and K-table (e.g.,
STATIS, multiple coinertia analysis). The philosophy of the package is
described in Dray and Dufour (2007) <doi:10.18637/jss.v022.i04>.

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
%doc %{rlibdir}/%{packname}/pictures
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
