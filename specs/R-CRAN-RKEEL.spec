%global packname  RKEEL
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          Using KEEL in R Code

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RKEELdata >= 1.0.5
BuildRequires:    R-CRAN-RKEELjars >= 1.0.19
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-pmml 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-rJava 
Requires:         R-CRAN-RKEELdata >= 1.0.5
Requires:         R-CRAN-RKEELjars >= 1.0.19
Requires:         R-CRAN-R6 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-pmml 
Requires:         R-CRAN-arules 
Requires:         R-Matrix 
Requires:         R-CRAN-rJava 

%description
'KEEL' is a popular Java software for a large number of different
knowledge data discovery tasks. This package takes the advantages of
'KEEL' and R, allowing to use 'KEEL' algorithms in simple R code. The
implemented R code layer between R and 'KEEL' makes easy both using 'KEEL'
algorithms in R as implementing new algorithms for 'RKEEL' in a very
simple way. It includes more than 100 algorithms for classification,
regression, preprocess, association rules and imbalance learning, which
allows a more complete experimentation process. For more information about
KEEL, see <http://www.keel.es/>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
