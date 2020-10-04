%global packname  rCBA
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          3%{?dist}%{?buildtag}
Summary:          CBA Classifier

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-TunePareto 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-TunePareto 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides implementations of a classifier based on the "Classification
Based on Associations" (CBA). It can be used for building classification
models from association rules. Rules are pruned in the order of precedence
given by the sort criteria and a default rule is added. The final
classifier labels provided instances. CBA was originally proposed by Liu,
B. Hsu, W. and Ma, Y. Integrating Classification and Association Rule
Mining. Proceedings KDD-98, New York, 27-31 August. AAAI. pp80-86 (1998,
ISBN:1-57735-070-7).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
