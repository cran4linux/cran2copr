%global packname  mrbsizeR
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Scale Space Multiresolution Analysis of Random Signals

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-fields >= 8.10
BuildRequires:    R-CRAN-maps >= 3.1.1
BuildRequires:    R-stats >= 3.0.0
BuildRequires:    R-grDevices >= 3.0.0
BuildRequires:    R-graphics >= 3.0.0
BuildRequires:    R-methods >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
Requires:         R-CRAN-fields >= 8.10
Requires:         R-CRAN-maps >= 3.1.1
Requires:         R-stats >= 3.0.0
Requires:         R-grDevices >= 3.0.0
Requires:         R-graphics >= 3.0.0
Requires:         R-methods >= 3.0.0
Requires:         R-CRAN-Rcpp >= 0.12.14

%description
A method for the multiresolution analysis of spatial fields and images to
capture scale-dependent features. mrbsizeR is based on scale space
smoothing and uses differences of smooths at neighbouring scales for
finding features on different scales. To infer which of the captured
features are credible, Bayesian analysis is used. The scale space
multiresolution analysis has three steps: (1) Bayesian signal
reconstruction. (2) Using differences of smooths, scale-dependent features
of the reconstructed signal can be found. (3) Posterior credibility
analysis of the differences of smooths created. The method has first been
proposed by Holmstrom, Pasanen, Furrer, Sain (2011)
<DOI:10.1016/j.csda.2011.04.011>. Matlab code is available under
<http://cc.oulu.fi/~lpasanen/MRBSiZer/>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
