%global __brp_check_rpaths %{nil}
%global packname  mosaicModel
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          An Interface to Statistical Modeling Independent of ModelArchitecture

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-mosaicCore 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggformula 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyverse 
Requires:         R-CRAN-mosaicCore 
Requires:         R-splines 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggformula 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-knitr 
Requires:         R-MASS 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyverse 

%description
Provides functions for evaluating, displaying, and interpreting
statistical models. The goal is to abstract the operations on models from
the particular architecture of the model. For instance, calculating effect
sizes rather than looking at coefficients. The package includes interfaces
to both regression and classification architectures, including lm(),
glm(), rlm() in 'MASS', random forests and recursive partitioning,
k-nearest neighbors, linear and quadratic discriminant analysis, and
models produced by the 'caret' package's train(). It's straightforward to
add in other other model architectures.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
