%global packname  BivRegBLS
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Tolerance Interval and EIV Regression - Method ComparisonStudies

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ellipse 
Requires:         R-CRAN-ellipse 

%description
Assess the agreement in method comparison studies by tolerance intervals
and errors-in-variables (EIV) regressions. The Ordinary Least Square
regressions (OLSv and OLSh), the Deming Regression (DR), and the
(Correlated)-Bivariate Least Square regressions (BLS and CBLS) can be used
with unreplicated or replicated data. The BLS() and CBLS() are the two
main functions to estimate a regression line, while XY.plot() and
MD.plot() are the two main graphical functions to display, respectively an
(X,Y) plot or (M,D) plot with the BLS or CBLS results. Four hyperbolic
statistical intervals are provided: the Confidence Interval (CI), the
Confidence Bands (CB), the Prediction Interval and the Generalized
prediction Interval. Assuming no proportional bias, the (M,D) plot
(Band-Altman plot) may be simplified by calculating univariate tolerance
intervals (beta-expectation (type I) or beta-gamma content (type II)).
Major updates from last version 1.0.0 are: title shortened, include the
new functions BLS.fit() and CBLS.fit() as shortcut of the, respectively,
functions BLS() and CBLS(). References: B.G. Francq, B. Govaerts (2016)
<doi:10.1002/sim.6872>, B.G. Francq, B. Govaerts (2014)
<doi:10.1016/j.chemolab.2014.03.006>, B.G. Francq, B. Govaerts (2014)
<http://publications-sfds.fr/index.php/J-SFdS/article/view/262>, B.G.
Francq (2013), PhD Thesis, UCLouvain, Errors-in-variables regressions to
assess equivalence in method comparison studies,
<https://dial.uclouvain.be/pr/boreal/object/boreal%3A135862/datastream/PDF_01/view>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
