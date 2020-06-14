%global packname  MachineLearning
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          2%{?dist}
Summary:          Machine Learning Algorithms for Innovation in Tourism

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-NbClust 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-FSelectorRcpp 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rpart.plot 
Requires:         R-CRAN-NbClust 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-arules 
Requires:         R-rpart 
Requires:         R-CRAN-FSelectorRcpp 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rpart.plot 

%description
A collection of routines created in the collaboration framework in tourism
innovation between the Valencian Tourism Agency (AVT)
<http://www.turisme.gva.es/opencms/opencms/turisme/es/index.jsp> and the
Miguel Hernandez University. The package provides a set of machine
learning tools for pattern detection, association and classification rules
and feature selection even under massive data environments. Almiñana,
Escudero, Pérez-Martín, Rabasa, and Santamaría (2014)
<doi:10.1007/s11750-012-0264-6>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
