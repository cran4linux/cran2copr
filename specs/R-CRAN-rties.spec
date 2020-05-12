%global packname  rties
%global packver   5.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.0.0
Release:          1%{?dist}
Summary:          Modeling Interpersonal Dynamics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-DataCombine 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-interactions 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-nlme 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-DataCombine 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-interactions 
Requires:         R-lattice 
Requires:         R-CRAN-lme4 
Requires:         R-MASS 
Requires:         R-CRAN-mclust 
Requires:         R-nlme 
Requires:         R-nnet 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-zoo 

%description
The name of this package grew out of our research on temporal
interpersonal emotion systems (TIES), hence 'rties'. It provides tools for
using a set of models to investigate temporal processes in bivariate
(e.g., dyadic) systems. The general approach is to model, one dyad at a
time, the dynamics of a variable that is assessed repeatedly from both
partners, extract the parameter estimates for each dyad, and then use
those parameter estimates as input to a latent profile analysis to extract
groups of dyads with qualitatively distinct dynamics. Finally, the profile
memberships can be used to either predict, or be predicted by, another
variable of interest. Currently, 2 models are supported: 1)
inertia-coordination, and 2) a coupled-oscillator. Extended documentation
is provided in vignettes. Theoretical background can be found in Butler
(2011) <doi:10.1177/1088868311411164> and Butler & Barnard (2019)
<doi:10.1097/PSY.0000000000000703>.

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
