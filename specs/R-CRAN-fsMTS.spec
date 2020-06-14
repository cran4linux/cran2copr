%global packname  fsMTS
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          2%{?dist}
Summary:          Feature Selection for Multivariate Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-mpmi 
BuildRequires:    R-CRAN-freqdom 
BuildRequires:    R-CRAN-randomForestSRC 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-mpmi 
Requires:         R-CRAN-freqdom 
Requires:         R-CRAN-randomForestSRC 

%description
Implements feature selection routines for multivariate time series (MTS).
The list of implemented algorithms includes: own lags (independent MTS
components), distance-based (using external structure, e.g. Pfeifer and
Deutsch (1980) <doi:10.2307/1268381>), cross-correlation (see Schelter et
al. (2006, ISBN:9783527406234)), graphical LASSO (see Haworth and Cheng
(2014) <https://www.gla.ac.uk/media/Media_401739_smxx.pdf>), random forest
(see Pavlyuk (2020) "Random Forest Variable Selection for Sparse Vector
Autoregressive Models" in Contributions to Statistics, in production),
least angle regression (see Gelper and Croux (2008)
<https://lirias.kuleuven.be/retrieve/16024>), mutual information (see
Schelter et al. (2006, ISBN:9783527406234), Liu et al. (2016)
<doi:10.1109/ChiCC.2016.7554480>), and partial spectral coherence (see
Davis et al.(2016) <doi:10.1080/10618600.2015.1092978>). In addition, the
package implements functions for ensemble feature selection (using feature
ranking and majority voting). The package is implemented within Dmitry
Pavlyuk's research project No. 1.1.1.2/VIAA/1/16/112 "Spatiotemporal urban
traffic modelling using big data".

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
