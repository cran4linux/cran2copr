%global packname  mudfold
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Multiple UniDimensional unFOLDing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.3
Requires:         R-core >= 3.3.3
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
Requires:         R-boot 
Requires:         R-CRAN-glmnet 
Requires:         R-mgcv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 

%description
Nonparametric unfolding item response theory (IRT) model for dichotomous
data (see W.H. Van Schuur (1984). Structure in Political Beliefs: A New
Model for Stochastic Unfolding with Application to European Party
Activists, and W.J.Post (1992). Nonparametric Unfolding Models: A Latent
Structure Approach). The package implements MUDFOLD (Multiple
UniDimensional unFOLDing), an iterative item selection algorithm that
constructs unfolding scales from dichotomous preferential-choice data
without explicitly assuming a parametric form of the item response
functions. Scale diagnostics from Post(1992) and estimates for the person
locations proposed by Johnson(2006) and Van Schuur(1984) are also
available. This model can be seen as the unfolding variant of Mokken(1971)
scaling method.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
