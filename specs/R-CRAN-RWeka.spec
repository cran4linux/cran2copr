%global packname  RWeka
%global packver   0.4-42
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.42
Release:          2%{?dist}
Summary:          R/Weka Interface

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RWekajars >= 3.9.3.1
BuildRequires:    R-CRAN-rJava >= 0.6.3
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grid 
Requires:         R-CRAN-RWekajars >= 3.9.3.1
Requires:         R-CRAN-rJava >= 0.6.3
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grid 

%description
An R interface to Weka (Version 3.9.3). Weka is a collection of machine
learning algorithms for data mining tasks written in Java, containing
tools for data pre-processing, classification, regression, clustering,
association rules, and visualization.  Package 'RWeka' contains the
interface code, the Weka jar is in a separate package 'RWekajars'.  For
more information on Weka see <http://www.cs.waikato.ac.nz/ml/weka/>.

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
%doc %{rlibdir}/%{packname}/arff
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX
