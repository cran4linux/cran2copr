%global packname  mratios
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}
Summary:          Ratios of Coefficients in the General Linear Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-survPresmooth 
BuildRequires:    R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-multcomp 
Requires:         R-survival 
Requires:         R-CRAN-survPresmooth 
Requires:         R-stats 

%description
Performs (simultaneous) inferences for ratios of linear combinations of
coefficients in the general linear model, linear mixed model, and for
quantiles in a one-way layout. Multiple comparisons and simultaneous
confidence interval estimations can be performed for ratios of treatment
means in the normal one-way layout with homogeneous and heterogeneous
treatment variances, according to Dilba et al. (2007)
<https://cran.r-project.org/doc/Rnews/Rnews_2007-1.pdf> and Hasler and
Hothorn (2008) <doi:10.1002/bimj.200710466>. Confidence interval
estimations for ratios of linear combinations of linear model parameters
like in (multiple) slope ratio and parallel line assays can be carried
out. Moreover, it is possible to calculate the sample sizes required in
comparisons with a control based on relative margins. For the simple
two-sample problem, functions for a t-test for ratio-formatted hypotheses
and the corresponding confidence interval are provided assuming
homogeneous or heterogeneous group variances.

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
%{rlibdir}/%{packname}/INDEX
