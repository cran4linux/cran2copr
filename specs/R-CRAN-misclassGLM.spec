%global __brp_check_rpaths %{nil}
%global packname  misclassGLM
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          Computation of Generalized Linear Models with MisclassifiedCovariates Using Side Information

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-mlogit 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-bigmemory 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-mlogit 

%description
Estimates models that extend the standard GLM to take misclassification
into account. The models require side information from a secondary data
set on the misclassification process, i.e. some sort of misclassification
probabilities conditional on some common covariates. A detailed
description of the algorithm can be found in Dlugosz, Mammen and Wilke
(2015) <http://www.zew.de/PU70410>.

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
%{rlibdir}/%{packname}
