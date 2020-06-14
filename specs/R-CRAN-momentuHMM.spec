%global packname  momentuHMM
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          2%{?dist}
Summary:          Maximum Likelihood Analysis of Animal Movement Behavior UsingMultivariate Hidden Markov Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-crawl >= 2.2.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-CircStats 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mitools 
BuildRequires:    R-CRAN-moveHMM 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-argosfilter 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Brobdingnag 
BuildRequires:    R-CRAN-conicfit 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-qdapRegex 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-crawl >= 2.2.1
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-CircStats 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mitools 
Requires:         R-CRAN-moveHMM 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-argosfilter 
Requires:         R-CRAN-car 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-sp 
Requires:         R-MASS 
Requires:         R-CRAN-Brobdingnag 
Requires:         R-CRAN-conicfit 
Requires:         R-CRAN-nleqslv 
Requires:         R-survival 
Requires:         R-CRAN-qdapRegex 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-rlang 

%description
Extended tools for analyzing telemetry data using generalized hidden
Markov models. Features of momentuHMM (pronounced ``momentum'') include
data pre-processing and visualization, fitting HMMs to location and
auxiliary biotelemetry or environmental data, biased and correlated random
walk movement models, hierarchical HMMs, multiple imputation for
incorporating location measurement error and missing data, user-specified
design matrices and constraints for covariate modelling of parameters,
random effects, decoding of the state process, visualization of fitted
models, model checking and selection, and simulation. See McClintock and
Michelot (2018) <doi:10.1111/2041-210X.12995>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
