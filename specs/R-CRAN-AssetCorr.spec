%global packname  AssetCorr
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}
Summary:          Estimating Asset Correlations from Default Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-VineCopula 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-mvQuad 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-VineCopula 
Requires:         R-CRAN-mvtnorm 
Requires:         R-boot 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-mvQuad 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rdpack 

%description
Functions for the estimation of intra- and inter-cohort correlations in
the Vasicek credit portfolio model. For intra-cohort correlations, the
package covers the two method of moments estimators of Gordy (2000)
<doi:10.1016/S0378-4266(99)00054-0>, the method of moments estimator of
Lucas (1995) <http://jfi.iijournals.com/content/4/4/76> and a Binomial
approximation extension of this approach. Moreover, the maximum likelihood
estimators of Gordy and Heitfield (2010)
<http://elsa.berkeley.edu/~mcfadden/e242_f03/heitfield.pdf> and Duellmann
and Gehde-Trapp (2004) <http://hdl.handle.net/10419/19729> are
implemented. For inter-cohort correlations, the method of moments
estimator of Bluhm and Overbeck (2003)
<doi:10.1007/978-3-642-59365-9_2>/Bams et al. (2016)
<https://ssrn.com/abstract=2676595> is provided and the maximum likelihood
estimators comprise the approaches of Gordy and Heitfield
(2010)/Kalkbrener and Onwunta (2010) <ISBN: 978-1906348250> and Pfeuffer
et al. (2018). Bootstrap and Jackknife procedures for bias correction are
included as well as the method of moments estimator of Frei and Wunsch
(2018) <doi:10.21314/JCR.2017.231> for auto-correlated time series.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%doc %{rlibdir}/%{packname}/REFERENCES.bib.sav
%{rlibdir}/%{packname}/INDEX
