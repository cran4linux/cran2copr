%global packname  r2glmm
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Computes R Squared for Mixed (Multilevel) Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-pbkrtest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-afex 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-mgcv 
Requires:         R-CRAN-lmerTest 
Requires:         R-Matrix 
Requires:         R-CRAN-pbkrtest 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-afex 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 

%description
The model R squared and semi-partial R squared for the linear and
generalized linear mixed model (LMM and GLMM) are computed with confidence
limits. The R squared measure from Edwards et.al (2008)
<DOI:10.1002/sim.3429> is extended to the GLMM using penalized
quasi-likelihood (PQL) estimation (see Jaeger et al. 2016
<DOI:10.1080/02664763.2016.1193725>). Three methods of computation are
provided and described as follows. First, The Kenward-Roger approach. Due
to some inconsistency between the 'pbkrtest' package and the 'glmmPQL'
function, the Kenward-Roger approach in the 'r2glmm' package is limited to
the LMM. Second, The method introduced by Nakagawa and Schielzeth (2013)
<DOI:10.1111/j.2041-210x.2012.00261.x> and later extended by Johnson
(2014) <DOI:10.1111/2041-210X.12225>. The 'r2glmm' package only computes
marginal R squared for the LMM and does not generalize the statistic to
the GLMM; however, confidence limits and semi-partial R squared for fixed
effects are useful additions. Lastly, an approach using standardized
generalized variance (SGV) can be used for covariance model selection.
Package installation instructions can be found in the readme file.

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
%{rlibdir}/%{packname}/INDEX
