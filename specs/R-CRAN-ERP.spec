%global packname  ERP
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          2%{?dist}
Summary:          Significance Analysis of Event-Related Potentials Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-pacman 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-fdrtool 
Requires:         R-splines 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-pacman 

%description
Functions for signal detection and identification designed for
Event-Related Potentials (ERP) data in a linear model framework. The
functional F-test proposed in Causeur, Sheu, Perthame, Rufini (2018,
submitted) for analysis of variance issues in ERP designs is implemented
for signal detection (tests for mean difference among groups of curves in
One-way ANOVA designs for example). Once an experimental effect is
declared significant, identification of significant intervals is achieved
by the multiple testing procedures reviewed and compared in Sheu,
Perthame, Lee and Causeur (2016, <DOI:10.1214/15-AOAS888>). Some of the
methods gathered in the package are the classical FDR- and
FWER-controlling procedures, also available using function p.adjust. The
package also implements the Guthrie-Buchwald procedure (Guthrie and
Buchwald, 1991 <DOI:10.1111/j.1469-8986.1991.tb00417.x>), which accounts
for the auto-correlation among t-tests to control erroneous detection of
short intervals. The Adaptive Factor-Adjustment method is an extension of
the method described in Causeur, Chu, Hsieh and Sheu (2012,
<DOI:10.3758/s13428-012-0230-0>). It assumes a factor model for the
correlation among tests and combines adaptively the estimation of the
signal and the updating of the dependence modelling (see Sheu et al.,
2016, <DOI:10.1214/15-AOAS888> for further details).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
