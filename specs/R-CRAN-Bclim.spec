%global packname  Bclim
%global packver   3.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.2
Release:          1%{?dist}
Summary:          Bayesian Palaeoclimate Reconstruction from Pollen Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-CRAN-mclust 
Requires:         R-graphics 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-ggplot2 

%description
Takes pollen and chronology data from lake cores and produces a Bayesian
posterior distribution of palaeoclimate from that location after fitting a
non-linear non-Gaussian state-space model. For more details see the paper
Parnell et al. (2015), Bayesian inference for palaeoclimate with time
uncertainty and stochastic volatility. Journal of the Royal Statistical
Society: Series C (Applied Statistics), 64: 115–138
<DOI:10.1111/rssc.12065>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
